from ...gui import SubScreen, Label, Frame
from tkinter import Entry, StringVar, Menu, Menubutton, BooleanVar, Radiobutton, PhotoImage
from ...constants import COLORS, FONTS
from .AddOrderWindow import AddOrderWindow
from ...components import AccentButton, AccentHorizontalScrollbar, CustomListView
from math import floor
import json

class OrderListView(SubScreen):
    """This class display a table of component within a category"""
    def __init__(self, master, navigation_function, app_controller):
        """Init the view
        
        Parameters
        ----------
        master : master widget
        navigation_function : function use to navigate
        """
        super().__init__(master, background=COLORS.WHITE, title="Orders")

        self.app_controller = app_controller
        
        self.navigate = navigation_function
        self.sort_options = {
            "order_id": 0,
            "customer_id": 0,
            "items": 0,
            "date": 0,
            "price": 0,
        }
        self.sort_asc_img = PhotoImage(file="./images/arrow-up.png")
        self.sort_desc_img = PhotoImage(file="./images/arrow-down.png")
        self.no_sort_img = PhotoImage(file="./images/blank.png")
        self.customers_ids = self.get_customers_ids()
        self.components_prices = self.app_controller.get_all_components_prices()

    def get_customers_ids(self):
        customers_ids = {}
        result = self.app_controller.get_list("customer")
        for c in result:
            customers_ids[c.get_id()] = c.get_name()
        return customers_ids

    # Override render method
    def render(self, props=None):
        super().render()

        # Initialize tree view frame and filter frame
        self.tree_view_frame = Frame(self, background=COLORS.WHITE)
        self.filters_frame = Frame(self, background=COLORS.SECONDARY, width=120)
        
        # Make the frame take up the hold space
        self.tree_view_frame.pack_propagate(False)
        self.tree_view_frame.grid_propagate(False)

        # Config the grid
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tree_view_frame.grid(row=0, column=0, sticky="nsew")
        self.filters_frame.grid(row=0, column=1, sticky="nsew")

        # Build the filter frame
        self.build_filters_frame()
        
        # Build the tree view
        self.build_tree_view()

        # Specify the widget to destroy
        self.add_widgets_to_destroy([self.tree_view_frame, self.filters_frame])

    def on_sort(self, event):
        tree_view: CustomListView = self.tree_view_frame.table_frame.tree_view
        region = tree_view.identify_region(event.x, event.y)

        if region != "heading":
            return
        
        column_id = tree_view.identify_column(event.x)
        column_index = int(column_id[1]) -1

        sort_column = [
            "order_id",
            "customer_id",
            "items",
            "date",
            "price"
        ]


        self.sort_options[sort_column[column_index]] = (self.sort_options[sort_column[column_index]] + 1) % 3
        if self.sort_options[sort_column[column_index]] == 0:
            tree_view.heading(column_id, image=self.no_sort_img)
        elif self.sort_options[sort_column[column_index]] == 1:
            tree_view.heading(column_id, image=self.sort_asc_img)
        else:
            tree_view.heading(column_id, image=self.sort_desc_img)

        self.apply_filters()


    def on_double_click(self, event):
        """Handle double click event"""
        tree_view: CustomListView = self.tree_view_frame.table_frame.tree_view
        region = tree_view.identify_region(event.x, event.y)

        if region != "cell":
            return

        selected_iid = tree_view.focus()
        values = tree_view.item(selected_iid)["values"]

        self.navigate(subscreen_name="detailed_view", props={"values": values, "components_prices": self.components_prices})

    def build_tree_view(self):
        """Build the component tree view table"""
        # Crate search bar and table frame
        search_bar_frame = self.tree_view_frame.search_bar_frame = Frame(self.tree_view_frame, background="transparent")
        table_frame = self.tree_view_frame.table_frame = Frame(self.tree_view_frame, background="transparent")

        search_bar_frame.pack(fill="x")
        table_frame.pack(fill="both", expand=True)
 
        # Search bar
        search_bar_frame.label = Label(search_bar_frame, text="Order ID", background="transparent", font=FONTS.get_font("paragraph"))
        search_bar_frame.entry = Entry(search_bar_frame, font=FONTS.get_font("paragraph"))
        search_bar_frame.button = AccentButton(
            search_bar_frame, 
            self.apply_filters, 
            "Search", 
            image="./images/search.png",
            activebackground="white",
            compound="right",
        )
        search_bar_frame.button.pack(side="right", fill="y", pady=20, ipadx=14, ipady=2, padx=20)
        search_bar_frame.entry.pack(side="right", fill="y", pady=20, ipadx=10, ipady=5)
        search_bar_frame.label.pack(side="right", fill="y", pady=20, ipadx=10, ipady=5)

        # Add component button
        search_bar_frame.add_order_button = AccentButton(search_bar_frame,
            lambda: AddOrderWindow(self,
                self.app_controller,
                self.apply_filters,
            ),
            "ADD +",
            activebackground="white",
        )
        search_bar_frame.add_order_button.pack(side="left", pady=20, padx=20, ipadx=14, ipady=2)
        
        # Create scroll bar
        scroll_bar = table_frame.scroll_bar = AccentHorizontalScrollbar(table_frame)

        # Create the tree view
        columns = [
            "order_id", 
            "customer", 
            "items",
            "date", 
            "total_price", 
        ]
        tree_view = table_frame.tree_view = CustomListView(
            table_frame, 
            columns=columns,
            yscrollcommand=scroll_bar.set,
        )

        scroll_bar.add_command(tree_view.yview)

        # Config the headings
        headings = {
            "order_id": {"text": "Order ID"},
            "customer": {"text": "Customer"},
            "items": {"text": "items"},
            "date": {"text": "Purchase date"},
            "total_price": {"text": "Total price"},
        }
        tree_view.config_headings(headings)

        # Config the rows
        columns_setting = {
            "order_id": {"anchor": "center", "width": 100, "stretch": False},
            "customer": {"anchor": "center", "width": 100, "stretch": False},
            "date": {"anchor": "center", "width": 140, "stretch": False},
            "items": {"anchor": "center", "width": 250, "stretch": False},
            "total_price": {"anchor": "center",},
        }
        tree_view.config_columns(columns_setting)

        tree_view.pack(side="left", fill="both", expand=True)
        scroll_bar.pack(side="left", fill="y")

        # Bind double click envent
        tree_view.bind("<Double-1>", self.on_double_click)
        tree_view.bind("<Button-1>", self.on_sort)

        self.apply_filters()

    def build_filters_frame(self):
        """Create the filters frame"""
        filters_frame = self.filters_frame

        # Filters label
        filters_frame.label = Label(
            filters_frame, 
            "FILTERS", 
            background="transparent", 
            foreground="white", 
            font=FONTS.get_font("heading2", bold=True)
        )
        self.filters_frame.label.pack(pady=(10, 0))

        # date filter
        filters_frame.customer_label = self.create_filter_label("Customer's id")
        filters_frame.customer_label.pack(anchor="w", pady=5, padx=14)
        filters_frame.customer_entry = Entry(filters_frame)
        filters_frame.customer_entry.pack(fill="x", padx=14)

        

        filters_frame.date_label = self.create_filter_label("Purchase date")
        filters_frame.date_label.pack(anchor="w", pady=5, padx=14)

        filters_frame.date_frame, \
        filters_frame.date_from_entry, \
        filters_frame.date_to_entry = self.create_from_to_input()
        filters_frame.date_frame.pack(fill="x")

        # total price filter
        filters_frame.total_price_label = self.create_filter_label("Price")
        filters_frame.total_price_label.pack(anchor="w", pady=5, padx=14)

        filters_frame.total_price_frame, \
        filters_frame.price_from_entry, \
        filters_frame.price_to_entry = self.create_from_to_input()
        filters_frame.total_price_frame.pack(fill="x")
        
        # items filter

        # Apply filter button
        filters_frame.apply_button = AccentButton(filters_frame,
            text="Apply",
            command=self.apply_filters,
        )
        filters_frame.apply_button.pack(side="bottom", fill="both", pady=20, padx=14)

    def create_options_menu_filter(self, label:str, options: tuple[str]):
        """Create a options menu with button
        
        Parameters
        ----------
        label : label of the button
        options : option available
        """
        filters_frame = self.filters_frame
        
        # Create option menu frame
        options_menu_frame = Frame(filters_frame, background="transparent")

        # Create the option menu button
        options_menu_button = Menubutton(
            options_menu_frame, 
            text=label,
            background=COLORS.SECONDARY,
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left",
            activeforeground=COLORS.ACCENT,
        )
        options_menu_button.pack(anchor="w", pady=5, padx=9)

        # Create choosen option label
        choosen_option_label = Label(
            options_menu_frame,
            text="None",
            font=FONTS.get_font("paragraph"),
            background="transparent",
            foreground="white"
        )
        choosen_option_label.pack(anchor="w", padx=14)

        # Create menu
        options_menu = options_menu_button.options_menu = Menu(
            options_menu_button,
            tearoff=False,
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph"),
            activebackground="white",
            activeforeground=COLORS.ACCENT
        )
        option_state_variable = f"{label.lower()}_options"
        option_index_state_variable = f"{label.lower()}_options_index"
        self.states[option_state_variable] = []
        self.states[option_index_state_variable] = []

        def toggle_option(index, option):
            if option in self.states[option_state_variable]:
                self.states[option_state_variable].remove(option)
                self.states[option_index_state_variable].remove(str(index))
            else:
                self.states[option_state_variable].append(option)
                self.states[option_index_state_variable].append(str(index))
            choosen_option_label.config(text=", ".join(self.states[option_index_state_variable]))
        
        options_menu.option_variables: dict[str, BooleanVar] = {}
        for index, option in enumerate(options):
            options_menu.option_variables[option] = BooleanVar(False)
            options_menu.add_checkbutton(
                label=f"{index}. {option}", 
                onvalue=True, 
                offvalue=False, 
                variable=options_menu.option_variables[option], 
                command=(lambda i, o: lambda: toggle_option(i, o))(index, option),
            )
       
        options_menu_button.configure(menu=options_menu)

        return options_menu_frame

    def create_filter_label(self, label: str):
        """Create a filter label
        
        Parameters
        ----------
        label : name of the filter
        """
        filters_frame = self.filters_frame
        l = Label(
            filters_frame, 
            text=label,
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        return l

    def create_from_to_input(self):
        """Create a from to input"""
        filters_frame = self.filters_frame
        input_frame = Frame(filters_frame, background="transparent")
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=1)
        f = Label(input_frame, 
            "From", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        f.grid(row=0, column=0, sticky="w", padx=14)

        f_e = Entry(input_frame)
        f_e.grid(row=0, column=1, sticky="ew", padx=(0, 14))

        t = Label(input_frame, 
            "To", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        t.grid(row=1, column=0, sticky="w", padx=14)

        t_e = Entry(input_frame)
        t_e.grid(row=1, column=1, sticky="ew", padx=(0, 14))

        return input_frame, f_e, t_e
    
    def get_all_filter(self):
        """Get all filter and search

        The return dict will be of the form
        {
            "order_id": "abcxyz",
            "customer_id" : "132abvc",
            "price" : "123",
            "items": "ABC"
            "date" : [("<=","10"), (">=, 4")],
        }
        """
        
        filters_frame = self.filters_frame
        search_bar_frame = self.tree_view_frame.search_bar_frame

        filters_dict = {}
        # Get search option
        filters_dict["order_id"] = search_bar_frame.entry.get()
        
        filters_dict["customer_id"] = filters_frame.customer_entry.get()

        # Get inventory date
        filters_dict["date"] = {
            "to": filters_frame.date_to_entry.get(),
            "from": filters_frame.date_from_entry.get()
        }

      
        return filters_dict
    
    def clear_all_items(self):
        tree_view :CustomListView = self.tree_view_frame.table_frame.tree_view
        for item in tree_view.get_children():
            tree_view.delete(item)

    def get_all_sorting(self):
        sort_options = {}
        for key, value in list(self.sort_options.items()):
            if key == "price":
                continue
            if value == 0:
                continue
            if value == 1:
                sort_options[key] = "asc"
            if value == 2:
                sort_options[key] = "desc"
        return sort_options

    def apply_filters(self):
        """Applying the filters"""
        tree_view :CustomListView = self.tree_view_frame.table_frame.tree_view
        filters_frame = self.filters_frame
         # Get price
        price_from =  filters_frame.price_from_entry.get()
        price_to = filters_frame.price_to_entry.get()
        price_from = 0 if price_from == "" else float(price_from)
        price_to = 999999999999999 if price_to == "" else float(price_to)

        filters = self.get_all_filter()
        sort_options = self.get_all_sorting()
        result = self.app_controller.get_filtered_list("order", filters, sort_options)
        rows = []
        for order in result:
            order_info = order.get_all_info()
            price = sum([no_item*self.components_prices[part_number] for part_number, no_item in list(order.get_items().items())])
            order_info[1] = f"({order_info[1]}) {self.customers_ids[order.get_customer_id()]}"
            price = floor(price * 100) / 100
            order_info[2] = json.dumps(order_info[2])
            order_info.append(price)
            rows.append(order_info)

        if self.sort_options["price"] != 0:
            rows = sorted(rows, key=lambda r: r[-1], reverse=self.sort_options["price"] == 2)
        rows = list(filter(lambda r: r[-1] >= price_from and r[-1] <= price_to, rows))
        self.clear_all_items()
        for r in rows:
            tree_view.add_item(r)

        