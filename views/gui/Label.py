from tkinter import Label as tkLabel
from tkinter.font import Font
from .Typography import Typography
class Label(tkLabel):
    """Custom Label"""
    def __init__(self,
            master,
            text: str,
            foreground="black",
            background="white",
            font: Font = Typography.get_font("paragraph")
        ):
        """Init the label
        
        Parameters
        ----------
        master : master widget,
        text : str text
        foreground : text color (default black)
        background : background color (default white)
        font : a tk font (default Typography paragraph)
        """
        super().__init__(
            master,
            text=text,
            background=background,
            foreground=foreground,
            font=font
        )