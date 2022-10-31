from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('mainkv.kv')


class MyLayout(BoxLayout):
    press_property = StringProperty("The angle will be displayed here")

    def left_press(self):

        self.press_property = "Left 30°"

    def right_press(self):

        self.press_property = "Right 30°"


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
