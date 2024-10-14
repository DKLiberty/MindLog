import tkinter as tk
import sqlite3
from tkinter import messagebox

# Создание/подключение к базе данных SQLite
conn = sqlite3.connect('notes.db')
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

# Текстовое поле для ввода заметки
note_text = tk.Text(root, width=40, height=10)
note_text.pack(pady=10)

# Кнопка для добавления заметки
add_button = tk.Button(root, text="Добавить заметку", command=add_note)
add_button.pack(pady=10)

root.mainloop()

# Закрываем соединение с базой данных при выходе
conn.close()
