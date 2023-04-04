from ...gui import SubScreen, Label, Frame, Button
from ...constants import FONTS, COLORS
from ...components import AccentButton
from .UpdateOrderWindow import UpdateOrderWindow
from PIL import Image, ImageTk

class OrderDetailedView(SubScreen):
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
        super().render()
        self.title = "Order's information"

        # Create layout frame
        self.info_frame = Frame(self)
        self.info_frame.pack(side="left", fill="both", padx=20, pady=(50,50), expand=True)

        # Info text
        self.order_id_box = Frame(self.info_frame, highlightbackground="black", highlightthickness=2)
        self.order_id_label = Label(self.order_id_box,
            text="PART NUMBER", 
            font=FONTS.get_font("paragraph"),
            background="transparent"
        )
        self.order_id_label.pack(anchor="w", padx=20, pady=(20, 0))

        self.order_id = Label(self.order_id_box,
            text=props[0], 
            font=FONTS.get_font("heading2", bold=True),
            background="transparent"
        )
        self.order_id.pack(anchor="w", padx=20, pady=(0, 16))

        self.customer = self.create_info_box("Customer", props[1], True)
        self.date = self.create_info_box("Purchase date", props[3], True)
        self.price = self.create_info_box("total price", props[4])
        
        self.update_info_button = AccentButton(
            self.info_frame, 
            command=lambda: UpdateOrderWindow(self,
                self.component_type,
                self.app_controller,
                props,
                on_close_fun=self.render,
            ),
            text="Update information",
        )

        # Placing box
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_rowconfigure(4, weight=1)

        self.order_id_box.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,40))

        self.customer.grid(row=1, column=0, sticky="w")
        self.price.grid(row=1, column=1, sticky="w")
        self.date.grid(row=4, column=0, sticky="sw")
        self.update_info_button.grid(row=4, column=1, pady=10,sticky="sw")

        
        # Specify the widgets to destroy
        self.add_widgets_to_destroy([self.info_frame])

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