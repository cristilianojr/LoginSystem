from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.properties import (
    ListProperty,
    BooleanProperty,
    NumericProperty,
)
from kivy.graphics import (
    Color, RoundedRectangle,
    Line,
    )

class TextLabel(ButtonBehavior, Label):
    # Basic Properties
    radius: list = ListProperty([0, 0, 0, 0])
    # Background Properties
    background: bool = BooleanProperty(False)
    background_color: list = ListProperty([.15, .15, .15, 1])
    # Border Properties
    border: bool = BooleanProperty(False)
    border_width: int = NumericProperty(2)
    border_color: list = ListProperty([1, 1, 1, 1])
    # hover properties
    hover: bool = BooleanProperty(False)
    hover_color: list = ListProperty([.5, .5, 1, 1]) 
    # press color properties
    press_activation: bool = BooleanProperty(False)
    press_color: list = ListProperty([.3, .3, 1, 1])
    reset_color: list = ListProperty([1, 1, 1, 1])

    def __init__(self, radius: list = None, background: bool = None, background_color: list  = None, \
        border: bool = None, border_width: int = None, border_color: list = None, \
        **kwargs) -> None:
        # Call master init function
        super(TextLabel, self).__init__(**kwargs)

        # Binding properties
        self.bind( # Draw the background!
            pos = self._do_background,
            x = self._do_background,
            y = self._do_background,
            size = self._do_background,
            width = self._do_background,
            height = self._do_background,
            size_hint = self._do_background,
            radius = self._do_background,
            background = self._do_background,
            background_color = self._do_background,
        )

        self.bind( # Draw the border!
            pos = self._do_border,
            x = self._do_border,
            y = self._do_border,
            size = self._do_border,
            width = self._do_border,
            height = self._do_border,
            size_hint = self._do_border,
            radius = self._do_border,
            border = self._do_border,
            border_color = self._do_border,
            border_width = self._do_border,
        )

        self.bind( # Change text color 
            on_press = self._do_press_color,
            on_touch_up = self._do_release_color,
            on_touch_move = self._do_press_color,
        )

        Window.bind(
            mouse_pos = self._do_hover,
        )

        self.radius = radius if radius != None else self.radius
        self.background = background if background != None else self.background
        self.background_color = background_color if background_color != None else self.background_color
        self.border = border if border != None else self.border
        self.border_width = border_width if border_width != None else self.border_width
        self.border_color = border_color if border_color != None else self.border_color

    def _do_background(self, *args) -> None:
        # Clear before canvas
        self.canvas.before.clear()
        # Draw a new background into canvas before
        if self.background == True:
            with self.canvas.before:
                Color(*self.background_color)
                RoundedRectangle(
                    pos = self.pos,
                    size = self.size,
                    radius = self.radius)

    def _do_border(self, *args) -> None:
        # Clear after canvas
        self.canvas.after.clear()
        # Draw a new border into canvas after
        if self.border == True:
            with self.canvas.after:
                Color(*self.border_color)
                Line(
                    rounded_rectangle = (
                        self.x, self.y, 
                        self.width, self.height, 
                        *self.radius), 
                    width = self.border_width
                    )

    def on_size(self, *args) -> None:
        self.text_size = self.size

    def _do_press_color(self, *args) -> None:
        if self.press_activation == True and self.collide_point(*Window.mouse_pos):
            self.color = [*self.press_color]

    def _do_release_color(self, *args) -> None:
        if self.press_activation == True and self.collide_point(*Window.mouse_pos) and self.hover == True:
            self.color = [*self.hover_color]
        elif self.press_activation == True and self.collide_point(*Window.mouse_pos):
            self.color = [*self.reset_color]

    def _do_hover(self, *args) -> None:
        if self.hover == True and self.collide_point(*Window.mouse_pos) and self.state == 'normal':
            self.color = [*self.hover_color]
        else:
            self.color = [*self.reset_color]
