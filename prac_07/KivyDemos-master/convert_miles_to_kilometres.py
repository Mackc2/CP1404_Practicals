from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILE_CONVERSION_FACTOR = 1.609344;

class ConvertMilesToKilometres(App):
    def build(self):
        Window.size = (600,300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root


    def handle_increment(self,increment):
        value = self.validate_miles()
        value += increment
        self.root.ids.input_number.text = str(value)

    def handle_convert(self):
        value = self.validate_miles()
        value = value * MILE_CONVERSION_FACTOR
        self.root.ids.answer_display.text = str(value)

    def validate_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

ConvertMilesToKilometres().run()