from ...gui import Screen, SubScreen, Frame, Label
from ...constants import COLORS, FONTS
from .CustomerDetailedView import CustomerDetailedView
from tkinter import Entry, Menubutton, Menu, BooleanVar, PhotoImage
from .AddCustomerWindow import AddCustomerWindow
from ...components import AccentButton, AccentHorizontalScrollbar, CustomListView

class CustomerScreen(Screen):
    """App's main screen"""
    def __init__(self, master, app_controller):
        """Init screen"""
        super().__init__(master, background="white",
            title="Manufacturer",
            title_font=FONTS.get_font("heading1", bold=True),
            title_bar_foreground=COLORS.ACCENT
        )
        self.app_controller = app_controller
        self.sorts = [0, 0, 0]
        self.sort_asc_img = PhotoImage(file="./images/arrow-up.png")
        self.sort_desc_img = PhotoImage(file="./images/arrow-down.png")
        self.no_sort_img = PhotoImage(file="./images/blank.png")

        self.add_subscreen("manufacturer_main", SubScreen(self.main_frame,
            render_function=self.render_customer,
        ))
        self.add_subscreen("detailed_view", CustomerDetailedView(self.main_frame, self.app_controller))
        self.navigate_subscreen("manufacturer_main")
    
    def on_sort(self, subscreen, event):
        tree_view: CustomListView = subscreen.tree_view_frame.table_frame.tree_view
        region = tree_view.identify_region(event.x, event.y)

        if region != "heading":
            return
        
        column_id = tree_view.identify_column(event.x)
        column_index = int(column_id[1]) -1
        self.sorts[column_index] = (self.sorts[column_index] + 1) % 3
        if self.sorts[column_index] == 0:
            tree_view.heading(column_id, image=self.no_sort_img)
        elif self.sorts[column_index] == 1:
            tree_view.heading(column_id, image=self.sort_asc_img)
        else:
            tree_view.heading(column_id, image=self.sort_desc_img)
        self.apply_filters(subscreen)
    
    def render_customer(self, subscreen, props=None):
        # Initialize tree view frame and filter frame
        subscreen.tree_view_frame = Frame(subscreen, background=COLORS.WHITE)
        subscreen.filters_frame = Frame(subscreen, background=COLORS.SECONDARY, width=120)
        
        # Make the frame take up the hold space
        subscreen.tree_view_frame.pack_propagate(False)
        subscreen.tree_view_frame.grid_propagate(False)

        # Config the grid
        subscreen.grid_columnconfigure(0, weight=10)
        subscreen.grid_columnconfigure(1, weight=1)
        subscreen.grid_rowconfigure(0, weight=1)

        subscreen.tree_view_frame.grid(row=0, column=0, sticky="nsew")
        subscreen.filters_frame.grid(row=0, column=1, sticky="nsew")\
        
        # Build the filter frame
        self.build_filters_frame(subscreen)

        # Build the tree view
        self.build_tree_view(subscreen)

        # Specify the widget to destroy
        subscreen.add_widgets_to_destroy([subscreen.tree_view_frame, subscreen.filters_frame])
    
    def build_filters_frame(self, subscreen):
        """Create the filters frame"""
        filters_frame = subscreen.filters_frame

        # Filters label
        filters_frame.label = Label(
            filters_frame, 
            "FILTERS", 
            background="transparent", 
            foreground="white", 
            font=FONTS.get_font("heading2", bold=True)
        )
        filters_frame.label.pack(pady=(10, 0))

        # ID filter
        filters_frame.customer_id_label = Label(
            filters_frame, 
            text="Customer's ID",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.customer_id_label.pack(anchor="w", pady=5, padx=14)
        filters_frame.customer_id_entry = Entry(filters_frame)
        filters_frame.customer_id_entry.pack(fill="x", padx=14)

        # Customer name filter
        filters_frame.customer_name_label = Label(
            filters_frame, 
            text="Name",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.customer_name_label.pack(anchor="w", pady=5, padx=14)
        filters_frame.customer_name_entry = Entry(filters_frame)
        filters_frame.customer_name_entry.pack(fill="x", padx=14)

        # Customer phone number filter
        filters_frame.phone_number_label = Label(
            filters_frame, 
            text="Phone number",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.phone_number_label.pack(anchor="w", pady=5, padx=14)
        filters_frame.phone_number_entry = Entry(filters_frame)
        filters_frame.phone_number_entry.pack(fill="x", padx=14)

       
        # Apply filter button
        filters_frame.apply_button = AccentButton(filters_frame,
            text="Apply",
            command=lambda: self.apply_filters(subscreen),
        )
        filters_frame.apply_button.pack(side="bottom", fill="both", pady=20, padx=14)

    def on_double_click(self, subscreen, event):
        """Handle  click event"""
        tree_view: CustomListView = subscreen.tree_view_frame.table_frame.tree_view
        region = tree_view.identify_region(event.x, event.y)

        if region != "cell":
            return

        selected_iid = tree_view.focus()
        values = tree_view.item(selected_iid)["values"]

        self.navigate_subscreen(subscreen_name="detailed_view", props=values)

    def build_tree_view(self, subscreen):
        """Build the component tree view table"""
        # Crate search bar and table frame
        action_bar_frame = subscreen.tree_view_frame.action_bar_frame = Frame(subscreen.tree_view_frame, background="transparent")
        table_frame = subscreen.tree_view_frame.table_frame = Frame(subscreen.tree_view_frame, background="transparent")

        action_bar_frame.pack(fill="x")
        table_frame.pack(fill="both", expand=True)
    
        # Add customer button
        action_bar_frame.add_customer_button = AccentButton(action_bar_frame,
            lambda: AddCustomerWindow(self,
                self.app_controller,
                lambda: self.apply_filters(subscreen)
            ),
            "ADD +",
            activebackground="white"
        )
        action_bar_frame.add_customer_button.pack(side="left", pady=20, padx=20, ipadx=14, ipady=2)

        
        # Create scroll bar
        scroll_bar = table_frame.scroll_bar = AccentHorizontalScrollbar(table_frame)

        # Create the tree view
        tree_view = table_frame.tree_view = CustomListView(
            table_frame, 
            columns=(
                "id", 
                "name", 
                "phone_number", 
            ),
            yscrollcommand=scroll_bar.set,
        )

        scroll_bar.add_command(tree_view.yview)

        tree_view.config_headings({
            "id": {"text": "ID"},
            "name": {"text": "Name"},
            "phone_number": {"text": "Phone number"},
        })

        tree_view.config_columns({
            "id": {"anchor": "center"},
            "name": {"anchor": "center"},
            "phone_number": {"anchor": "center"},
        })

        tree_view.pack(side="left", fill="both", expand=True)
        scroll_bar.pack(side="left", fill="y")

        # Bind double click envent
        tree_view.bind("<Double-1>", lambda e: self.on_double_click(subscreen, e))
        tree_view.bind("<Button-1>", lambda e: self.on_sort(subscreen, e))


        # self.apply_filters(subscreen)

    def get_all_filter(self, subcreen):
        """Get all filter and search

        The return dict will be of the form
        {
            "id": "abcxyz",
            "name" : "132abvc",
            "phone_number" : "0123213"
        }
        """
        
        filters_frame = subcreen.filters_frame

        filters_dict = {}
        # Get search option
        filters_dict["id"] = filters_frame.customer_id_entry.get()
        filters_dict["name"] = filters_frame.customer_name_entry.get()
        filters_dict["phone_number"] = filters_frame.phone_number_entry.get()

        return filters_dict
    
    def clear_all_items(self, subscreen):
        tree_view :CustomListView = subscreen.tree_view_frame.table_frame.tree_view
        for item in tree_view.get_children():
            tree_view.delete(item)

    def get_all_sorting(self):
        sort_column = [
            "id", 
            "name", 
            "phone_number", 
        ]
        sort_options = []
        for index, op in enumerate(self.sorts):
            if op == 0:
                continue
            if op == 1:
                sort_options.append((sort_column[index], "asc")) 
            if op == 2:
                sort_options.append((sort_column[index], "desc")) 

        return sort_options

    def apply_filters(self, subscreen):
        """Applying the filters"""
        tree_view :CustomListView = subscreen.tree_view_frame.table_frame.tree_view
        filters = self.get_all_filter(subscreen)
        sort_options = self.get_all_sorting()
        no_result, result = self.app_controller.get_list_with_filters("manufacturer", filters, sort_options)
        self.clear_all_items(subscreen)
        for manufacturer in result:
            manufacturer_info = manufacturer.get_all_info()
            manufacturer_info.append(manufacturer.get_image_path())
            tree_view.add_item(manufacturer_info)