from ...gui import Screen, Frame, Button, SubScreen
from ...constants import COLORS, FONTS
from .OrderListView import OrderListView
from .OrderDetailedView import OrderDetailedView

class OrderScreen(Screen):
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

        self.add_subscreen("list_view", 
            OrderListView(self.main_frame,
                navigation_function=self.navigate_subscreen,
                app_controller=app_controller
            )
        )
        self.add_subscreen("detailed_view", OrderDetailedView(self.main_frame, app_controller))
        self.navigate_subscreen("list_view")