from tkinter import Button as tkButton, PhotoImage
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
            image: PhotoImage or str=None,
            font: Font=None,
            compound: str=None
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
        image : label image path (default None)
        font : a tk font type default None
        compound : image and text relative position default None
        """
        # Check if the backgroud is transparent
        if background == "transparent":
            background = master.background
        
        # Check if the label have image
        self.label_image: PhotoImage = None
        if image != None:
            if isinstance(image, str):
                self.label_image = PhotoImage(file=image)
            else:
                self.label_image = image

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
            cursor="hand2",
            image=self.label_image,
            compound=compound
        )