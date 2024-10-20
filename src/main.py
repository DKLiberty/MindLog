import flet as ft
import os
import subprocess

def main(page: ft.Page):
    page.title = "MindLog"
    page.window_width = 500
    page.window_height = 500
    page.window_resizable = False
    page.window_center()

    select_mylog = ft.Text("Select .mylog file", size=20, weight="bold")
    list_mylog = ft.ListView(expand=True)
    no_mylog = ft.Text("No .mylog File", color = 'red', visible=False)

    def update_file_list():
        current_folder = "."
        mylog_files = []

        for root, dirs, files in os.walk(current_folder):
            for file in files:
                if file.endswith('.mylog'):
                    full_path = os.path.join(root, file)
                    mylog_files.append(full_path)

        if mylog_files:
            list_mylog.controls.clear()
            for mylog_file in mylog_files:
                btn_db = ft.ElevatedButton(text=mylog_file, on_click=lambda e, db=mylog_file: open_mylog_file(db))
                list_mylog.controls.append(btn_db)
            no_mylog.visible = False
        else:
            no_mylog.visible = True
        
        page.update()

    def open_mylog_file(file_path):
        print(f"Opening file: {file_path}")
        page.window_destroy()
        subprocess.run(["source.exe", file_path])

    content_display = ft.Column(
        [
            select_mylog,
            list_mylog,
            no_mylog
        ],
        horizontal_alignment="center"
    )

    page.add(
        content_display
    )

    update_file_list()

ft.app(target=main)
