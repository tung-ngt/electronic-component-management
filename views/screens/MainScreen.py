from gui import Screen, Label, Frame
from constants import COLORS, FONTS

class MainScreen(Screen):
    """App's main screen"""
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, background=COLORS.WHITE)

        self.label = Label(self,
            text="Dashboard",
            background="transparent",
            foreground="#000000",
            font=FONTS.get_font("heading1", bold=True)
        )
        self.label.pack(pady=(100,0))

        self.main_frame = Frame(self, background="transparent")
        self.main_frame.pack(anchor="center", fill="both", expand=True)

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)

        self.box1 = Frame(self.main_frame, background=COLORS.BACKGROUND_LIGHT)
        self.box2 = Frame(self.main_frame, background=COLORS.SECONDARY)
        self.box3 = Frame(self.main_frame, background="#ffffff")
        self.box4 = Frame(self.main_frame, background=COLORS.BACKGROUND_LIGHT)

        self.box1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)
        self.box2.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=20, pady=20)
        self.box3.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.box4.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        
        self.box3.pack_propagate(False)
        self.items_count_label = Label(self.box3, "1200 items in inventory", background="transparent", font="heading2")
        self.items_count_label.pack(fill="both", expand=True)
