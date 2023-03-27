from gui import Screen, Label, Frame
from constants import COLORS, FONTS

class ComponentScreen(Screen):
    """Component screen
    
    Display information about the electric components
    """
    def __init__(self, master):
        """Init screen"""
        super().__init__(master)

        # Add screen title
        self.label = Label(self,
            text="Components",
            background="transparent",
            foreground="#000000",
            font=FONTS.get_font("heading1", bold=True)
        )
        self.label.pack(pady=(100,0))

        # Create component frame
        self.main_frame = Frame(self, background="transparent")
        self.main_frame.pack(anchor="center", fill="both", expand=True)

        # Configure grid
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)

        # Create frames
        self.box1 = Frame(self.main_frame, background=COLORS.WHITE)
        self.box2 = Frame(self.main_frame, background=COLORS.WHITE)
        self.box3 = Frame(self.main_frame, background=COLORS.WHITE)
        self.box4 = Frame(self.main_frame, background=COLORS.WHITE)
        self.box5 = Frame(self.main_frame, background=COLORS.WHITE)

        # Place frames
        self.box1.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.box4.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.box2.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=20, pady=20)
        self.box3.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.box5.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        
        # Make box take the full width and height
        self.box1.pack_propagate(False)
        self.box2.pack_propagate(False)
        self.box3.pack_propagate(False)
        self.box4.pack_propagate(False)
        self.box5.pack_propagate(False)

        # Add images
        self.capcitor_img = Label(self.box1, image="./images/capacitor.png", background="transparent")
        self.capcitor_img.pack(fill="both", expand=True, anchor="s")
        self.ic_img = Label(self.box2, image="./images/ic.png", background="transparent")
        self.ic_img.pack(fill="both", expand=True, anchor="s")
        self.inductor_img = Label(self.box3, image="./images/inductor.png", background="transparent")
        self.inductor_img.pack(fill="both", expand=True, anchor="s")
        self.resistor_img = Label(self.box4, image="./images/resistor.png", background="transparent")
        self.resistor_img.pack(fill="both", expand=True, anchor="s")
        self.sensor_img = Label(self.box5, image="./images/sensor.png", background="transparent")
        self.sensor_img.pack(fill="both", expand=True, anchor="s")

        # Add labels
        self.capcitor_label = Label(self.box1, text="Capacitor", background="transparent", font=FONTS.get_font("heading3", bold=True))
        self.capcitor_label.pack(fill="both", expand=True, anchor="n")
        self.ic_label = Label(self.box2, text="IC", background="transparent", font=FONTS.get_font("heading3", bold=True))
        self.ic_label.pack(fill="both", expand=True, anchor="n")
        self.inductor_label = Label(self.box3, text="Inductor", background="transparent", font=FONTS.get_font("heading3", bold=True))
        self.inductor_label.pack(fill="both", expand=True, anchor="n")
        self.resistor_label = Label(self.box4, text="Resistor", background="transparent", font=FONTS.get_font("heading3", bold=True))
        self.resistor_label.pack(fill="both", expand=True, anchor="n")
        self.sensor_label = Label(self.box5, text="Sensor", background="transparent", font=FONTS.get_font("heading3", bold=True))
        self.sensor_label.pack(fill="both", expand=True, anchor="n")

        # Bind click event
        self.capcitor_img.bind("<Button-1>", lambda event: print("capcitor"))
        self.ic_img.bind("<Button-1>", lambda event: print("ic"))
        self.inductor_img.bind("<Button-1>", lambda event: print("inductor"))
        self.resistor_img.bind("<Button-1>", lambda event: print("resistor"))
        self.sensor_img.bind("<Button-1>", lambda event: print("sensor"))
        self.capcitor_label.bind("<Button-1>", lambda event: print("capcitor"))
        self.ic_label.bind("<Button-1>", lambda event: print("ic"))
        self.inductor_label.bind("<Button-1>", lambda event: print("inductor"))
        self.resistor_label.bind("<Button-1>", lambda event: print("resistor"))
        self.sensor_label.bind("<Button-1>", lambda event: print("sensor"))