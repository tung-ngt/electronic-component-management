from ...gui import SubScreen, Label, Frame, Button
from ...constants import FONTS, COLORS
from .UpdateCustomerWindow import UpdateCustomerWindow
from ...components import AccentButton
from PIL import Image, ImageTk

class CustomerDetailedView(SubScreen):
    """This class display details of a specific component"""
    def __init__(self, master, app_controller):
        self.app_controller = app_controller
        super().__init__(master, background="white")

    # Overriding render method
    def render(self, props=None):
        super().render()
        self.title = "Customers"

        # Create layout frame
        self.info_frame = Frame(self)
        self.info_frame.pack(fill="both", padx=20, pady=100, expand=True)
        # Info text
        self.man_id_box = Frame(self.info_frame, highlightbackground="black", highlightthickness=2)
        self.man_id_label = Label(self.man_id_box,
            text="CUSTOMER'S ID", 
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

        self.man_name = self.create_info_box("Name", props[1])
        
        self.man_country = self.create_info_box("Phone number", props[2])

        self.update_info_button = AccentButton(
            self.info_frame, 
            command=lambda: UpdateCustomerWindow(self,
                self.app_controller,
                props,
                self.render
            ),
            text="Update information",
        )

        # Placing box
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)

        self.man_id_box.grid(row=0, column=0, sticky="w", pady=(0,40))

        self.man_name.grid(row=1, column=0, sticky="w")
        self.man_country.grid(row=2, column=0, sticky="w")
        self.update_info_button.grid(row=3, column=0, sticky="w", pady=(40,0))
        
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
