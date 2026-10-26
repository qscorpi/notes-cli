"""Работа с файловым хранилищем заметок."""

import json
from pathlib import Path

NOTES_FILE = Path.home() / ".notes.json"


def load_notes(path: Path = NOTES_FILE) -> list[dict]:
    """Загрузить заметки из файла. Если файла нет — вернуть пустой список."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(notes: list[dict], path: Path = NOTES_FILE) -> None:
    """Сохранить заметки в файл."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
