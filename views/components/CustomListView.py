from ..gui import TreeView
from ..constants import COLORS, FONTS

class CustomListView(TreeView):
    """Custom list view to show components and manufacturer"""
    def __init__(self, master, columns: tuple[str], yscrollcommand=None):
        """Init the List view
        
        Parameters
        ----------
        master : master widget
        columns : the tuple of columns in the list
        yscrollcommand : scrollbar command
        """
        super().__init__(master, columns, "browse", "headings", yscrollcommand, "custom.Treeview")
        self.config_styles(
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

    def add_item(self, values: tuple[str]):
        """Add a item to a row in the list
        
        Paramters
        ---------
        values : values in the row
        """
        self.insert(parent="", index="end", values=values)

    def create_items_from_list(self, list_of_items: list[tuple[str]]):
        """Add items to rows in the list
        
        Paramters
        ---------
        list_of_items : list of values tuples in the rows
        """
        for item in list_of_items:
            self.add_item(item)