from tkinter.font import Font
from copy import deepcopy

class Typography:
    """Typography is use to store configurations about fonts, types, ..."""
    __root = None
    __fonts: dict[str, dict[str, Font]] = {}
   
    @staticmethod
    def init_typography(win):
        """Set typography root"""
        Typography.__root = win
        Typography.__default_fonts: dict[str, Font] = {
            "paragraph": Font(Typography.__root,
                family= "Times New Roman",
                size= 16,
            ),
            "heading1": Font(Typography.__root,
                family= "Times New Roman",
                size= 48
            ),
            "heading2": Font(Typography.__root,
                family= "Times New Roman",
                size= 32
            ),
            "heading3": Font(Typography.__root,
                family= "Times New Roman",
                size= 24,
            )
        }
        Typography.__create_variations(Typography.__default_fonts)
        
            
    @staticmethod
    def __create_variations(fonts: dict[str, Font]):
        for name, font in list(fonts.items()):
            variations = {}
            for w in ["normal", "bold"]:
                for s in ["roman", "italic"]:
                    v = font.copy()
                    v.config(weight=w, slant=s)
                    variations[w+s] = v
            Typography.__fonts[name] = variations

    @staticmethod
    def get_font(font_type, bold=False, italic=False):
        """Return the fonts
        
        Parameters
        ----------
        font_type : can be (paragraph, heading1, heading2, heading3)
        bold : default False
        italic : default False
        """
        variation = ("bold" if bold else "normal") + ("italic" if italic else "roman")
        if font_type in Typography.__fonts.keys():
            return Typography.__fonts[font_type][variation]

    @staticmethod
    def set_fonts(fonts: dict):
        """Set up font
        
        Parameters:
        font : {name : {family, size}}
        """
        font_data = {}
        for name, font in list(fonts.items()):
                font_data[name] = Font(Typography.__root, family=font["family"], size=font["size"])
        Typography.__create_variations(font_data)