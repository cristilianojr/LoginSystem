# Standart Imports
import sys
from typing import NoReturn
from kivy.app import App
from views.managerpages import ManagerApp
from controllers.register_manage import register_user
from views.templates import *


class MainApp(App):
    def build(self) -> object:
        self.manager = ManagerApp(
            pages={
                'login': LoginPage(),
                'register': RegisterPage(),
            }
        )

        def current_page(page) -> None:
            self.manager.current_page = self.manager.pages[page]

        self.manager.pages['login'].ids['register_button'].released_function = current_page
        self.manager.pages['login'].ids['register_button'].released_args = ['register']
        
        self.manager.pages['register'].ids['back_button'].released_function = current_page
        self.manager.pages['register'].ids['back_button'].released_args = ['login']

        self.manager.pages['register'].ids['register_button'].released_function = register_user
        self.manager.pages['register'].ids['register_button'].released_args = [
            self.manager.pages['register'].ids['name_input'],
            self.manager.pages['register'].ids['username_input'],
            self.manager.pages['register'].ids['password_input'],
        ]
        # Set initial page
        self.manager.current_page = self.manager.pages['login']

        return self.manager

if __name__ == '__main__':
    APP = MainApp()
    APP.run()
    sys.exit(APP)
