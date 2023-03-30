from ...gui import Screen, SubScreen, Label, Frame, TreeView, Button
from ...constants import COLORS, FONTS
from .ManufacturerDetailedView import ManufacturerDetailedView
from tkinter import Entry, BooleanVar
from tkinter.ttk import Style, Scrollbar
class ManufacturerScreen(Screen):
    """App's main screen"""
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, background=COLORS.SECONDARY,
            title="Manufacturer",
            title_font=FONTS.get_font("heading1", bold=True)
        )

        self.add_subscreen("manufacturer_main", SubScreen(self.main_frame,
            render_function=self.render_manufacturer,
            title_bar_foreground="white"
        ))
        self.add_subscreen("detailed_view", ManufacturerDetailedView(self.main_frame))
        self.navigate_subscreen("manufacturer_main")

    
    def render_manufacturer(self, subscreen, props=None):
        # Initialize tree view frame and filter frame
        subscreen.tree_view_frame = Frame(subscreen, background=COLORS.WHITE)
        
        # Make the frame take up the hold space

        # Config the grid
        subscreen.grid_columnconfigure(0, weight=1)
        subscreen.grid_rowconfigure(0, weight=1)

        subscreen.tree_view_frame.grid(row=0, column=0, sticky="nsew")

        # Build the tree view
        self.build_tree_view(subscreen)

        # Specify the widget to destroy
        subscreen.add_widgets_to_destroy([subscreen.tree_view_frame])

    def on_double_click(self, subscreen, event):
        """Handle double click event"""
        tree_view: TreeView = subscreen.tree_view_frame.table_frame.tree_view
        region = tree_view.identify_region(event.x, event.y)

        if region != "cell":
            return

        selected_iid = tree_view.focus()
        values = tree_view.item(selected_iid)["values"]

        self.navigate_subscreen(subscreen_name="detailed_view", props=values)

    def build_tree_view(self, subscreen):
        """Build the component tree view table"""
        # Crate search bar and table frame
        search_bar_frame = subscreen.tree_view_frame.search_bar_frame = Frame(subscreen.tree_view_frame, background="transparent")
        table_frame = subscreen.tree_view_frame.table_frame = Frame(subscreen.tree_view_frame, background="transparent")

        search_bar_frame.pack(fill="x")
        table_frame.pack(fill="both", expand=True)
 
        # Search bar
        search_bar_frame.entry = Entry(subscreen.tree_view_frame.search_bar_frame, font=FONTS.get_font("paragraph"))
        search_bar_frame.button = Button(
            subscreen.tree_view_frame.search_bar_frame, 
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
        s.configure("custom.Vertical.TScrollbar", troughcolor=COLORS.WHITE, background=COLORS.ACCENT, arrowcolor="white", relief="flat")
        s.map("custom.Vertical.TScrollbar", background=[("active", COLORS.ACCENT)])

        scroll_bar = table_frame.scroll_bar = Scrollbar(table_frame, orient="vertical", style="custom.Vertical.TScrollbar")

        # Create the tree view
        tree_view = table_frame.tree_view = TreeView(
            table_frame, 
            columns=(
                "id", 
                "name", 
                "country", 
            ),
            yscrollcommand=scroll_bar.set,
            style_name="man.Treeview"
        )

        scroll_bar.config(command=tree_view.yview)

        # Apply the styles
        tree_view.config_styles(
            heading={
                "background": COLORS.WHITE,
                "foreground": COLORS.ACCENT,
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
            "id": {"text": "ID"},
            "name": {"text": "Name"},
            "country": {"text": "Country"},
        })

        tree_view.config_columns({
            "id": {"anchor": "center"},
            "name": {"anchor": "center"},
            "country": {"anchor": "center"},
        })

        tree_view.pack(side="left", fill="both", expand=True)
        scroll_bar.pack(side="left", fill="y")

        # Bind double click envent
        tree_view.bind("<Double-1>", lambda e: self.on_double_click(subscreen, e))

        for i in range(30):
            tree_view.insert(parent="", index="end", values=(f"SCD123AB{i}", f"Samsung{i}", f"Korea{i}"))