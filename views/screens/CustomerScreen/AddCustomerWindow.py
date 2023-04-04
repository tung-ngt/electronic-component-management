from tkinter import Toplevel, Entry, StringVar, Menu, Menubutton, messagebox
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton

class AddCustomerWindow:
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
        self.screen.title("Add a customer")
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
            "Add a customer",
            background=COLORS.WHITE,
            font=FONTS.get_font("heading1", bold=True),
        )
        man_label.pack(pady=30)

        form_frame = Frame(self.screen, background=COLORS.PRIMARY)
        form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Config the grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.rowconfigure(6, weight=1)

        man_id_label = Label(
            form_frame,
            "Customer's ID",
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
        
        phone_number_label = Label(
            form_frame,
            "Phone number",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.phone_number_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        phone_number_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=(34,14), pady=(14,5))
        self.phone_number_entry.grid(row=5, column=0, columnspan=2, sticky="ew", padx=(34,14), ipady=4)
        
        add_button = AccentButton(
            form_frame, 
            command=self.submit, 
            text="Add",
        )

        add_button.grid(row=6, column=0, sticky="w",padx=34, pady=34, ipadx=20)

    def submit(self):
        """Submit the form"""
        data = {
            "id": self.man_id_entry.get(),
            "name": self.name_entry.get(),
            "phone_number": self.phone_number_entry.get()
        }
        try:
            self.app_controller.add_customer(data)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Successfull", "Add customer was suscessfull")