from gui import SubScreen, Label, Frame, Button, TreeView
from tkinter import Entry
from tkinter.ttk import Scrollbar, Style
from constants import COLORS, FONTS

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
        self.filters_frame = Frame(self, background=COLORS.SECONDARY)
        
        # Make the frame take up the hold space
        self.tree_view_frame.pack_propagate(False)
        self.tree_view_frame.grid_propagate(False)

        # Config the grid
        self.grid_columnconfigure(0, weight=9)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tree_view_frame.grid(row=0, column=0, sticky="nsew")
        self.filters_frame.grid(row=0, column=1, sticky="nsew")

        # Build the tree view
        self.build_tree_view()

        self.filters_frame.label = Label(
            self.filters_frame, 
            "FILTERS", 
            background="transparent", 
            foreground="white", 
            font=FONTS.get_font("heading2", bold=True)
        )

        self.filters_frame.label.pack(pady=20)

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
        
        # Create scroll bar
        s = Style(table_frame)
        s.theme_use("alt")
        s.configure("arrowless.Vertical.TScrollbar", thumbcolor=COLORS.BACKGROUND_LIGHT, troughtcolor=COLORS.WHITE, background=COLORS.ACCENT)
        scroll_bar = table_frame.scroll_bar = Scrollbar(table_frame, orient="vertical", style="arrowless.Vertical.TScrollbar")

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
            yscrollcommand=scroll_bar.set
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
            selecteđ={
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