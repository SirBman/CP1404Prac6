from kivy.app import App
from kivy.lang import Builder

milesToKm = 1.60934

class converterApp (App):
    def build(self):
        self.title = "Converter Demo"
        self.root = Builder.load_file('converter.kv')
        return self.root

    def calculate(self):
        miInput = self.get_miles()
        miInKm = miInput * milesToKm
        self.root.ids.output_value.text = str(miInKm)

    def handle_increment(self, change):

        value = self.get_miles() + change
        self.root.ids.input_dist.text = str(value)
        self.calculate()

    def get_miles(self):
        try:
            value = float(self.root.ids.input_dist.text)
            return value
        except ValueError:
            return 0

converterApp().run()