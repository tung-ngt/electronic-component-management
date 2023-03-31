from ..gui import Button
from tkinter import PhotoImage
from tkinter.font import Font
from ..constants import COLORS, FONTS

class AccentButton(Button):
    """This is a custom button with accent color theme"""
    def __init__(self,
        master,
        command,
        text,
        width=None,
        height=None,
        image: PhotoImage or str = None,
        compound: str = None,
        activebackground = COLORS.WHITE,
        activeforeground = COLORS.ACCENT,
        hover_background: str = None,
        hover_foreground: str = None
        ):
        """Init the button
        
        Parameters
        master : master widget
        command : command to run on press
        text : text of the button
        """
        super().__init__(master,
            command,
            text,
            width,
            height,
            COLORS.ACCENT,
            "white",
            activebackground,
            activeforeground,
            0,
            image,
            FONTS.get_font("paragraph", bold=True),
            compound,
            hover_background,
            hover_foreground
        )

    def pack(self, **kwargs):
        if "ipadx" not in kwargs.keys():
            kwargs["ipadx"] = 10    
        if "ipady" not in kwargs.keys():
            kwargs["ipady"] = 4
        super().pack(**kwargs)

    def grid(self, **kwargs):
        if "ipadx" not in kwargs.keys():
            kwargs["ipadx"] = 10    
        if "ipady" not in kwargs.keys():
            kwargs["ipady"] = 4
        super().grid(**kwargs)