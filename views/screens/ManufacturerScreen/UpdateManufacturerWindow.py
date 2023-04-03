from tkinter import Toplevel, Entry, StringVar, Menu, Menubutton, messagebox
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton

class UpdateManufacturerWindow:
    """This is a pop up window to add a student"""
    def __init__(self,
            master, 
            app_controller, 
            initial_values,
            on_close_fun = None,
        ):
        """Create the window
        
        Parameters
        ----------
        master : master widget
        app_controller : app controller
        initial_values : initial values of the component
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
        self.initial_values = initial_values
        self.on_close_fun = on_close_fun

        self.create_form()

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
        self.man_id_entry.insert(0, self.initial_values[0])
        self.man_id_entry.config(state="disabled")
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
        self.name_entry.insert(0, self.initial_values[1])
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
        self.country.set(self.initial_values[2])
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
            text="Update",
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
            self.app_controller.update_manufacturer(data, data["id"])
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Successfull", "Add component was suscessfull")
            updated_values = list(data.values())
            self.screen.destroy()
            self.on_close_fun(updated_values)