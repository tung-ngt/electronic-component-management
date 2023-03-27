from tkinter import EW
from tkinter.font import Font
from .Frame import Frame
from .Label import Label
from .Button import Button

class Navbar(Frame):
    """Represent a Navbar"""
    def __init__(self,
            master, 
            links: list[tuple[str, str]], 
            background="black", 
            text_color="white", 
            redirect_funtion=lambda screen_name: print(screen_name),
            font: Font = None,
        ):
        """Init the Nabar
        
        Parameters
        ----------
        master : master widget,
        background : navbar background color
        links : list of tuple of screen name and text [(name, text)]
        text_color : default black,
        redirect_funtion : funtion to change screen
        font : a tk Font for link text
        """
        super().__init__(master, background=background)
        self.text_font = font
        self.text_color = text_color
        self.background = background
        self.links = links
        self.redirect_function = redirect_funtion
        self.link_widgets: list[Label] = []
        self.__create_links()
        self.grid_columnconfigure(0, weight=1)
    
    def __create_logo(self, logo_path: str, name: str):
        """Create and place the logo on top of the navbar
        
        Parameters
        ----------
        logo_path : path to the logo
        name : name of the app
        """

    def __create_links(self):
        """Create links and place them on the navbar"""

        # Get redirect call back function for a screen
        def get_redirect_fun(screen_name: str):
            local_name = screen_name
            def redirect():
                self.redirect_function(local_name)
            return redirect
        
        # Loop over the links and render them
        for i, (screen_name, text) in enumerate(self.links):
            redirect = get_redirect_fun(screen_name)
            link_widget = Button(
                self, 
                command=redirect,
                text=text, 
                background=self.background, 
                foreground=self.text_color,
                activebackground= self.text_color,
                activeforeground=self.background,
                font=self.text_font,
                borderwidth=0
            )
            link_widget.grid(row=i+1, column=0, sticky=EW, padx=10, pady=3)
            self.link_widgets.append(link_widget)