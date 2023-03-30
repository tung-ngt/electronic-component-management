from ...gui import SubScreen, Label, Frame, Button, TreeView
from tkinter import Entry, StringVar, Menu, Menubutton, BooleanVar, Radiobutton
from tkinter.ttk import Scrollbar, Style
from ...constants import COLORS, FONTS

class ComponentListView(SubScreen):
    """This class display a table of component within a category"""
    def __init__(self, master, navigation_function):
        """Init the view
        
        Parameters
        ----------
        master : master widget
        navigation_function : function use to navigate
        """
        super().__init__(master, background=COLORS.WHITE)
        
        self.navigate = navigation_function

    # Override render method
    def render(self, props=None):
        super().render()
        self.title = props["selected"].capitalize()

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

        # Build the tree view
        self.build_tree_view()

        # Build the filter frame
        self.build_filters_frame()

        # Specify the widget to destroy
        self.add_widgets_to_destroy([self.tree_view_frame, self.filters_frame])

    def on_double_click(self, event):
        """Handle double click event"""
        tree_view: TreeView = self.tree_view_frame.table_frame.tree_view
        region = tree_view.identify_region(event.x, event.y)

        if region != "cell":
            return

        selected_iid = tree_view.focus()
        values = tree_view.item(selected_iid)["values"]

        self.navigate(subscreen_name="detailed_view", props=values)

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
            font=FONTS.get_font("paragraph")
        )
        search_bar_frame.man_search = Radiobutton(search_bar_frame,
            text="Manufacturer",
            value="man_name",
            variable=search_bar_frame.search_option,
            font=FONTS.get_font("paragraph")
        )

        search_bar_frame.entry = Entry(self.tree_view_frame.search_bar_frame, font=FONTS.get_font("paragraph"))
        search_bar_frame.button = Button(
            self.tree_view_frame.search_bar_frame, 
            lambda: print("search"), 
            "Search", 
            image="./images/search.png",
            background=COLORS.ACCENT,
            foreground="white",
            activebackground="white",
            activeforeground=COLORS.ACCENT,
            compound="right",
            font=FONTS.get_font("paragraph", bold=True)
        )
        search_bar_frame.button.pack(side="right", fill="y", pady=20, ipadx=14, ipady=2, padx=20)
        search_bar_frame.entry.pack(side="right", fill="y", pady=20, ipadx=10, ipady=5)
        search_bar_frame.part_number_search.pack(side="right", fill="y", pady=20, padx=20)
        search_bar_frame.man_search.pack(side="right", fill="y", pady=20)
        
        # Create scroll bar
        s = Style(table_frame)
        s.theme_use("alt")
        s.configure("custom.Vertical.TScrollbar", troughcolor=COLORS.WHITE, background=COLORS.ACCENT, arrowcolor="white", relief="flat")
        s.map("custom.Vertical.TScrollbar", background=[("active", COLORS.ACCENT)])

        scroll_bar = table_frame.scroll_bar = Scrollbar(table_frame, orient="vertical", style="custom.Vertical.TScrollbar")

        # Create the tree view
        tree_view = table_frame.tree_view = TreeView(
            table_frame, 
            columns=(
                "part_number", 
                "price", 
                "guarantee", 
                "manufacturer", 
                "inventory_date",
                "sub_category", 
                "stock"
            ),
            yscrollcommand=scroll_bar.set,
            style_name="comp.Treeview"
        )

        scroll_bar.config(command=tree_view.yview)

        # Apply the styles
        tree_view.config_styles(
            heading={
                "background": COLORS.WHITE,
                "foreground": "black",
                "font": FONTS.get_font("paragraph", bold=True),
            },
            row={
                "background": COLORS.WHITE,
                "foreground": "black",
                "font": FONTS.get_font("paragraph"),
                "rowheight": 34
            },
            selected={
                "background":  COLORS.ACCENT,
            }
        )
        
        tree_view.config_headings({
            "part_number": {"text": "Part number"},
            "price": {"text": "Price"},
            "guarantee": {"text": "Guarantee"},
            "manufacturer": {"text": "Manufacturer"},
            "inventory_date": {"text": "Inventory date"},
            "sub_category": {"text": "Subcategory"},
            "stock": {"text": "Stock"},
        })

        tree_view.config_columns({
            "part_number": {"anchor": "center"},
            "price": {"anchor": "center"},
            "guarantee": {"anchor": "center"},
            "manufacturer": {"anchor": "center"},
            "inventory_date": {"anchor": "center"},
            "sub_category": {"anchor": "center"},
            "stock": {"anchor": "center"},
        })

        tree_view.pack(side="left", fill="both", expand=True)
        scroll_bar.pack(side="left", fill="y")

        # Bind double click envent
        tree_view.bind("<Double-1>", self.on_double_click)

        for i in range(30):
            tree_view.insert(parent="", index="end", values=("SCD123AB", "0.3", str(i), "Samsung", "20/12/2020", "Controller", "3000"))

    def build_filters_frame(self):
        """Create the filters frame"""
        filters_frame = self.filters_frame

        # Config the grid
        filters_frame.columnconfigure(0, weight=1)
        filters_frame.columnconfigure(1, weight=2)
        filters_frame.rowconfigure(18, weight=1)

        # Filters label
        filters_frame.label = Label(
            filters_frame, 
            "FILTERS", 
            background="transparent", 
            foreground="white", 
            font=FONTS.get_font("heading2", bold=True)
        )
        self.filters_frame.label.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        # Inventory date filter
        filters_frame.inventory_date_label = Label(
            filters_frame, 
            text="Inventory date",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.inventory_date_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=5, padx=14)

        filters_frame.date_from_label = Label(filters_frame, 
            "From", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.date_from_label.grid(row=2, column=0, sticky="w", padx=14)

        filters_frame.date_from_entry = Entry(filters_frame)
        filters_frame.date_from_entry.grid(row=2, column=1, sticky="ew", padx=(0, 14))

        filters_frame.date_to_label = Label(filters_frame, 
            "To", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.date_to_label.grid(row=3, column=0, sticky="w", padx=14)

        filters_frame.date_to_entry = Entry(filters_frame)
        filters_frame.date_to_entry.grid(row=3, column=1, sticky="ew", padx=(0, 14))

        # Price filter
        filters_frame.price_label = Label(
            filters_frame, 
            text="Price",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.price_label.grid(row=4, column=0, columnspan=2, sticky="w", pady=5, padx=14)

        filters_frame.price_from_label = Label(filters_frame, 
            "From", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.price_from_label.grid(row=5, column=0, sticky="w", padx=14)

        filters_frame.price_from_entry = Entry(filters_frame)
        filters_frame.price_from_entry.grid(row=5, column=1, sticky="ew", padx=(0, 14))

        filters_frame.price_to_label = Label(filters_frame, 
            "To", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.price_to_label.grid(row=6, column=0, sticky="w", padx=14)

        filters_frame.price_to_entry = Entry(filters_frame)
        filters_frame.price_to_entry.grid(row=6, column=1, sticky="ew", padx=(0, 14))
        
        # Guarantee filter
        filters_frame.guarantee_label = Label(
            filters_frame, 
            text="Guarantee",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.guarantee_label.grid(row=7, column=0, columnspan=2,  sticky="w", pady=5, padx=14)

        filters_frame.guarantee_from_label = Label(filters_frame, 
            "From", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.guarantee_from_label.grid(row=8, column=0, sticky="w", padx=14)

        filters_frame.guarantee_from_entry = Entry(filters_frame)
        filters_frame.guarantee_from_entry.grid(row=8, column=1, sticky="ew", padx=(0, 14))

        filters_frame.guarantee_to_label = Label(filters_frame, 
            "To", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.guarantee_to_label.grid(row=9, column=0, sticky="w", padx=14)

        filters_frame.guarantee_to_entry = Entry(filters_frame)
        filters_frame.guarantee_to_entry.grid(row=9, column=1, sticky="ew", padx=(0, 14))

        # Stock filter
        filters_frame.stock_label = Label(
            filters_frame, 
            text="Stock",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left"
        )
        filters_frame.stock_label.grid(row=10, column=0, columnspan=2,  sticky="w", pady=5, padx=14)

        filters_frame.stock_from_label = Label(filters_frame, 
            "From", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.stock_from_label.grid(row=11, column=0, sticky="w", padx=14)

        filters_frame.stock_from_entry = Entry(filters_frame)
        filters_frame.stock_from_entry.grid(row=11, column=1, sticky="ew", padx=(0, 14))

        filters_frame.stock_to_label = Label(filters_frame, 
            "To", 
            background="transparent", 
            foreground="white",
            font=FONTS.get_font("paragraph", italic=True)
        )
        filters_frame.stock_to_label.grid(row=12, column=0, sticky="w", padx=14)

        filters_frame.stock_to_entry = Entry(filters_frame)
        filters_frame.stock_to_entry.grid(row=12, column=1, sticky="ew", padx=(0, 14))

        # Subcategory filter
        subcategories_button = filters_frame.subcategories_button = Menubutton(
            filters_frame, 
            text="Subcategory",
            background=COLORS.SECONDARY,
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True),
            justify="left",
            activeforeground=COLORS.ACCENT
        )
        filters_frame.subcategories_button.grid(row=14, column=0, columnspan=2,  sticky="w", pady=5, padx=14)

        subcategories_button.menu = Menu(subcategories_button, tearoff=False)
        self.states["menu_options"] = []
        def toggle_option(option):
            if option in self.states["menu_options"]:
                self.states["menu_options"].remove(option)
            else:
                self.states["menu_options"].append(option)
            print(self.states["menu_options"])
        
    
        subcategories_button.menu.option_a = BooleanVar(False)
        subcategories_button.menu.option_b = BooleanVar(False)
        subcategories_button.menu.option_c = BooleanVar(False)
        subcategories_button.menu.add_checkbutton(
            label="A", 
            onvalue=True, 
            offvalue=False, 
            variable=subcategories_button.menu.option_a, 
            command= lambda: toggle_option("A"),
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        subcategories_button.menu.add_checkbutton(
            label="B", 
            onvalue=True, 
            offvalue=False, 
            variable=subcategories_button.menu.option_b, 
            command= lambda: toggle_option("B"),
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        subcategories_button.menu.add_checkbutton(
            label="C", 
            onvalue=True, 
            offvalue=False, 
            variable=subcategories_button.menu.option_c, 
            command= lambda: toggle_option("C"),
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        subcategories_button.configure(menu=subcategories_button.menu)

        def get_all_filter():
            pass
        filters_frame.apply_button = Button(filters_frame,
            text="Apply",
            command=get_all_filter,
            background=COLORS.ACCENT,
            foreground="white",
            activebackground="white",
            activeforeground=COLORS.ACCENT,
            font=FONTS.get_font("paragraph", bold=True)
        )

        filters_frame.apply_button.grid(row=18, column=0, columnspan=2, ipady=4, padx=14, sticky="ew")
