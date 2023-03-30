from ...gui import SubScreen, Label, Frame
from tkinter import PhotoImage
from ...constants import COLORS, FONTS

class ManufacturerDetailedView(SubScreen):
    """This class display details of a specific component"""
    def __init__(self, master):
        super().__init__(master, background="white")

    # Overriding render method
    def render(self, props=None):
        super().render()
        self.title = "Component Information"

        # Create layout frame
        self.info_frame = Frame(self)
        self.action_frame = Frame(self)
        self.info_frame.pack(side="left", fill="both", padx=20, pady=100, expand=True)
        self.action_frame.pack(side="left", fill="both", pady=100, expand=True)

        # Action part
        self.man_img = PhotoImage(file="./images/component_img.png")
        self.man_img_label = Label(self.action_frame, image=self.man_img)
        self.man_img_label.pack()

        # Info text
        self.man_id_box = Frame(self.info_frame, highlightbackground="black", highlightthickness=2)
        self.man_id_label = Label(self.man_id_box,
            text="MANUFACTURER ID", 
            font=FONTS.get_font("paragraph"),
            background="transparent"
        )
        self.man_id_label.pack(anchor="w", padx=20, pady=(20, 0))

        self.man_id = Label(self.man_id_box,
            text=props[0], 
            font=FONTS.get_font("heading2", bold=True),
            background="transparent"
        )
        self.man_id.pack(anchor="w", padx=20, pady=(0, 16))

        self.man_name_label = Label(self.info_frame,
            text="Name",
            font=FONTS.get_font("paragraph")
        )
        self.name = Label(self.info_frame,
            text=props[1],
            font=FONTS.get_font("heading3", bold=True)
        )
        
        self.country_label = Label(self.info_frame,
            text="Country",
            font=FONTS.get_font("paragraph")
        )
        self.country = Label(self.info_frame,
            text=props[2],
            font=FONTS.get_font("heading3", bold=True)
        )

        # Placing box
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)

        self.man_id_box.grid(row=0, column=0, sticky="w", pady=(0,40))

        self.man_name_label.grid(row=1, column=0, sticky="w", pady=(40,0))
        self.name.grid(row=2, column=0, sticky="w", pady=(0,20))
        self.country_label.grid(row=3, column=0, sticky="w", pady=(20,0))
        self.country.grid(row=4, column=0, sticky="w", pady=(0,20))
        
        # Specify the widgets to destroy
        self.add_widgets_to_destroy([self.info_frame, self.action_frame])

