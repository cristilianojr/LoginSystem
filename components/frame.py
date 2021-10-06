from kivy.uix.image import Image
from kivy.properties import (
    ListProperty, NumericProperty,
)
from kivy.graphics import (
    Color, Line,
)

class Iframe(Image):
    # Basic 
    radius: list = ListProperty([50, 50, 50, 50])

    # Border 
    border_color: list = ListProperty([1, 1, 1, 1])
    border_width: int = NumericProperty(5)

    def __init__(self, **kwargs):
        super(Iframe, self).__init__(**kwargs)

        # Binding all properties in the specific function
        # Background
        self.bind(
            pos = self._do_border,
            x = self._do_border,
            y = self._do_border,
            size = self._do_border,
            width = self._do_border,
            height = self._do_border,
            size_hint = self._do_border,
            radius = self._do_border,
            border_color = self._do_border,
            border_width = self._do_border,
        )

    def _do_border(self, *args) -> None: 
        # Reset canvas before
        self.canvas.after.clear()
        # Draw background
        with self.canvas.after:
            Color(*self.border_color)
            Line(rounded_rectangle=[self.x, self.y, self.width, self.height, *self.radius], width=self.border_width)

    
   

