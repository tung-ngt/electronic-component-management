from gui import GUI, Screen, Navbar
from constants import COLORS, FONTS
import tkinter as tk

class EComponentManagementGUI(GUI):
    def __init__(self):
        super().__init__(
            "Electronic Component Management", 
            fullscreen=True, 
            icon="./images/circuit-board.png",
            fonts=FONTS.FONTS
        )
        self.init_navbar(
            Navbar(self.root_window, COLORS.NEUTRAL_RED, [("main","Home"), ("info", "Info")], text_color=COLORS.WHITE,
                redirect_funtion=self.change_screen
            )
        )
        self.add_screen(
            "main",
            Screen(self.root_window, COLORS.DARK_CYAN)
        )
        self.add_screen(
            "info",
            Screen(self.root_window, COLORS.WHITE)
        )

        self.show_screen("main")

app = EComponentManagementGUI()
app.main_loop()