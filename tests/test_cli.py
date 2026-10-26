from unittest.mock import patch

from notes.cli import add_note, delete_note, list_notes


@patch("notes.cli.save_notes")
@patch("notes.cli.load_notes")
def test_add_note(mock_load, mock_save, capsys):
    # 1. Настраиваем мок: load_notes вернёт пустой список
    mock_load.return_value = []

    # 2. Вызываем функцию
    add_note("Тестовая заметка")

    # 3. Проверяем, что save_notes была вызвана с правильным списком
    mock_save.assert_called_once_with([{"text": "Тестовая заметка"}])

    # 4. Проверяем, что вывелось в консоль
    captured = capsys.readouterr()
    assert captured.out == "Добавлено: Тестовая заметка\n"


@patch("notes.cli.load_notes")
def test_list_notes_empty(mock_load, capsys):
    mock_load.return_value = []

    list_notes()

    captured = capsys.readouterr()
    assert captured.out == "Заметок нет.\n"


@patch("notes.cli.load_notes")
def test_list_notes_with_data(mock_load, capsys):
    mock_load.return_value = [{"text": "Купить молоко"}, {"text": "Позвонить маме"}]

    list_notes()

    captured = capsys.readouterr()
    assert "1. Купить молоко" in captured.out
    assert "2. Позвонить маме" in captured.out


@patch("notes.cli.save_notes")
@patch("notes.cli.load_notes")
def test_delete_note_success(mock_load, mock_save, capsys):
    mock_load.return_value = [{"text": "Удалить меня"}]

    delete_note(1)

    mock_save.assert_called_once_with([])  # список стал пустым

    captured = capsys.readouterr()
    assert captured.out == "Удалено: Удалить меня\n"


@patch("notes.cli.load_notes")
def test_delete_note_out_of_bounds(mock_load, capsys):
    mock_load.return_value = [{"text": "Единственная заметка"}]

    delete_note(99)

    captured = capsys.readouterr()
    assert "Заметки с номером 99 не существует" in captured.out
