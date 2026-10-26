from pathlib import Path

from notes.storage import load_notes, save_notes


def test_save_and_load(tmp_path: Path) -> None:
    # tmp_path — это специальная фикстура pytest.
    # Она создаёт уникальную временную папку для КАЖДОГО теста.
    test_file = tmp_path / "test_notes.json"

    notes_to_save = [{"text": "Заметка 1"}, {"text": "Заметка 2"}]

    # Сохраняем
    save_notes(notes_to_save, path=test_file)

    # Проверяем, что файл реально создался
    assert test_file.exists()

    # Загружаем обратно
    loaded_notes = load_notes(path=test_file)

    # Проверяем, что данные совпадают
    assert loaded_notes == notes_to_save
