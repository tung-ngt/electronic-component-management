from ...gui import SubScreen, Label, Frame, Button
from ...constants import FONTS, COLORS
from ...components import AccentButton, CustomListView, AccentHorizontalScrollbar
from .UpdateOrderWindow import UpdateOrderWindow
from PIL import Image, ImageTk
import json
from math import floor

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
        self.title = "Order's information"



    # Overriding render method
    def render(self, props=None):
        super().render()
        values = props["values"]
        components_prices = props["components_prices"]

        # Create layout frame
        self.info_frame = Frame(self, background=COLORS.SECONDARY)
        self.items_frame = Frame(self, background=COLORS.WHITE)
        self.info_frame.pack(fill="x")
        self.items_frame.pack(fill="both", expand=True)

        # Info text
        self.order_id_box = Frame(self.info_frame, 
            background="transparent", 
            highlightbackground="white",
            highlightthickness=2
        )
        self.order_id_label = Label(self.order_id_box,
            text="PART NUMBER", 
            font=FONTS.get_font("paragraph"),
            foreground="white",
            background="transparent"
        )
        self.order_id_label.pack(anchor="w", padx=20, pady=(20, 0))

        self.order_id = Label(self.order_id_box,
            text=values[0], 
            font=FONTS.get_font("heading2", bold=True),
            foreground="white",
            background="transparent"
        )
        self.order_id.pack(anchor="w", padx=20, pady=(0, 16))

        self.customer = self.create_info_box("Customer", values[1], True)
        self.date = self.create_info_box("Purchase date", values[3], True)
        self.price = self.create_info_box("total price", values[4])
        
        # self.update_info_button = AccentButton(
        #     self.info_frame, 
        #     command=lambda: UpdateOrderWindow(self,
        #         self.component_type,
        #         self.app_controller,
        #         values,
        #         on_close_fun=self.render,
        #     ),
        #     text="Update information",
        # )

        # Placing box
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(1, weight=1)
        self.info_frame.grid_columnconfigure(2, weight=1)
        self.info_frame.grid_rowconfigure(0, weight=1)
        self.info_frame.grid_rowconfigure(1, weight=1)

        self.order_id_box.grid(row=0, column=0, columnspan=1, sticky="w", padx=20, pady=(20, 0))

        self.customer.grid(row=0, column=1, pady=(20, 0), sticky="w")
        self.price.grid(row=1, column=1, pady=(0, 20), sticky="w")
        self.date.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="sw")
        # self.update_info_button.grid(row=0, column=2)
        
        items = json.loads(values[2])

        self.create_items_list(items, components_prices)

        # Specify the widgets to destroy
        self.add_widgets_to_destroy([self.info_frame, self.items_frame])

    def create_info_box(self, label:str, value:str, small=False):
        """Create and return a info_box
        
        Parameters
        ----------
        label : name of the info box
        value : value of the box
        small : small info box
        """
        frame = Frame(self.info_frame, background="transparent")
        l = Label(
            frame, 
            text=label, 
            foreground="white",
            background="transparent",
            font=FONTS.get_font("paragraph", italic=small)
        )
        i = Label(
            frame, 
            text=value, 
            foreground="white",
            background="transparent",
            font=FONTS.get_font("heading3" if not small else "paragraph", bold=True)
        )
        l.pack(anchor="w")
        i.pack(anchor="w")

        return frame
    
    def create_items_list(self, items, components_prices):
        self.scrollbar = AccentHorizontalScrollbar(self.items_frame)
        self.items_list = CustomListView(self.items_frame,
            (
                "part_number",
                "amount",
                "price",
                "total"
            ),
            self.scrollbar.set
        )
        self.scrollbar.add_command(self.items_list.yview)


        self.items_list.config_headings({
            "part_number": {"text": "Part number"},
            "amount": {"text": "Amount"},
            "price": {"text": "Price"},
            "total": {"text": "Total"}
        })

        self.items_list.config_columns({
            "part_number": {"anchor": "center"},
            "amount": {"anchor": "center"},
            "price": {"anchor": "center"},
            "total": {"anchor": "center"}
        })

        for part_number, amount in list(items.items()):
            item_price = components_prices[part_number]
            row = (part_number, amount, item_price, floor(amount*item_price * 100)/100)
            self.items_list.add_item(row)

        self.scrollbar.pack(side="right", fill="y")
        self.items_list.pack(side="left", fill="both", expand=True)
