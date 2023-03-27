from gui import Screen, Label
from constants import COLORS

class ComponentScreen(Screen):
    """Component screen
    
    Display information about the electric components
    """
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, background=COLORS.BACKGROUND_LIGHT)

        self.label = Label(self,
            text="Component Screen",
            background="transparent",
            foreground="#000000"
        )
        self.label.pack()
