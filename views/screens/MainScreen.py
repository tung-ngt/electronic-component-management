from gui import Screen, Label
from constants import COLORS, FONTS

class MainScreen(Screen):
    """App's main screen"""
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, background=COLORS.WHITE)

        self.label = Label(self, text="Hello guys", background="transparent",font=FONTS.get_font("heading1"))
        self.label.pack()
