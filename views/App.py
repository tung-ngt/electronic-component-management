from gui import GUI
from constants import COLORS, FONTS
from screens import MainScreen, ComponentScreen
from components import Navbar

class EComponentStoreManagementGUI(GUI):
    """Electronic Componnet Store Infomation Mangament GUI APP"""
    def __init__(self):
        super().__init__(
            "Electronic Component Store Infomation Mangament", 
            fullscreen=True, 
            icon="./images/circuit-board.png",
            on_close_fun=self.on_close
        )
        
        # Init fonts
        FONTS.init_fonts(self)

        # Initialze navbar and specify links
        self.init_navbar(Navbar(self,
            [
                ("main","Home"),
                ("components", "Components")
            ],
            self.change_screen,
            logo={
                "logo_path": "./images/circuit-board.png",
                "name": "ECSIM",
                "font": FONTS.get_font("heading1", bold=True),
                "color": COLORS.WHITE
            }
        ))

        self.add_screen("main", MainScreen(self))
        self.add_screen("components", ComponentScreen(self))

        self.show_screen("main")

    def on_close(self):
        print("Closed")
        print("Thank you for using the system")
        self.destroy()

if __name__ == "__main__":
    app = EComponentStoreManagementGUI()
    app.mainloop()