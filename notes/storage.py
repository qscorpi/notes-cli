import json
from pathlib import Path

NOTES_FILE = Path.home() / ".notes.json"


def load_notes() -> list[dict]:
    """Загрузить заметки из файла. Если файла нет — вернуть пустой список."""
    if not NOTES_FILE.exists():
        return []
    with NOTES_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(notes: list[dict]) -> None:
    """Сохранить заметки в файл."""
    with NOTES_FILE.open("w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
