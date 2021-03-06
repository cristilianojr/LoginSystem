from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (
    ListProperty, BooleanProperty,
    NumericProperty,
    )
from kivy.graphics import (
    Color, RoundedRectangle,
    Line,
    )

class Frame(FloatLayout): 
    # Basic Properties
    radius: list = ListProperty([0, 0, 0, 0])
    # Background Properties
    background: bool = BooleanProperty(False)
    background_color: list = ListProperty([.15, .15, .15, 1])
    # Border Properties
    border: bool = BooleanProperty(False)
    border_width: int = NumericProperty(2)
    border_color: list = ListProperty([1, 1, 1, 1])

    def __init__(self, radius: list = None, background: bool = None, background_color: list  = None, \
        border: bool = None, border_width: int = None, border_color: list = None, \
        **kwargs) -> None:
        # Call master init function
        super(Frame, self).__init__(**kwargs)

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
            border = self._do_background,
            border_color = self._do_background,
            border_width = self._do_background,
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
