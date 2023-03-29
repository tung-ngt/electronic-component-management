from ..gui import Navbar as guiNav
from ..constants import COLORS, FONTS
from tkinter.font import Font as tkFont

class Navbar(guiNav):
    """App's navbar"""
    def __init__(self,
            master,
            links: list[tuple[str, str]], 
            redirect_funtion,
            logo: dict[str, str or tkFont]
        ):
        """Init the navbar"""
        super().__init__(master, links,
            COLORS.PRIMARY, COLORS.WHITE, 
            redirect_funtion,
            font=FONTS.get_font("paragraph", bold=True),
            logo=logo
        )