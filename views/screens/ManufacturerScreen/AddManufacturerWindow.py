from tkinter import Toplevel, Entry
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton

class AddManufacturerWindow:
    """This is a pop up window to add a student"""
    def __init__(self, master, values=None):
        """Create the window
        
        Parameters
        ----------
        master : master widget
        values : initial values of the window
        """
        # Window settings
        self.screen = Toplevel(master)
        self.values = values
        if values == None:
            self.screen.title("Add a manufacturer")
        else:
            self.screen.title("Update manufacturer")
        # self.screen.grab_set()
        self.screen.geometry("1200x800+0+0")
        self.screen.minsize(1000, 700)
        self.screen["background"] = COLORS.WHITE

        self.create_form()

    def create_form(self):
        """Create component information form"""
        man_label = Label(
            self.screen,
            "Add a manufacturer" if self.values==None else "Update manufacturer",
            background=COLORS.WHITE,
            font=FONTS.get_font("heading1", bold=True),
        )
        man_label.pack(pady=30)

        form_frame = Frame(self.screen, background=COLORS.PRIMARY)
        form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Config the grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)
        form_frame.rowconfigure(4, weight=1)

        man_id_label = Label(
            form_frame,
            "Mannufacturer ID",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        man_id_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        man_id_label.grid(row=0, column=0, sticky="w", padx=(34,14), pady=(34,5))
        man_id_entry.grid(row=1, column=0, sticky="ew", padx=(34,14), ipady=4)
        
        name_label = Label(
            form_frame,
            "Name",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        name_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        name_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=(34,14), pady=(14,5))
        name_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=(34,14), ipady=4)
        
        country_label = Label(
            form_frame,
            "Country",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        country_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        country_label.grid(row=0, column=1, sticky="w", padx=(34,14), pady=(14,5))
        country_entry.grid(row=1, column=1, sticky="ew", padx=(34,14), ipady=4)

        add_button = AccentButton(
            form_frame, 
            command=lambda: print("hello"), 
            text="Add",
        )

        add_button.grid(row=4, column=0, sticky="w",padx=34, pady=34, ipadx=20)