from ...gui import SubScreen, Label, Frame
from tkinter import PhotoImage
from ...constants import COLORS, FONTS

class ComponentDetailedView(SubScreen):
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
        self.component_img = PhotoImage(file="./images/component_img.png")
        self.component_img_label = Label(self.action_frame, image=self.component_img)
        self.component_img_label.pack()

        # Info text
        self.part_number_box = Frame(self.info_frame, highlightbackground="black", highlightthickness=2)
        self.part_number_label = Label(self.part_number_box,
            text="PART NUMBER", 
            font=FONTS.get_font("paragraph"),
            background="transparent"
        )
        self.part_number_label.pack(anchor="w", padx=20, pady=(20, 0))

        self.part_number = Label(self.part_number_box,
            text=props[0], 
            font=FONTS.get_font("heading2", bold=True),
            background="transparent"
        )
        self.part_number.pack(anchor="w", padx=20, pady=(0, 16))

        self.inventory_date = Label(self.info_frame, 
            text=f"Inventory date\n{props[4]}",
            font=FONTS.get_font("paragraph", italic=True),
            justify="right"
        )

        self.price_label = Label(self.info_frame,
            text="Price",
            font=FONTS.get_font("paragraph")
        )
        self.price = Label(self.info_frame,
            text=props[1],
            font=FONTS.get_font("heading3", bold=True)
        )
        
        self.guarantee_label = Label(self.info_frame,
            text="No months guarenteed",
            font=FONTS.get_font("paragraph")
        )
        self.guarantee = Label(self.info_frame,
            text=props[2],
            font=FONTS.get_font("heading3", bold=True)
        )

        self.manufacturer_label = Label(self.info_frame,
            text="Manufacturer",
            font=FONTS.get_font("paragraph")
        )
        self.manufacturer = Label(self.info_frame,
            text=props[3],
            font=FONTS.get_font("heading3", bold=True)
        )

        self.subcategory_label = Label(self.info_frame,
            text="Subcategory",
            font=FONTS.get_font("paragraph")
        )
        self.subcategory = Label(self.info_frame,
            text=props[5],
            font=FONTS.get_font("heading3", bold=True)
        )

        self.stock_label = Label(self.info_frame,
            text="Stock",
            font=FONTS.get_font("paragraph")
        )
        self.stock = Label(self.info_frame,
            text=props[6],
            font=FONTS.get_font("heading3", bold=True)
        )

        # Placing box
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.part_number_box.grid(row=0, column=0, sticky="w", pady=(0,40))
        self.inventory_date.grid(row=0, column=1, sticky="e", pady=(0,40))

        self.price_label.grid(row=1, column=0, sticky="w", pady=(40,0))
        self.price.grid(row=2, column=0, sticky="w", pady=(0,20))
        self.stock_label.grid(row=1, column=1, sticky="w", pady=(40,0))
        self.stock.grid(row=2, column=1, sticky="w", pady=(0,20))
        self.subcategory_label.grid(row=3, column=0, sticky="w", pady=(20,0))
        self.subcategory.grid(row=4, column=0, sticky="w", pady=(0,20))
        self.guarantee_label.grid(row=3, column=1, sticky="w", pady=(20,0))
        self.guarantee.grid(row=4, column=1, sticky="w", pady=(0,20))
        self.manufacturer_label.grid(row=5, column=0, columnspan=2, sticky="w", pady=(20,0))
        self.manufacturer.grid(row=6, column=0, columnspan=2, sticky="w", pady=(0,20))
        
        # Specify the widgets to destroy
        self.add_widgets_to_destroy([self.info_frame, self.action_frame])

