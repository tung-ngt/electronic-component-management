from ...gui import SubScreen, Label, Frame
from tkinter import Entry, StringVar, Menu, Menubutton, BooleanVar, Radiobutton, PhotoImage
from ...constants import COLORS, FONTS
from .AddComponentWindow import AddComponentWindow
from ...components import AccentButton, AccentHorizontalScrollbar, CustomListView

class ComponentListView(SubScreen):
    """This class display a table of component within a category"""
    def __init__(self, master, navigation_function, app_controller):
        """Init the view
        
        Parameters
        ----------
        master : master widget
        navigation_function : function use to navigate
        """

        # Initialize the subscreen
        super().__init__(master, background=COLORS.WHITE)

        # Set app_controller and navigate_function
        self.app_controller = app_controller
        self.navigate = navigation_function

        # Get manufacturers id from app_controller
        self.get_all_manufacturers_ids()

        # Initalize sort options to no sort
        self.sort_options = {
            "part_number": 0, 
            "price": 0, 
            "guarantee": 0, 
            "mnf_id": 0, 
            "inventory_date": 0,
            "sub_category": 0, 
            "stock": 0,
            "special_attr": 0
        }

        # Load sort images
        self.sort_asc_img = PhotoImage(file="./images/arrow-up.png")
        self.sort_desc_img = PhotoImage(file="./images/arrow-down.png")
        self.no_sort_img = PhotoImage(file="./images/blank.png")

    def get_all_manufacturers_ids(self):
        """Get all the manufacturers id and name"""
        # Get list of manufacturers
        manufacturers = self.app_controller.get_list("manufacturer")
        self.manufacturers_ids = {}
        for manufacturer in manufacturers:
            self.manufacturers_ids[manufacturer.get_id()] = manufacturer.get_name()

    # Override render method
    def render(self, props=None):
        super().render()
        self.component_type: str = props["selected"]
        self.title = self.component_type.capitalize()

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
        """Run when the heading is clicked"""
        tree_view: CustomListView = self.tree_view_frame.table_frame.tree_view

        # Check if the region is the heading
        region = tree_view.identify_region(event.x, event.y)
        if region != "heading":
            return
        
        # Get the column that the user clicked on
        column_id = tree_view.identify_column(event.x)
        column_index = int(column_id[1]) -1

        sort_column = [
            "part_number", 
            "price", 
            "guarantee", 
            "mnf_id", 
            "inventory_date",
            "sub_category", 
            "stock",
            "special_attr"
        ]

        # Update sort_options
        self.sort_options[sort_column[column_index]] = (self.sort_options[sort_column[column_index]] + 1) % 3

        # Update sort indicator
        if self.sort_options[sort_column[column_index]] == 0:
            tree_view.heading(column_id, image=self.no_sort_img)
        elif self.sort_options[sort_column[column_index]] == 1:
            tree_view.heading(column_id, image=self.sort_asc_img)
        else:
            tree_view.heading(column_id, image=self.sort_desc_img)

        # Get new list
        self.apply_filters()

    def on_double_click(self, event):
        """Handle double click event
        
        Navigate to detailed view of a row
        """
        tree_view: CustomListView = self.tree_view_frame.table_frame.tree_view

        # Check if the user click on a row
        region = tree_view.identify_region(event.x, event.y)
        if region != "cell":
            return
        
        # Get the row
        selected_iid = tree_view.focus()
        values = tree_view.item(selected_iid)["values"]

        # Navigate to detail view
        self.navigate(subscreen_name="detailed_view", props={"component_type": self.component_type, "values": values})

    def build_tree_view(self):
        """Build the component tree view table"""
        # Crate search bar and table frame
        search_bar_frame = self.tree_view_frame.search_bar_frame = Frame(self.tree_view_frame, background="transparent")
        table_frame = self.tree_view_frame.table_frame = Frame(self.tree_view_frame, background="transparent")

        search_bar_frame.pack(fill="x")
        table_frame.pack(fill="both", expand=True)
 
        # Search bar
        search_bar_frame.search_option = StringVar()
        search_bar_frame.search_option.set("part_number")
        search_bar_frame.part_number_search = Radiobutton(search_bar_frame,
            text="Part number",
            value="part_number",
            variable=search_bar_frame.search_option,
            font=FONTS.get_font("paragraph"),
        )
        search_bar_frame.man_search = Radiobutton(search_bar_frame,
            text="Manufacturer's id",
            value="man_name",
            variable=search_bar_frame.search_option,
            font=FONTS.get_font("paragraph"),
        )

        search_bar_frame.entry = Entry(self.tree_view_frame.search_bar_frame, font=FONTS.get_font("paragraph"))
        search_bar_frame.button = AccentButton(
            self.tree_view_frame.search_bar_frame, 
            self.apply_filters, 
            "Search", 
            image="./images/search.png",
            activebackground="white",
            compound="right",
        )
        search_bar_frame.button.pack(side="right", fill="y", pady=20, ipadx=14, ipady=2, padx=20)
        search_bar_frame.entry.pack(side="right", fill="y", pady=20, ipadx=10, ipady=5)
        search_bar_frame.part_number_search.pack(side="right", fill="y", pady=20, padx=20)
        search_bar_frame.man_search.pack(side="right", fill="y", pady=20)

        # Add component button
        search_bar_frame.add_component_button = AccentButton(search_bar_frame,
            lambda: AddComponentWindow(self,
                self.component_type,
                self.app_controller,
                self.apply_filters,
            ),
            "ADD +",
            activebackground="white",
        )
        search_bar_frame.add_component_button.pack(side="left", pady=20, padx=20, ipadx=14, ipady=2)
        
        # Create scroll bar
        scroll_bar = table_frame.scroll_bar = AccentHorizontalScrollbar(table_frame)

        # Create the tree view
        columns = [
            "part_number", 
            "price", 
            "guarantee", 
            "manufacturer", 
            "inventory_date",
            "sub_category", 
            "stock",
            
        ]
        if self.component_type == "ic":
            columns.append("clock")
        elif self.component_type == "sensor":
            columns.append("sensor_type")
        else:
            columns.append(self.component_type[:-2] + "ance")
            
        tree_view = table_frame.tree_view = CustomListView(
            table_frame, 
            columns=columns,
            yscrollcommand=scroll_bar.set,
        )

        scroll_bar.add_command(tree_view.yview)

        # Config the headings
        headings = {
            "part_number": {"text": "Part number"},
            "price": {"text": "Price"},
            "guarantee": {"text": "Guarantee"},
            "manufacturer": {"text": "Manufacturer"},
            "inventory_date": {"text": "Inventory date"},
            "sub_category": {"text": "Subcategory"},
            "stock": {"text": "Stock"},
        }
        if self.component_type == "ic":
            headings["clock"] = {"text": "Clock"}
        elif self.component_type == "sensor":
            headings["sensor_type"] = {"text": "Sensor type"}
        else:
            headings[self.component_type[:-2] + "ance"] = {"text": (self.component_type[:-2] + "ance").capitalize()}
        tree_view.config_headings(headings)

        # Config the rows
        columns_setting = {
            "part_number": {"anchor": "center", "width": 200, "stretch": False},
            "price": {"anchor": "center", "width": 70, "stretch": False},
            "guarantee": {"anchor": "center", "width": 120, "stretch": False},
            "manufacturer": {"anchor": "center"},
            "inventory_date": {"anchor": "center", "width": 140, "stretch": False},
            "sub_category": {"anchor": "center"},
            "stock": {"anchor": "center", "width": 70, "stretch": False},
        }
        if self.component_type == "ic":
            headings["clock"] = {"anchor": "center", "stretch": False}
        elif self.component_type == "sensor":
            headings["sensor_type"] = {"anchor": "center"}
        else:
            headings[self.component_type[:-2] + "ance"] = {"anchor": "center", "width": 70, "stretch": False}
        tree_view.config_columns(columns_setting)

        scroll_bar.pack(side="right", fill="y")
        tree_view.pack(side="left", fill="both", expand=True)

        # Bind click envent
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

        # Inventory date filter
        filters_frame.inventory_date_label = self.create_filter_label("Inventory date")
        filters_frame.inventory_date_label.pack(anchor="w", pady=5, padx=14)

        filters_frame.date_frame, \
        filters_frame.date_from_entry, \
        filters_frame.date_to_entry = self.create_from_to_input()
        filters_frame.date_frame.pack(fill="x")

        # Price filter
        filters_frame.price_label = self.create_filter_label("Price")
        filters_frame.price_label.pack(anchor="w", pady=5, padx=14)

        filters_frame.price_frame, \
        filters_frame.price_from_entry, \
        filters_frame.price_to_entry = self.create_from_to_input()
        filters_frame.price_frame.pack(fill="x")
        
        # Guarantee filter
        filters_frame.guarantee_label = self.create_filter_label("Guarantee")
        filters_frame.guarantee_label.pack(anchor="w", pady=5, padx=14)

        filters_frame.guarantee_frame, \
        filters_frame.guarantee_from_entry, \
        filters_frame.guarantee_to_entry = self.create_from_to_input()
        filters_frame.guarantee_frame.pack(fill="x")

        # Stock filter
        filters_frame.stock_label = self.create_filter_label("Stock")
        filters_frame.stock_label.pack(anchor="w", pady=5, padx=14)

        filters_frame.stock_frame, \
        filters_frame.stock_from_entry, \
        filters_frame.stock_to_entry = self.create_from_to_input()
        filters_frame.stock_frame.pack(fill="x")

        # Subcategory filter
        filters_frame.subcategory_menu_frame = self.create_options_menu_filter("Subcategory", self.app_controller.get_distinct_column(self.component_type, "sub_category"))
        filters_frame.subcategory_menu_frame.pack(fill="x")

        # Optional filter
        if self.component_type == "sensor":
            filters_frame.sensor_menu_frame = self.create_options_menu_filter("Sensor type", self.app_controller.get_distinct_column("sensor", "sensor_type"))
            filters_frame.sensor_menu_frame.pack(fill="x")
            self.optional_type = "sensor_type"
        else:
            optional_label: str = self.component_type[:-2] + "ance" \
                if self.component_type in ["capacitor", "inductor", "resistor"] \
                else "clock"
            self.optional_type = optional_label
            filters_frame.optional_label = self.create_filter_label(optional_label.capitalize())
            filters_frame.optional_label.pack(anchor="w", pady=5, padx=14)

            filters_frame.optional_frame, \
            filters_frame.optional_from_entry, \
            filters_frame.optional_to_entry = self.create_from_to_input()
            filters_frame.optional_frame.pack(fill="x")

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
            options_menu.option_variables[option] = BooleanVar()
            options_menu.option_variables[option].set(False)
            options_menu.add_checkbutton(
                label=f"{index}. {option}", 
                onvalue=True, 
                offvalue=False, 
                variable=options_menu.option_variables[option], 
                command=(lambda i, o: lambda: toggle_option(i, o))(index, option),
            )
       
        options_menu_button.configure(menu=options_menu)

        return options_menu_frame

    def create_filter_label(self, label: str) -> Label:
        """Create a filter label
        
        Parameters
        ----------
        label : name of the filter

        Return a Label
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
            "mnf_id": "abcxyz",
            "part_number" : "132abvc",
            "inventory_date" : {"from":"2023-12-01"), "to": "2022-01-01"},
            "sensor_type" : ["sensor 1", "sensor 2"]
        }
        """
        
        filters_frame = self.filters_frame
        search_bar_frame = self.tree_view_frame.search_bar_frame

        filters_dict = {}
        # Get search option
        if search_bar_frame.search_option.get() == "part_number":
            filters_dict["part_number"] = search_bar_frame.entry.get()
            filters_dict["mnf_id"] = ""
        else:
            filters_dict["part_number"] = ""
            filters_dict["mnf_id"] = search_bar_frame.entry.get()
        
        # Get inventory date
        filters_dict["inventory_date"] = {
            "from": filters_frame.date_from_entry.get(),
            "to": filters_frame.date_to_entry.get(),
        }

        # Get price
        filters_dict["price"] = {
            "from": filters_frame.price_from_entry.get(),
            "to": filters_frame.price_to_entry.get(),
        }

        # Get guarantee
        filters_dict["guarantee"] = {
            "from": filters_frame.guarantee_from_entry.get(),
            "to": filters_frame.guarantee_to_entry.get(),
        }

        # Get stock
        filters_dict["stock"] = {
            "from": filters_frame.stock_from_entry.get(),
            "to": filters_frame.stock_to_entry.get(),
        }
        
        # Get subcategory
        filters_dict["sub_category"] = self.states["subcategory_options"]

        # Get optional filter
        if self.optional_type == "sensor_type":
            filters_dict[self.optional_type] = self.states["sensor type_options"]
        else:
            filters_dict[self.optional_type] = {
                "from": filters_frame.optional_from_entry.get(),
                "to": filters_frame.optional_to_entry.get(),
            }

        return filters_dict
    
    def clear_all_items(self):
        """Clear all items in the list view"""
        tree_view :CustomListView = self.tree_view_frame.table_frame.tree_view
        for item in tree_view.get_children():
            tree_view.delete(item)

    def get_all_sorting(self):
        """Convert the sort option
    
        The sort option will be of the form
        {
            "part_number: "asc",
            "date": "desc" 
        }
        """
        special_attr = ""
        if self.component_type == "ic":
            special_attr = "clock"
        elif self.component_type == "sensor":
            special_attr = "sensor_type"
        else:
           special_attr = self.component_type[:-2] + "ance"

        sort_options = {}
        for key, value in list(self.sort_options.items()):
            if key == "special_attr":
                column = special_attr
            else:
                column = key

            if value == 0:
                continue
            if value == 1:
                sort_options[column] = "asc"
            if value == 2:
                sort_options[column] = "desc"

        return sort_options

    def apply_filters(self):
        """Applying the filters"""
        
        tree_view :CustomListView = self.tree_view_frame.table_frame.tree_view

        # Get the filters and sort_options in the correct form
        filters = self.get_all_filter()
        sort_options = self.get_all_sorting()

        # Get the filtered list
        result = self.app_controller.get_filtered_list(self.component_type, filters, sort_options)
        
        self.clear_all_items()
        for component in result:
            component_info = component.get_all_info()
            component_info[3] = f"({component_info[3]}) {self.manufacturers_ids[component.get_mnf_id()]}"
            component_info.append(component.get_image_path())
            tree_view.add_item(component_info)