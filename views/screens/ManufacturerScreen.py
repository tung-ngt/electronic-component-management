from ..gui import Screen, SubScreen, Label
from ..constants import COLORS, FONTS

class ManufacturerScreen(Screen):
    """App's main screen"""
    def __init__(self, master):
        """Init screen"""
        super().__init__(master, background=COLORS.SECONDARY,
            title="Manufacturer",
            title_font=FONTS.get_font("heading1", bold=True)
        )

        self.add_subscreen("manufacturer_main", SubScreen(self.main_frame, render_function=self.render_manufacturer))
        self.navigate_subscreen("manufacturer_main")

    
    def render_manufacturer(self, subscreen, props=None):
        subscreen.man_label = Label(subscreen, text="This is a manu")
        subscreen.man_label.pack()