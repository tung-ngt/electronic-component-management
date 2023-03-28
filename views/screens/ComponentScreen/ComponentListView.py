from gui import SubScreen, Label
from constants import COLORS

class ComponentListView(SubScreen):
    def __init__(self, master):
        super().__init__(master, background=COLORS.WHITE)

    # Override render method
    def render(self, props=None):
        super().render()
        self.title = props["selected"].capitalize()
        self.label = Label(self, text=props["selected"], background="transparent")
        self.label.pack()

        self.widgets_to_destroy.append(self.label)