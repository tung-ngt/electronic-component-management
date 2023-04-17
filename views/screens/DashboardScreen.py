from ..gui import Screen, Label, Frame, SubScreen
from ..components import AccentButton
from ..constants import COLORS, FONTS
from tkinter import Canvas

class DashboardScreen(Screen):
    """App's main screen"""
    def __init__(self, master, app_controller):
        """Init screen

        This screen contains summaries of the system
        
        Parameters
        ----------
        master : master widget
        app_controller : the app controller
        """

        # Set master and app_controller
        self.master = master
        self.app_controller = app_controller

        # Initialize the screen
        super().__init__(master,
            background=COLORS.WHITE,
            title="Dashboard",
            title_font=FONTS.get_font("heading1", bold=True)
        )
        
        # Get data from app controller
        self.get_orders_info()
        self.get_customers_ids()
        self.get_recent_customer()

        # Specify subscreen
        self.add_subscreen("dashboard_main",
            SubScreen(
                self.main_frame,
                background=COLORS.WHITE,
                render_function=self.render_dashboard
            )
        )
        self.navigate_subscreen("dashboard_main")

    def get_customers_ids(self):
        """Get customers' ids from the app controller"""

        customers_ids = {}

        # Get the customers list
        customers = self.app_controller.get_list("customer")

        for c in customers:
            customers_ids[c.get_id()] = c.get_name()

        self.cutsomers_ids = customers_ids

    def get_recent_customer(self):
        """Get customers list who recently purchases some components"""

        recent_customer_id = []
        recent_customer = []

        # Get recent order and the customers' ids
        orders = self.app_controller.get_list("order")
        orders = sorted(orders, key=lambda o: o.get_date())[-5:]
        for o in orders:
            if o.get_customer_id() not in recent_customer_id:
                recent_customer_id.append(o.get_customer_id())

        # Get the customers infomation
        for i in recent_customer_id:
            recent_customer.append(f"({i}) {self.cutsomers_ids[i]}")

        self.recent_customer = recent_customer

    def get_orders_info(self):
        """Get number of orders made in a time frame"""
        total = 0
        data = {}

        # Get all orders
        orders = self.app_controller.get_list("order")

        # Increment orders count of the coresponding year 
        for o in orders:
            year = o.get_date().split("-")[0]
            if year in data.keys():
                data[year] += 1
            else:
                data[year] = 1
            total += 1

        # Sort the years
        keys = data.keys()
        keys = sorted(keys)
        sorted_data = {k: data[k] for k in keys}

        self.total_orders = total
        self.orders_data = sorted_data
        self.max_order = max(data.values())
        

    def render_dashboard(self, subscreen: SubScreen, props = None):
        """Render the dashboard"""

        # Create content Frame and config the grid
        subscreen.content = Frame(subscreen, background="transparent")
        subscreen.content.pack(anchor="center", fill="both", expand=True)

        subscreen.content.grid_rowconfigure(0, weight=1)
        subscreen.content.grid_rowconfigure(1, weight=1)
        subscreen.content.grid_columnconfigure(1, weight=1)
        subscreen.content.grid_columnconfigure(0, weight=1)
        subscreen.content.grid_columnconfigure(2, weight=1)

        # Create infomation boxes
        subscreen.box1 = Frame(subscreen.content, background=COLORS.BACKGROUND_LIGHT)
        subscreen.box2 = Frame(subscreen.content, background=COLORS.SECONDARY)
        subscreen.box3 = Frame(subscreen.content, background="#ffffff")
        subscreen.box4 = Frame(subscreen.content, background=COLORS.BACKGROUND_LIGHT)

        # Placement
        # box1 box1 box2
        # box3 box4 box2
        subscreen.box1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=(30, 10), pady=(30, 15))
        subscreen.box2.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=(15, 30), pady=(30, 50))
        subscreen.box3.grid(row=1, column=0, sticky="nsew", padx=(30,15), pady=(30, 50))
        subscreen.box4.grid(row=1, column=1, sticky="nsew", padx=(15,15), pady=(20, 50))
        
        # Force scale
        subscreen.box3.pack_propagate(False)
        subscreen.box4.pack_propagate(False)

        # Component infomation box
        subscreen.box3.items_count_label = Label(
            subscreen.box3,
            f"{self.app_controller.get_no_of_components()} items in inventory",
            background="transparent",
            font=FONTS.get_font("heading3")
        )
        subscreen.box3.items_count_label.pack(fill="both", expand=True)
        
        # Manufacturer infomation box
        subscreen.box4.manufacturer_count_label = Label(
            subscreen.box4,
            f"{len(self.app_controller.get_list('manufacturer'))} manufacturers",
            background="transparent",
            foreground=COLORS.PRIMARY,
            font=FONTS.get_font("heading3", bold=True)
        )
        subscreen.box4.manufacturer_count_label.pack(fill="both", expand=True)

        # Create the canvas for order chart
        canvas = subscreen.box1.canvas = Canvas(subscreen.box1, background=COLORS.BACKGROUND_LIGHT)
        canvas.pack(fill="both", expand=True)
        canvas.bind("<Configure>", self.draw_chart)

        
        # Create recent customers box
        subscreen.box2.label = Label(
            subscreen.box2,
            "Recent cutomers",
            foreground="white",
            background="transparent",
            font=FONTS.get_font("heading2", bold=True)
        )
        subscreen.box2.label.pack(pady=20)

        for c in self.recent_customer:
            Label(
                subscreen.box2,
                text=c,
                font=FONTS.get_font("paragraph"),
                foreground="white",
                background="transparent"
            ).pack(pady=10)
        
        # Dashboard refresh button
        subscreen.refresh_button = AccentButton(
            subscreen, 
            lambda: self.refresh_data(subscreen),
            "Refresh"
        )
        subscreen.refresh_button.place(relx=1, x=-30, rely=1, y=-10, anchor="se", width=150)

        # specify which widget to destroy when re
        subscreen.add_widgets_to_destroy([subscreen.content])

    def refresh_data(self, subscreen):
        """Rehydrate boxes with new data"""
        subscreen.box3.items_count_label.config(
            text=f"{self.app_controller.get_no_of_components()} items in inventory"
        )
        subscreen.box4.manufacturer_count_label.config(
            text=f"{len(self.app_controller.get_list('manufacturer'))} manufacturers"
        )
        self.get_orders_info()
        self.draw_chart(canvas=subscreen.box1.canvas)
        

    def draw_chart(self, event = None, canvas = None):
        """Draw the order chart"""

        # Get the canvas that is passed in or from the event
        if canvas == None:
            canvas = event.widget
        
        # Clear the canvas
        canvas.delete("all")

        # Get the canvas's dimensions
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # Compute the position to place the bars
        pos = canvas_width / (len(self.orders_data) + 1)
        max_bar_height = canvas_height - 150
        bar_bottom = canvas_height - 50
        bar_width = 50

        # Create the title 
        canvas.create_text(canvas_width / 2, 50, text=f"{self.total_orders} orders", font=FONTS.get_font("heading2", bold=True), anchor="center", fill=COLORS.PRIMARY)

        # Create bars for the years
        for index, (year, count) in enumerate(list(self.orders_data.items())):
            # Get the postion to place the current bar
            x_center = pos * (index + 1)

            # Compute the bar dimemsions
            ratio = count / self.max_order
            bar_left = x_center - bar_width / 2
            bar_right = x_center + bar_width / 2
            bar_height = max_bar_height * ratio
            bar_top = bar_bottom - bar_height

            # Get the y center to place count text
            y_center = (bar_top + bar_bottom) / 2

            # Create the bar
            canvas.create_rectangle(
                bar_left, bar_top, bar_right, bar_bottom, 
                fill=COLORS.ACCENT, outline=COLORS.ACCENT
            )
            # Create the year label
            canvas.create_text(
                x_center, bar_bottom + 20, 
                text=year, 
                anchor="center", 
                font=FONTS.get_font("paragraph")
            )
            # Create the count text
            canvas.create_text(
                x_center, y_center,
                text=count,
                font=FONTS.get_font("paragraph", bold=True),
                fill="white",
                anchor="center"
            )

