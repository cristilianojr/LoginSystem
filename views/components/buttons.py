from types import FunctionType
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window

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

class ButtonBase(ButtonBehavior):
    # Basic Properties
    id: str = StringProperty(None)
    radius: list =  ListProperty([10, 10, 10, 10])
    
    # Regarding the filling of the background
    background_activety: bool = BooleanProperty(True)
    background_color: list = ListProperty([.15, .15, .15, 1])

    # Regarding the filling of the foreground
    foreground_activety: bool = BooleanProperty(True)
    foreground_color: list = ListProperty([1, 1, 1, .5])

    # Regarding canvas.after filling when the mouse is over the widget
    hover_activety: bool = BooleanProperty(True)
    hover_color: list = ListProperty([1, 1, 1, .2])
    
    # Regarding the click and release of the button 
    pressed_function: FunctionType = None
    pressed_args: list = []
    pressed_kwargs: dict = {}
    released_function: FunctionType = None
    released_args: list = []
    released_kwargs: dict = {}

    def __init__(self, id: str = None, radius: list = None, background_activety: bool = None, background_color: list = None, \
        foreground_activety: bool = None, foreground_color: list = None, hover_activety: bool = None, hover_color: list = None, \
        pressed_function: FunctionType = None, pressed_args: list = None, pressed_kwargs: dict = None, released_function: FunctionType = None, \
        released_args: list = None, released_kwargs: dict = None, **kwargs):

        # Running an __init__ function of the parent class
        super(ButtonBase, self).__init__(**kwargs)
        
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
            radius = self._do_background,
            background_activety = self._do_background,
            background_color = self._do_background,
        )
        # Foreground
        self.bind(
            on_press = self._do_foreground,
            on_touch_move = self._do_foreground,
            on_touch_up = self._undo_foreground,

        )
        self.bind(
            on_press = self._build_pressed_function,
            on_touch_up = self._build_released_function,
        )

        # Mouse movement
        Window.bind(mouse_pos = self._do_hover)

        # Pre-setting the values ​​entered in the class call
        self.id: str = id if id != None else self.id
        self.radius: list = radius if radius != None else self.radius
        self.background_activety: bool = background_activety if background_activety != None else self.background_activety
        self.background_color: list = background_color if background_color != None else self.background_color
        self.foreground_activety: bool = foreground_activety if foreground_activety != None else self.foreground_activety
        self.foreground_color: list = foreground_color if foreground_color != None else self.foreground_color
        self.hover_activety: bool = hover_activety if hover_activety != None else self.hover_activety
        self.hover_color: list = hover_color if hover_color != None else self.hover_color
        self.pressed_function: FunctionType = pressed_function if pressed_function != None else self.pressed_function
        self.pressed_args: list = pressed_args if pressed_args != None else self.pressed_args
        self.pressed_kwargs: dict = pressed_kwargs if pressed_kwargs != None else self.pressed_kwargs
        self.released_function: FunctionType = released_function if released_function != None else self.released_function
        self.released_args: list = released_args if released_args != None else self.released_args
        self.released_kwargs: dict = released_kwargs if released_kwargs != None else self.released_kwargs

    def _do_background(self, *args) -> None: 
        # Reset canvas before
        self.canvas.before.clear()
        # Draw background
        if self.background_activety == True:
            with self.canvas.before:
                Color(*self.background_color)
                RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)

    def _do_foreground(self, *args) -> None: 
        # Reset canvas after
        self.canvas.after.clear()

        # Draw foreground
        if self.foreground_activety == True and self.collide_point(*Window.mouse_pos):
            with self.canvas.after:
                Color(*self.foreground_color)
                RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)

    def _undo_foreground(self, *args) -> None:
        # Reset foreground 
        self.canvas.after.clear()

    def _do_hover(self, *args) -> None: 
        if self.hover_activety == True and self.collide_point(*Window.mouse_pos) and self.state == 'normal':
            # reset canvas.after
            self.canvas.after.clear()
            # Draw Hover Effect
            with self.canvas.after:
                Color(*self.hover_color)
                RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
        else:
            # reset canvas.after
            self.canvas.after.clear()

    def _build_pressed_function(self, *args) -> None: 
        if self.pressed_function != None:
            self.pressed_function(*self.pressed_args, **self.pressed_kwargs)

    def _build_released_function(self, *args) -> None:
        if self.released_function != None and self.collide_point(*Window.mouse_pos) and self.state == 'down':
            self.released_function(*self.released_args, **self.released_kwargs)

class Ibutton(ButtonBase, Image): pass
class Tbutton(ButtonBase, Label): pass
