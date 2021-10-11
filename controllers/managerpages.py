
def change_widget(parent_widget, new_widget) -> None:
    # Remove all current children
    for child in parent_widget.children:
        parent_widget.remove_widget(child)
    # Add the new widget
    parent_widget.add_widget(new_widget)

def apply_color_template() -> None: ...
