# Standard imports
import sys
from kivy.app import App

# kivy Imports
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.graphics import (
    Color, RoundedRectangle,
    )

# App Imports
from components.buttons import Tbutton
from components.text import TextLabel

# Configurations window
from kivy.core.window import Window
from kivy.config import Config 

_fized_size = (300, 400)

Window.size = _fized_size
Window.left = 400
Window.top = 200
Window.borderless = False

def block_resize(*args) -> None:
    Window.size = _fized_size

Window.bind(size = block_resize)


class Background(Widget):
    radius: list = ListProperty([15, 15, 15, 15])
    color: list = ListProperty([0.2, .2, .2, 1])
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)

        # Binding all properties in the specific function
        # Background
        self.bind(
            pos = self._do_background,
            x = self._do_background,
            y = self._do_background,
            size = self._do_background,
            width = self._do_background,
            height = self._do_background,
            size_hint = self._do_background,
            color = self._do_background,
            radius = self._do_background,
        )

    def _do_background(self, *args) -> None: 
        # Reset canvas before
        self.canvas.before.clear()
        # Draw background
        with self.canvas.before:
            Color(*self.color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)

class LoginPage(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        background = Background()
        background.size_hint = .95, .95
        background.pos_hint = {'x': 0.025, 'y': .025}

        text_username = TextLabel(text='Username:')
        text_username.size_hint = .8, .07
        text_username.pos_hint = {'x': .1, 'y': .6}

        login_input = TextInput()
        login_input.size_hint = .8, .07
        login_input.pos_hint = {'x': .1, 'y': .52}

        text_password = TextLabel(text='Password:')
        text_password.size_hint = .8, .07
        text_password.pos_hint = {'x': .1, 'y': .46}

        password_input = TextInput()
        password_input.password = True
        password_input.size_hint = .8, .07
        password_input.pos_hint = {'x': .1, 'y': .38}

        login_button = Tbutton(text='Login')
        login_button.background_color = [.1, .1, .1, 1]
        login_button.size_hint = .8, .07
        login_button.pos_hint = {'x': .1, 'y': .3}
        
        text_login = Label(text='LOGIN')
        text_login.font_size = 35
        text_login.size_hint = .8, .07
        text_login.pos_hint = {'center_x': .5, 'center_y': .79}

        builder_list: list = [
            background, login_button, 
            text_username, login_input, 
            text_password, password_input, 
            text_login,
            ]

        for wid in builder_list:
            self.add_widget(wid)

class BuilderApp(App):
    def build(self) -> Widget:
        # Basics Configs
        self.title = 'LoginSystem'
        self.icon = r'media\images\loginicon.png'
     
        return LoginPage()

if __name__ == '__main__':
    APPLICATION = BuilderApp()
    APPLICATION.run()
    sys.exit(APPLICATION)