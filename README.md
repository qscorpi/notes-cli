# notes-cli

CLI-утилита для заметок на Python. Позволяет добавлять, просматривать и удалять заметки прямо из терминала.

## Требования

- Python 3.11+

## Использование

```bash
# добавить заметку
python notes/notes.py add "Купить молоко"

# показать все заметки
python notes/notes.py list

# удалить заметку по номеру
python notes/notes.py delete 1
```

## Где хранятся заметки

В файле `~/.notes.json` в формате JSON.

## Структура проекта

```
notes-cli/
├── .gitignore
├── README.md
└── notes/
    └── notes.py
```

## Лицензия

MIT
