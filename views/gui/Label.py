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
            image: str=None,
        ):
        """Init the label
        
        Parameters
        ----------
        master : master widget,
        text : str text
        foreground : text color (default black)
        background : background color (default white) specify transparent for transparent 
        font : a tk font (default None)
        image : label image path (default None)
        """
        # Check if the backgroud is transparent
        background = master.background if background == "transparent" else background
        if image != None:
            self.label_image = PhotoImage(file=image)
            super().__init__(
                master,
                image=self.label_image,
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