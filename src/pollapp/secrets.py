from pathlib import Path
import json

def get_secrets(file_path: Path):
    return json.loads(file_path.read_text())