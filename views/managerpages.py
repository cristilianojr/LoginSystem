from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import (
    ObjectProperty,
    DictProperty, 
    )

class ManagerApp(FloatLayout):

    current_page: object = ObjectProperty(Widget())

    pages: list = DictProperty({})

    def __init__(self, pages: list = None, **kwargs):
        super(ManagerApp, self).__init__(**kwargs)

        # Binding Properties
        self.bind(
            current_page = self._change_page,
            pages = self._change_page,
        )

        self.pages = pages if pages != None else self.pages

    def _change_page(self, *args) -> None:
        # Delete all childrren in self
        for child in self.children:
            self.remove_widget(child)

        # Add current page in variable
        self.add_widget(self.current_page)

