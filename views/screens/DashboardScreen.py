from ..gui import Screen, Label, Frame, SubScreen
from ..components import AccentButton
from ..constants import COLORS, FONTS
from tkinter import Canvas

class DashboardScreen(Screen):
    """App's main screen"""
    def __init__(self, master, app_controller):
        """Init screen"""
        self.app_controller = app_controller
        self.master = master
        super().__init__(master,
            background=COLORS.WHITE,
            title="Dashboard",
            title_font=FONTS.get_font("heading1", bold=True)
        )
        self.get_orders_info()
        self.get_customers_ids()
        self.get_recent_customer()
        self.add_subscreen("dashboard_main", SubScreen(self.main_frame, background=COLORS.WHITE, render_function=self.render_dashboard))
        self.navigate_subscreen("dashboard_main")

    def get_customers_ids(self):
        customers_ids = {}
        customers = self.app_controller.get_list("customer")

        for c in customers:
            customers_ids[c.get_id()] = c.get_name()

        self.cutsomers_ids = customers_ids

    def get_recent_customer(self):
        recent_customer_id = []
        recent_customer = []
        orders = self.app_controller.get_list("order")
        orders = sorted(orders, key=lambda o: o.get_date())[-5:]
        customers = self.app_controller.get_list("customer")
        for o in orders:
            if o.get_customer_id() not in recent_customer_id:
                recent_customer_id.append(o.get_customer_id())

        for i in recent_customer_id:
            recent_customer.append(f"({i}) {self.cutsomers_ids[i]}")

        self.recent_customer = recent_customer

    def get_orders_info(self):
        total = 0
        data = {}
        orders = self.app_controller.get_list("order")

        for o in orders:
            year = o.get_date().split("-")[0]
            if year in data.keys():
                data[year] += 1
            else:
                data[year] = 1
            total += 1

        keys = data.keys()
        keys = sorted(keys)
        sorted_data = {k: data[k] for k in keys}

        self.total_orders = total
        self.orders_data = sorted_data
        self.max_order = max(data.values())
        

    def render_dashboard(self, subscreen: SubScreen, props = None):
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

        subscreen.box1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=(30, 10), pady=(30, 15))
        subscreen.box2.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=(15, 30), pady=(30, 50))
        subscreen.box3.grid(row=1, column=0, sticky="nsew", padx=(30,15), pady=(30, 50))
        subscreen.box4.grid(row=1, column=1, sticky="nsew", padx=(15,15), pady=(20, 50))
        
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
            f"{len(self.app_controller.get_list('manufacturer'))} manufacturers",
            background="transparent",
            foreground=COLORS.PRIMARY,
            font=FONTS.get_font("heading3", bold=True)
        )
        subscreen.box4.manufacturer_count_label.pack(fill="both", expand=True)


        canvas = subscreen.box1.canvas = Canvas(subscreen.box1, background=COLORS.BACKGROUND_LIGHT)
        canvas.pack(fill="both", expand=True)
        canvas.bind("<Configure>", self.draw_chart)

        
        subscreen.refresh_button = AccentButton(
            subscreen, 
            lambda: self.refresh_data(subscreen),
            "Refresh"
        )
        subscreen.refresh_button.place(relx=1, x=-30, rely=1, y=-10, anchor="se", width=150)


        subscreen.box2.label = Label(
            subscreen.box2,
            "Recent cutomer",
            foreground="white",
            background="transparent",
            font=FONTS.get_font("heading2", bold=True)
        )
        subscreen.box2.label.pack(pady=20)

        for c in self.recent_customer:
            Label(subscreen.box2, text=c, font=FONTS.get_font("paragraph"), foreground="white", background="transparent").pack(pady=10)

        subscreen.add_widgets_to_destroy([subscreen.box1, subscreen.box2, subscreen.box3, subscreen.box4, subscreen.refresh_button])

    def refresh_data(self, subscreen):
        subscreen.box3.items_count_label.config(text=f"{self.app_controller.get_no_of_components()} items in inventory")
        subscreen.box4.manufacturer_count_label.config(text=f"{len(self.app_controller.get_list('manufacturer'))} manufacturers")
        self.get_orders_info()
        self.draw_chart(canvas=subscreen.box1.canvas)
        

    def draw_chart(self, event = None, canvas = None):
        if canvas == None:
            canvas = event.widget
        
        canvas.delete("all")

        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        pos = canvas_width / (len(self.orders_data) + 1)
        max_bar_height = canvas_height - 150
        bar_bottom = canvas_height - 50
        bar_width = 50

        canvas.create_text(canvas_width / 2, 50, text="Orders", font=FONTS.get_font("heading2", bold=True), anchor="center", fill=COLORS.PRIMARY)

        for index, (year, count) in enumerate(list(self.orders_data.items())):
            x_center = pos * (index + 1)
            ratio = count / self.max_order

            bar_left = x_center - bar_width / 2
            bar_right = x_center + bar_width / 2
            bar_height = max_bar_height * ratio
            bar_top = bar_bottom - bar_height

            y_center = (bar_top + bar_bottom) / 2

            canvas.create_rectangle(bar_left, bar_top, bar_right, bar_bottom, fill=COLORS.ACCENT, outline=COLORS.ACCENT)
            canvas.create_text(x_center, bar_bottom + 20, text=year, anchor="center", font=FONTS.get_font("paragraph"))
            canvas.create_text(x_center, y_center, text=count, font=FONTS.get_font("paragraph", bold=True), fill="white", anchor="center")

