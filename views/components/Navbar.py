from gui import Navbar as guiNav
from constants import COLORS, FONTS

class Navbar(guiNav):
    """App's navbar"""
    def __init__(self,
            master,
            links: list[tuple[str, str]], 
            redirect_funtion
        ):
        """Init the navbar"""
        super().__init__(master, links,
            COLORS.NEUTRAL_RED, COLORS.WHITE, 
            redirect_funtion,
            font=FONTS.get_font("paragraph")
        )