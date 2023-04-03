from tkinter import Toplevel, Entry, StringVar, Menu, Menubutton, messagebox
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton

class AddManufacturerWindow:
    """This is a pop up window to add a student"""
    def __init__(self, master, 
        app_controller, 
        on_close_fun = None,):
        """Create the window
        
        Parameters
        ----------
        master : master widget
        on_close_fun : function to run when closing window
        """
        # Window settings
        self.screen = Toplevel(master)
        self.screen.title("Add a manufacturer")
        self.screen.grab_set()

        self.screen.geometry("1200x800+0+0")
        self.screen.minsize(1000, 700)
        self.screen["background"] = COLORS.WHITE
        self.app_controller = app_controller
        self.on_close_fun = self.get_on_close_fun(on_close_fun)
        if self.on_close_fun != None:
            self.screen.protocol("WM_DELETE_WINDOW", self.on_close_fun)

        self.create_form()

    def get_on_close_fun(self, on_close_fun):
        def close():
            self.screen.destroy()
            on_close_fun()
        return close

    def create_form(self):
        """Create component information form"""
        man_label = Label(
            self.screen,
            "Add a manufacturer",
            background=COLORS.WHITE,
            font=FONTS.get_font("heading1", bold=True),
        )
        man_label.pack(pady=30)

        form_frame = Frame(self.screen, background=COLORS.PRIMARY)
        form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Config the grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.rowconfigure(5, weight=1)

        man_id_label = Label(
            form_frame,
            "Mannufacturer ID",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.man_id_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        man_id_label.grid(row=0, column=0, sticky="w", padx=(34,14), pady=(34,5))
        self.man_id_entry.grid(row=1, column=0, sticky="ew", padx=(34,14), ipady=4)
        
        name_label = Label(
            form_frame,
            "Name",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.name_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        name_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=(34,14), pady=(14,5))
        self.name_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=(34,14), ipady=4)
        
        country_frame = Frame(form_frame, background="transparent")
        country_label = Label(
            country_frame,
            "Sensor type",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.country = StringVar()
        self.country.set("None")
        country_options = self.app_controller.get_mnf_countries()
        country_button = Menubutton(
            country_frame,
            textvariable=self.country,
            background="white", 
            relief="flat", 
            borderwidth=0, 
            highlightthickness=0,
            font=FONTS.get_font("paragraph"),
        )
        country_menu = Menu(
            country_button,
            tearoff=False,
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        country_button.config(menu=country_menu)
        for option in country_options:
            def get_option(op):
                return lambda: self.country.set(op)
            country_menu.add_command(label=option, command=get_option(option))
        
        country_label.pack(anchor="w", padx=34, pady=(34,5))
        country_button.pack(fill="x", padx=34, ipady=2)
        country_frame.grid(row=4, column=0, sticky="ew")

        add_button = AccentButton(
            form_frame, 
            command=self.submit, 
            text="Add",
        )

        add_button.grid(row=5, column=0, sticky="w",padx=34, pady=34, ipadx=20)

    def submit(self):
        """Submit the form"""
        data = {
            "id": self.man_id_entry.get(),
            "name": self.name_entry.get(),
            "country": self.country.get()
        }
        try:
            self.app_controller.add_manufacturer(data)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Successfull", "Add component was suscessfull")