from tkinter import Label as tkLabel, PhotoImage
from tkinter.font import Font

class Label(tkLabel):
    """Custom Label"""
    def __init__(self,
            master,
            text: str="",
            foreground="black",
            background="white",
            font: Font=None,
            image: PhotoImage=None,
        ):
        """Init the label
        
        Parameters
        ----------
        master : master widget,
        text : str text
        foreground : text color (default black)
        background : background color (default white) specify transparent for transparent 
        font : a tk font (default None)
        image : label image (default None)
        """
        # Check if the backgroud is transparent
        background = master.background if background == "transparent" else background

        if image != None:
            super().__init__(
                master,
                image=image,
                background=background,
            )
        else:
            super().__init__(
                master,
                text=text,
                background=background,
                foreground=foreground,
                font=font
            )