from tkinter import Button as tkButton
from tkinter.font import Font

class Button(tkButton):
    """Wrapper around tkButton"""
    def __init__(self, 
            master, 
            command,
            text,
            width=None, height=None,
            background="white", foreground="black",
            activebackground="grey", activeforeground="black",
            borderwidth=0, 
            font: Font=None, 
        ):
        """Init the button
        
        Parameters
        ----------
        master : master widget
        command : function to run when press
        width : int
        height : int
        background
        foreground
        activebackground
        activeforeground
        borderwidth : default 0
        font : a tk font type default None
        """
        super().__init__(
            master, 
            activebackground=activebackground, 
            activeforeground=activeforeground,
            background=background,
            foreground=foreground,
            borderwidth=borderwidth,
            command=command,
            font=font,
            text=text,
            width=width,
            height=height,
            cursor="hand2"
        )