import tkinter as tk
from tkinter.font import Font as tkFont
import os
from .Screen import Screen
from .Navbar import Navbar
from .Label import Label
from .Typography import Typography
class GUI:
    """GUI app class"""
    def __init__(self, 
            title, 
            geometry="800x600", 
            resizable=(True, True),
            fullscreen=False,
            min_size=(0,0), 
            icon=None,
            fonts = {}
        ):
        """Init gui
        
        Parameters
        ----------
        title : title of the window
        geometry : initial geometry of the window string "{width}x{height}" default "800x600"
        resizable : if the window can change size (width, height) default (False, False)
        fullscreen : bool if the app is fullscreen (default False)
        min_size : (width: int, height: int)
        icon : path to icon default None
        fonts : fonts that is used in the app
        """
        self.root_window = tk.Tk()
        self.root_window.title(title)
        if fullscreen:
            self.root_window.state("zoomed")
            self.root_window.resizable(True, True)
        else:
            self.root_window.geometry(geometry)
            self.root_window.resizable(resizable[0], resizable[1])
            self.root_window.minsize(min_size[0], min_size[0])
        if os.path.isfile(icon):
            self.root_window.iconphoto(True, tk.PhotoImage(file=icon))

        Typography.init_typography(self.root_window)
        Typography.set_fonts(fonts)
        self.root_window.grid_rowconfigure(0, weight=1)
        self.root_window.grid_columnconfigure(0, weight=1, minsize=150)
        self.root_window.grid_columnconfigure(1, weight=9)
        self.screens: dict[str, Screen] = {}
        self.current_screen: str = None

    def init_navbar(self, navbar: Navbar):
        """Add navbar and place it in root window"""    
        self.navbar = navbar
        self.navbar.grid(row=0,column=0, sticky=tk.NSEW)

    def add_screen(self, screen_name: str, screen: Screen):
        """Add screen to the app
        
        Parameters
        ----------
        screen_name : name of the screen,
        screen : the screen
        """
        self.screens[screen_name] = screen

    def change_screen(self, screen_name: str):
        """Change screen to a specified screen"""
        self.hide_screen(self.current_screen)
        self.show_screen(screen_name)

    def hide_screen(self, screen_name: str):
        """Hide a screen"""
        self.screens[screen_name].grid_forget()
    
    def show_screen(self, screen_name: str):
        """Show a screen"""
        self.screens[screen_name].grid(row=0, column=1, sticky=tk.NSEW)
        self.current_screen = screen_name

    def main_loop(self):
        """Call main loop of the program"""
        self.root_window.mainloop()

    def quit(self):
        """Quit the gui"""
        self.root_window.quit()
