from kivy.uix.label import Label

from kivy.properties import (
    ListProperty,
    StringProperty,
    BooleanProperty,
    OptionProperty,
)

from kivy.graphics import (
    Color,
    RoundedRectangle,
    )

class TextLabel(Label):
    def on_size(self, *args) -> None:
        self.text_size = self.size