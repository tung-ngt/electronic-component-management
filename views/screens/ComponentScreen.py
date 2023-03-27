from gui import Screen, Label
from constants import COLORS

class ComponentScreen(Screen):
    """Component screen
    
    Display information about the electric components
    """
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, background=COLORS.DARK_CYAN)

        self.label = Label(self,
            text="Component Screen",
            background=COLORS.DARK_CYAN,
            foreground=COLORS.WHITE
        )
        self.label.pack()
