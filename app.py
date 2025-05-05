import os
from prompt_engine import generate_scene_code
from utils import extract_scene_class_name

def main():
    print("🎬 Manim Cursor - Generate Manim Code from Prompt")
    prompt = input("📝 Enter your prompt: ").strip()
    filename = input("📄 Enter a filename (no .py): ").strip().replace(" ", "_")
    quality = input("🎥 Choose quality [l = low, m = medium, h = high]: ").strip().lower()

    quality_flag = {
        "l": "-pql",
        "m": "-pqm",
        "h": "-pqh"
    }.get(quality, "-pql")

    os.makedirs("generated", exist_ok=True)
    scene_path = f"generated/{filename}.py"

    print("\n🧠 Generating scene code...")
    try:
        scene_code = generate_scene_code(prompt)
        with open(scene_path, "w") as f:
            f.write(scene_code)
        print("✅ Scene code saved at:", scene_path)
    except Exception as e:
        print("❌ Error generating or saving code:", e)
        return

    print("\n🔍 Parsing scene class name...")
    try:
        scene_class = extract_scene_class_name(scene_path)
        print("✅ Scene class found:", scene_class)
    except Exception as e:
        print("❌ Error extracting class name:", e)
        return

    print("\n📦 Copy and run this command to render your animation:\n")
    print(f"cd generated && manim {filename}.py {scene_class} {quality_flag} -o {filename} --media_dir ../output\n")

if __name__ == "__main__":
    main()
