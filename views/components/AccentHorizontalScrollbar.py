from tkinter.ttk import Scrollbar, Style
from ..constants import COLORS

class AccentHorizontalScrollbar(Scrollbar):
    """This is a custom scrollbar with accent color"""
    def __init__(self, master):
        """Init the scrollbar
        
        Parameters
        ----------
        master : master wiget
        """
        s = Style(master)
        s.theme_use("alt")
        s.configure("accent.Vertical.TScrollbar", troughcolor=COLORS.WHITE, background=COLORS.ACCENT, arrowcolor="white", relief="flat")
        s.map("accent.Vertical.TScrollbar", background=[("active", COLORS.ACCENT)])
        super().__init__(master,orient="vertical", style="accent.Vertical.TScrollbar")

    def add_command(self, command):
        """Add scroll command to scrollbar
        
        Parameters
        ----------
        command : scroll command
        """
        super().config(command=command)