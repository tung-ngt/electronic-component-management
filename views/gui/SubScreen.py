from .Frame import Frame
from tkinter import Widget

class SubScreen(Frame):
    """Represents a subscreen of a screen that can be navigated to"""
    def __init__(self, 
            master,
            background="white", 
            render_function=None, 
            title: str = None,
            title_bar_foreground: str=None,
            title_image = None
        ):
        super().__init__(master, background=background)
        self.render_function = render_function
        self.title  = title
        self.title_bar_foreground = title_bar_foreground
        self.title_image = title_image
        self.widgets_to_destroy: list[Widget] = []

    def clear_render(self):
        for widget in self.widgets_to_destroy:
            widget.destroy()

    def render(self, props=None):
        self.clear_render()
        if self.render_function != None:
            self.render_function(self, props)