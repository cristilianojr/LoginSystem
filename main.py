# Standart Imports
import sys
from kivy.app import App

from views.templates import LoginPage


class MainApp(App):
    def build(self) -> object:
        return LoginPage()

if __name__ == '__main__':
    APP = MainApp()
    APP.run()
    sys.exit(APP)
