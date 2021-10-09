# Standard imports
import sys
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

# kivy Imports
from kivy.uix.widget import Widget

# App Imports
from components.frame import Frame
from view.loginframe import LoginFrame
from view.registerframe import RegisterFrame

# Configurations window
from kivy.core.window import Window
Window.size = 800, 600

class ManagerPages(FloatLayout):
    def __init__(self, **kwargs):
        super(ManagerPages, self).__init__(**kwargs)
 
        self.login_frame = LoginFrame()
        self.register_frame = RegisterFrame()

        # Register in login frame
        self.login_frame.register_button.released_function = self.call_page
        self.login_frame.register_button.released_args = [self.register_frame]

        # Register in register frame
        self.register_frame.confirm_register_button.released_function = self.call_page
        self.register_frame.confirm_register_button.released_args = [self.login_frame]

        self.add_widget(self.login_frame)
    
    def call_page(self, new) -> None:
        for child in self.children:
            self.remove_widget(child)
        self.add_widget(new)

class BuilderApp(App):

    def build(self) -> Widget:
        # Basics Configs
        self.title = 'LoginSystem'
        self.icon = r'media\images\loginicon.png'
        return ManagerPages()

if __name__ == '__main__':
    APPLICATION = BuilderApp()
    APPLICATION.run()
    sys.exit(APPLICATION)
