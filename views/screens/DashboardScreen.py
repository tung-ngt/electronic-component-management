from ..gui import Screen, Label, Frame, SubScreen
from ..constants import COLORS, FONTS

class DashboardScreen(Screen):
    """App's main screen"""
    def __init__(self, master, app_controller):
        """Init screen"""
        self.app_controller = app_controller
        super().__init__(master,
            background=COLORS.WHITE,
            title="Dashboard",
            title_font=FONTS.get_font("heading1", bold=True)
        )

        self.add_subscreen("dashboard_main", SubScreen(self.main_frame, background=COLORS.WHITE, render_function=self.render_dashboard))
        self.navigate_subscreen("dashboard_main")

    def render_dashboard(self, subscreen, props = None):
        subscreen.content = Frame(subscreen, background="transparent")
        subscreen.content.pack(anchor="center", fill="both", expand=True)

        subscreen.content.grid_rowconfigure(0, weight=1)
        subscreen.content.grid_rowconfigure(1, weight=1)
        subscreen.content.grid_columnconfigure(1, weight=1)
        subscreen.content.grid_columnconfigure(0, weight=1)
        subscreen.content.grid_columnconfigure(2, weight=1)

        subscreen.box1 = Frame(subscreen.content, background=COLORS.BACKGROUND_LIGHT)
        subscreen.box2 = Frame(subscreen.content, background=COLORS.SECONDARY)
        subscreen.box3 = Frame(subscreen.content, background="#ffffff")
        subscreen.box4 = Frame(subscreen.content, background=COLORS.BACKGROUND_LIGHT)

        subscreen.box1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)
        subscreen.box2.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=20, pady=20)
        subscreen.box3.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        subscreen.box4.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        
        subscreen.box3.pack_propagate(False)
        subscreen.box3.items_count_label = Label(
            subscreen.box3,
            f"{self.app_controller.get_no_of_components()} items in inventory",
            background="transparent",
            font=FONTS.get_font("heading3")
        )
        subscreen.box3.items_count_label.pack(fill="both", expand=True)
        
        subscreen.box4.pack_propagate(False)
        subscreen.box4.manufacturer_count_label = Label(
            subscreen.box4,
            f"{len(self.app_controller.get_manufacturers())} manufacturers",
            background="transparent",
            foreground=COLORS.PRIMARY,
            font=FONTS.get_font("heading3", bold=True)
        )
        subscreen.box4.manufacturer_count_label.pack(fill="both", expand=True)
