from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Joshua", "Richard", "Kevin", "Olivier"}

    def build(self):
        self.title = "Dynamic_Name_Lister"
        self.root = Builder.load_file('dynamic_name_lister.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        for name in self.names:

            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
