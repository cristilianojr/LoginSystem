# Standart Imports
import sys
from kivy.app import App

from views.templates import LoginPage
from views.colors_palette import patterns

class MainApp(App):
    def build(self) -> object:
        return LoginPage(patterns['Normal Blue'])

if __name__ == '__main__':
    APP = MainApp()
    APP.run()
    sys.exit(APP)
