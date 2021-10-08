from components.frame import Frame, Background
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from components.text import TextLabel
from components.buttons import Tbutton

class RegisterFrame(Frame):
    background = Background()
    background.size_hint = .95, .95
    background.pos_hint = {'x': .025, 'y': .025}

    image_login = Image(source=r'media\images\Logo.png')
    image_login.size_hint = .4, .4
    image_login.pos_hint = {'center_x': .5, 'center_y': .79}

    text_name = TextLabel(text='Name:')
    text_name.size_hint = .8, .07
    text_name.pos_hint = {'x': .1, 'y': .64}

    name_input = TextInput()
    name_input.font_size = 24
    name_input.size_hint = .8, .07
    name_input.pos_hint = {'x': .1, 'y': .56}

    text_username = TextLabel(text='Username:')
    text_username.size_hint = .8, .07
    text_username.pos_hint = {'x': .1, 'y': .52}

    username_input = TextInput()
    username_input.font_size = 24
    username_input.size_hint = .8, .07
    username_input.pos_hint = {'x': .1, 'y': .44}

    text_password = TextLabel(text='Password:')
    text_password.size_hint = .8, .07
    text_password.pos_hint = {'x': .1, 'y': .4}

    password_input = TextInput()
    password_input.password = True
    password_input.font_size = 24
    password_input.size_hint = .8, .07
    password_input.pos_hint = {'x': .1, 'y': .32}  

    text_confirm_password = TextLabel(text='Confirm Password:')
    text_confirm_password.size_hint = .8, .07
    text_confirm_password.pos_hint = {'x': .1, 'y': .28}

    confirm_password_input = TextInput()
    confirm_password_input.password = True
    confirm_password_input.font_size = 24
    confirm_password_input.size_hint = .8, .07
    confirm_password_input.pos_hint = {'x': .1, 'y': .20}

    confirm_register_button = Tbutton(text='Sign Up')
    confirm_register_button.font_size = 20
    confirm_register_button.background_color = [.1, .1, .1, 1]
    confirm_register_button.size_hint = .8, .08
    confirm_register_button.pos_hint = {'x': .1, 'y': .09}  

    builder_list_ordering: list = [
        background, image_login,
        text_name, name_input,  
        text_username, username_input,
        text_password, password_input,
        text_confirm_password, confirm_password_input,
        confirm_register_button,
    ]

    def __init__(self, **kwargs):
        super(RegisterFrame, self).__init__(**kwargs)

        for wid in self.builder_list_ordering:
            self.add_widget(wid)






