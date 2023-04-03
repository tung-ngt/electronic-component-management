from .gui import GUI
from .constants import COLORS, FONTS
from .screens import DashboardScreen, ComponentScreen, ManufacturerScreen, CustomerScreen, OrderScreen
from .components import Navbar

class EComponentStoreManagementGUI(GUI):
    """Electronic Componnet Store Infomation Mangament GUI APP"""
    def __init__(self, app_controller):
        super().__init__(
            "Electronic Component Store Infomation Mangament", 
            fullscreen=True, 
            icon="./images/circuit-board.png",
            min_size=(1400, 900),
            on_close_fun=self.on_close
        )
        
        self.app_controller = app_controller

        # Init fonts
        FONTS.init_fonts(self)

        # Initialze navbar and specify links
        self.init_navbar(Navbar(self,
            [
                ("dashboard","Dashboard"),
                ("components", "Components"),
                ("manufacturers", "Manufacturers"),
                ("customers", "Customers"),
                # ("orders", "Orders"),
            ],
            self.change_screen,
            logo={
                "logo_path": "./images/circuit-board.png",
                "name": "ECSIM",
                "font": FONTS.get_font("heading1", bold=True),
                "color": COLORS.WHITE
            }
        ))

        self.add_screen("dashboard", DashboardScreen(self.screens_frame, self.app_controller))
        self.add_screen("components", ComponentScreen(self.screens_frame, self.app_controller))
        self.add_screen("manufacturers", ManufacturerScreen(self.screens_frame, self.app_controller))
        self.add_screen("customers", CustomerScreen(self.screens_frame, self.app_controller))
        # self.add_screen("orders", OrderScreen(self.screens_frame, self.app_controller))

        self.show_screen("dashboard")

    def on_close(self):
        print("Closed")
        print("Thank you for using the system")
        self.destroy()

if __name__ == "__main__":
    app = EComponentStoreManagementGUI()
    app.mainloop()