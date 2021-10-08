from components.frame import Frame, Background
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from components.text import TextLabel
from components.buttons import Tbutton

class LoginFrame(Frame):
    background = Background()
    background.size_hint = .95, .95
    background.pos_hint = {'x': .025, 'y': .025}

    text_username = TextLabel(text='Username:')
    text_username.size_hint = .8, .07
    text_username.pos_hint = {'x': .1, 'y': .6}

    login_input = TextInput()
    login_input.font_size = 24
    login_input.size_hint = .8, .07
    login_input.pos_hint = {'x': .1, 'y': .52}

    text_password = TextLabel(text='Password:')
    text_password.size_hint = .8, .07
    text_password.pos_hint = {'x': .1, 'y': .46}

    password_input = TextInput()
    password_input.font_size = 24
    password_input.password = True
    password_input.size_hint = .8, .07
    password_input.pos_hint = {'x': .1, 'y': .38}

    connect_button = Tbutton(text='Sign in')
    connect_button.font_size = 20
    connect_button.background_color = [.1, .1, .1, 1]
    connect_button.size_hint = .8, .07
    connect_button.pos_hint = {'x': .1, 'y': .18}

    register_button = Tbutton(text='Sign up')
    register_button.font_size = 20
    register_button.background_color = [.1, .1, .1, 1]
    register_button.size_hint = .8, .07
    register_button.pos_hint = {'x': .1, 'y': .08}
    

    image_login = Image(source=r'media\images\Logo.png')
    image_login.size_hint = .5, .5
    image_login.pos_hint = {'center_x': .5, 'center_y': .79}

    # Is important to build the page frame in order
    builder_list_ordering: list = [
        background, connect_button, 
        text_username, login_input, 
        text_password, password_input, 
        image_login, register_button,
        ]

    def __init__(self, **kwargs):
        super(LoginFrame, self).__init__(**kwargs)

        for wid in self.builder_list_ordering:
            self.add_widget(wid)