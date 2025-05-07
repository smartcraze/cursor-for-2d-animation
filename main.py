from prompt_engine import generate_scene_code
from utils import extract_scene_class_name
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import subprocess
import uuid
import os
import shutil

GENERATED_DIR = "temp/generated"
OUTPUT_DIR = "temp/output"

@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs(GENERATED_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    yield
    if os.path.exists("temp"):
        shutil.rmtree("temp")

app = FastAPI(lifespan=lifespan)

class PromptInput(BaseModel):
    prompt: str
    filename: str
    quality: str = "l"

QUALITY_FLAGS = {
    "l": "-pql",
    "m": "-pqm",
    "h": "-pqh"
}

@app.post("/generate")
async def generate(data: PromptInput):
    try:
        prompt = data.prompt.strip()
        filename = data.filename.strip().replace(" ", "_")
        quality_flag = QUALITY_FLAGS.get(data.quality.lower(), "-pql")

        scene_path = os.path.join(GENERATED_DIR, f"{filename}.py")

        # 1. Generate scene code
        scene_code = generate_scene_code(prompt)
        with open(scene_path, "w") as f:
            f.write(scene_code)

        # 2. Extract class name
        scene_class = extract_scene_class_name(scene_path)
        if not scene_class:
            raise HTTPException(status_code=400, detail="Scene class not found")

        # 3. Render the animation
        result = subprocess.run(
            [
                "manim",
                scene_path,
                scene_class,
                quality_flag,
                "-o", filename,
                "--media_dir", OUTPUT_DIR
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "error": "Manim rendering failed",
                "stderr": result.stderr,
                "stdout": result.stdout
            }

        video_path = os.path.join(OUTPUT_DIR, "videos", "temp", "480p15", f"{filename}.mp4")
        if not os.path.exists(video_path):
            raise HTTPException(status_code=500, detail="Rendered video not found")

        return {
            "message": "✅ Animation created",
            "scene_class": scene_class,
            "video_path": video_path  URL
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
