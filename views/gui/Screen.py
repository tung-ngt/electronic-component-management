import tkinter as tk
from .Navbar import Navbar
from .Frame import Frame

class Screen(Frame):
    """Represent a screen in the gui"""
    def __init__(self, master, background="#ffffff"):
        """Init the screen
        
        Parameters
        ----------
        master : master widget
        background : background color
        """
        super().__init__(master, background=background)
        self.background = background
        # Make the screen take up the whole available space
        # instead of skrinking to children widgets
        self.grid_propagate(False)
        self.pack_propagate(False)    