from views.components.frame import Frame

# Build KVLang
from kivy.lang import Builder
Builder.load_file(r'views\templates\loginpage.kv')
Builder.load_file(r'views\templates\registerpage.kv')
Builder.load_file(r'views\templates\recoverpassword.kv')


class LoginPage(Frame):
    pass

class RegisterPage(Frame):
    pass

class RecoverPage(Frame):
    pass
