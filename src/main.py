import tkinter as tk
import sqlite3
from tkinter import messagebox
import requests
import os

# Определяем текущую директорию и создаем папку db, если она не существует
current_directory = os.path.dirname(os.path.abspath(__file__))
db_directory = os.path.join(current_directory, 'db')

if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Путь к базе данных
db_path = os.path.join(db_directory, 'notes.db')

# Функция для загрузки тем из файла на GitHub
def load_theme():
    url = "https://raw.githubusercontent.com/DKLiberty/MindLog/develop/src/theme.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        theme = {}
        for line in response.text.splitlines():
            key, value = line.strip().split('=')
            theme[key] = value
        return theme
    else:
        messagebox.showerror("Ошибка", "Не удалось загрузить тему из GitHub.")
        return {}

# Создание/подключение к базе данных SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT NOT NULL
    )
''')

# Функция для добавления заметки в базу данных
def add_note():
    note = note_text.get("1.0", tk.END).strip()  # Получаем текст заметки
    if note:
        cursor.execute('INSERT INTO notes (note) VALUES (?)', (note,))
        conn.commit()  # Сохраняем изменения
        messagebox.showinfo("Успех", "Заметка добавлена!")
        note_text.delete("1.0", tk.END)  # Очищаем текстовое поле
    else:
        messagebox.showwarning("Ошибка", "Заметка не может быть пустой!")

# Создание интерфейса
root = tk.Tk()
root.title("Заметки")

# Загрузка стилей из файла
theme = load_theme()

# Применение стилей
root.configure(bg=theme['background_color'])

# Текстовое поле для ввода заметки
note_text = tk.Text(root, width=40, height=10, font=(theme['font_family'], int(theme['font_size'])), bg=theme['text_bg'], fg=theme['text_fg'])
note_text.pack(pady=10)

# Кнопка для добавления заметки
add_button = tk.Button(root, text="Добавить заметку", command=add_note, font=(theme['font_family'], int(theme['button_font_size'])), bg=theme['button_bg'], fg=theme['button_fg'])
add_button.pack(pady=10)

root.mainloop()

# Закрываем соединение с базой данных при выходе
conn.close()