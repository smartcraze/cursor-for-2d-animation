import re

def extract_scene_class_name(filepath: str) -> str:
    """Extracts the first class name that inherits from Scene."""
    with open(filepath, "r") as f:
        for line in f:
            match = re.match(r"\s*class\s+(\w+)\s*\(\s*Scene\s*\)", line)
            if match:
                return match.group(1)
    raise ValueError("❌ No Scene class found in the file.")
