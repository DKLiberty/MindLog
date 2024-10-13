from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from database import init_db, add_note

class MindLogApp(App):
    def build(self):
        init_db()
        return BoxLayout()

    def save_note(self):
        note_content = self.root.ids.note_input.text
        add_note(note_content)
        self.root.ids.note_input.text = ''

if __name__ == '__main__':
    MindLogApp().run()
