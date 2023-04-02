from ...gui import Screen, Frame, Button, SubScreen
from ...constants import COLORS, FONTS
from .ComponentListView import ComponentListView
from .ComponentDetailedView import ComponentDetailedView

class ComponentScreen(Screen):
    """Component screen
    
    Display information about the electric components
    """
    def __init__(self, master, app_controller):
        """Init screen"""
        super().__init__(master,
            title="Components",
            title_font=FONTS.get_font("heading1", bold=True),
            back_font=FONTS.get_font("paragraph", italic=True)
        )

        self.add_subscreen("component_main", SubScreen(self.main_frame, render_function=self.render_main))
        self.add_subscreen("list_view", 
            ComponentListView(self.main_frame,
                navigation_function=self.navigate_subscreen,
                app_controller=app_controller
            )
        )
        self.add_subscreen("detailed_view", ComponentDetailedView(self.main_frame, app_controller))
        
        self.navigate_subscreen("component_main")

    def render_main(self, subscreen: SubScreen, props=None):

        # Create component frame
        subscreen.content_frame = Frame(subscreen, background="transparent")
        subscreen.content_frame.pack(anchor="center", fill="both", expand=True)

        # Configure grid
        subscreen.content_frame.rowconfigure(0, weight=1)
        subscreen.content_frame.rowconfigure(1, weight=1)
        subscreen.content_frame.columnconfigure(0, weight=1)
        subscreen.content_frame.columnconfigure(1, weight=1)
        subscreen.content_frame.columnconfigure(2, weight=1)

        # Create frames
        subscreen.box1 = Frame(subscreen.content_frame, background=COLORS.WHITE)
        subscreen.box2 = Frame(subscreen.content_frame, background=COLORS.WHITE)
        subscreen.box3 = Frame(subscreen.content_frame, background=COLORS.WHITE)
        subscreen.box4 = Frame(subscreen.content_frame, background=COLORS.WHITE)
        subscreen.box5 = Frame(subscreen.content_frame, background=COLORS.WHITE)

        # Place frames
        subscreen.box1.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        subscreen.box4.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        subscreen.box2.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=20, pady=20)
        subscreen.box3.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        subscreen.box5.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        
        # Make box take the full width and height
        subscreen.box1.pack_propagate(False)
        subscreen.box2.pack_propagate(False)
        subscreen.box3.pack_propagate(False)
        subscreen.box4.pack_propagate(False)
        subscreen.box5.pack_propagate(False)

        # Add images
        subscreen.capcitor_img = Button(
            subscreen.box1,
            lambda: self.navigate_subscreen("list_view", {"selected": "capacitor"}),
            text="Capacitor",
            image="./images/capacitor.png",
            background="transparent",
            compound="top",
            font=FONTS.get_font("heading3", bold=True),
            activebackground=COLORS.SECONDARY
        )
        subscreen.capcitor_img.pack(fill="both", expand=True, anchor="s")

        subscreen.ic_img = Button(
            subscreen.box2,
            lambda: self.navigate_subscreen("list_view", {"selected": "ic"}),
            text="IC",
            image="./images/ic.png",
            background="transparent",
            compound="top",
            font=FONTS.get_font("heading3", bold=True),
            activebackground=COLORS.SECONDARY
        )
        subscreen.ic_img.pack(fill="both", expand=True, anchor="s")

        subscreen.inductor_img = Button(
            subscreen.box3,
            lambda: self.navigate_subscreen("list_view", {"selected": "inductor"}),
            text="Inductor",
            image="./images/inductor.png",
            background="transparent",
            compound="top",
            font=FONTS.get_font("heading3", bold=True),
            activebackground=COLORS.SECONDARY
        )
        subscreen.inductor_img.pack(fill="both", expand=True, anchor="s")

        subscreen.resistor_img = Button(
            subscreen.box4,
            lambda: self.navigate_subscreen("list_view", {"selected": "resistor"}),
            text="Resistor",
            image="./images/resistor.png",
            background="transparent",
            compound="top",
            font=FONTS.get_font("heading3", bold=True),
            activebackground=COLORS.SECONDARY
        )
        subscreen.resistor_img.pack(fill="both", expand=True, anchor="s")

        subscreen.sensor_img = Button(
            subscreen.box5,
            lambda: self.navigate_subscreen("list_view", {"selected": "sensor"}),
            text="Sensor",
            image="./images/sensor.png",
            background="transparent",
            compound="top",
            font=FONTS.get_font("heading3", bold=True),
            activebackground=COLORS.SECONDARY
        )
        subscreen.sensor_img.pack(fill="both", expand=True, anchor="s")

        subscreen.widgets_to_destroy.append(subscreen.content_frame)