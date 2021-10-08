from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.graphics import Color, RoundedRectangle

class Frame(FloatLayout): ...

class Background(Frame):
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
