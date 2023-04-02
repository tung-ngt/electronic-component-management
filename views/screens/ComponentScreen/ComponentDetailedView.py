from tkinter import PhotoImage
from ...gui import SubScreen, Label, Frame
from ...constants import FONTS
from ...components import AccentButton
from . AddComponentWindow import AddComponentWindow
from .UpdateComponentWindow import UpdateComponentWindow

class ComponentDetailedView(SubScreen):
    """This class display details of a specific component"""
    def __init__(self, master, app_controller):
        """Init the component detailed view
        
        Parameters
        ----------
        master : master widget
        app_controller : the app controller
        """
        self.app_controller = app_controller
        super().__init__(master, background="white")
        self.get_all_manufacturers_ids()

    def get_all_manufacturers_ids(self):
        manufacturers = self.app_controller.get_manufacturers()
        self.manufacturers_ids = {}
        for manufacturer in manufacturers:
            self.manufacturers_ids[manufacturer.get_id()] = manufacturer.get_name()


    # Overriding render method
    def render(self, props=None):
        self.component_type = props["component_type"]
        values = props["values"]
        super().render()
        self.title = "Component Information"

        # Create layout frame
        self.info_frame = Frame(self)
        self.image_frame = Frame(self)
        self.info_frame.pack(side="left", fill="both", padx=20, pady=(50,50), expand=True)
        self.image_frame.pack(side="left", fill="both", pady=100, expand=True)

        # Image frame
        self.component_img = PhotoImage(file="./images/component_img.png")
        self.component_img_label = Label(self.image_frame, image=self.component_img)
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
            text=values[0], 
            font=FONTS.get_font("heading2", bold=True),
            background="transparent"
        )
        self.part_number.pack(anchor="w", padx=20, pady=(0, 16))

        self.inventory_date = self.create_info_box("Inventory date", values[4], True)
        self.price = self.create_info_box("Price", values[1])
        self.guarantee = self.create_info_box("No months guarenteed", values[2],)
        self.manufacturer = self.create_info_box("Manufacturer", values[3],)
        self.subcategory = self.create_info_box("Subcategory", values[5],)
        self.stock = self.create_info_box("Stock", values[6],)

        if self.component_type == "ic":
            self.optional_info = self.create_info_box("Clock", values[7])
        if self.component_type == "capacitor":
            self.optional_info = self.create_info_box("Capacitance", values[7])
        if self.component_type == "inductor":
            self.optional_info = self.create_info_box("Inductance", values[7])
        if self.component_type == "resistor":
            self.optional_info = self.create_info_box("Resistance", values[7])
        if self.component_type == "sensor":
            self.optional_info = self.create_info_box("Sensor type", values[7])

        self.update_info_button = AccentButton(
            self.info_frame, 
            command=lambda: UpdateComponentWindow(self,
                self.component_type,
                self.app_controller,
                values,
                on_close_fun=self.render,
            ),
            text="Update information",
        )

        # Placing box
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_rowconfigure(4, weight=1)

        self.part_number_box.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,40))

        self.price.grid(row=1, column=0, sticky="w")
        self.stock.grid(row=1, column=1, sticky="w")
        self.optional_info.grid(row=2, column=0, sticky="w")
        self.guarantee.grid(row=2, column=1, sticky="w")
        self.subcategory.grid(row=3, column=0, sticky="w")
        self.manufacturer.grid(row=3, column=1, sticky="w")
        self.inventory_date.grid(row=4, column=0, sticky="sw")
        self.update_info_button.grid(row=4, column=1, pady=10,sticky="sw")

        
        # Specify the widgets to destroy
        self.add_widgets_to_destroy([self.info_frame, self.image_frame])

    def create_info_box(self, label:str, value:str, small=False):
        """Create and return a info_box
        
        Parameters
        ----------
        label : name of the info box
        value : value of the box
        small : small info box
        """
        frame = Frame(self.info_frame, background="transparent")
        l = Label(frame, text=label, font=FONTS.get_font("paragraph", italic=small))
        i = Label(frame, text=value, font=FONTS.get_font("heading3" if not small else "paragraph", bold=True))
        l.pack(anchor="w", pady=(40,0))
        i.pack(anchor="w")

        return frame