"""CLI-утилита для заметок."""

import argparse
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


def add_note(text: str) -> None:
    """Добавить новую заметку."""
    notes = load_notes()
    notes.append({"text": text})
    save_notes(notes)
    print(f"Добавлено: {text}")


def list_notes() -> None:
    """Показать все заметки."""
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note['text']}")


def delete_note(index: int) -> None:
    """Удалить заметку по её номеру (нумерация с 1)."""
    notes = load_notes()
    if not notes:
        print("Заметок нет.")
        return
    if index < 1 or index > len(notes):
        print(f"Заметки с номером {index} не существует. Всего заметок: {len(notes)}.")
        return
    removed = notes.pop(index - 1)
    save_notes(notes)
    print(f"Удалено: {removed['text']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Заметки в командной строке")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Добавить заметку")
    add_parser.add_argument("text", help="Текст заметки")

    subparsers.add_parser("list", help="Показать все заметки")

    delete_parser = subparsers.add_parser("delete", help="Удалить заметку по номеру")
    delete_parser.add_argument("index", type=int, help="Номер заметки (начиная с 1)")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.text)
    elif args.command == "list":
        list_notes()
    elif args.command == "delete":
        delete_note(args.index)


if __name__ == "__main__":
    main()
