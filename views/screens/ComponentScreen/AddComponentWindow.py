from tkinter import Toplevel, Entry, StringVar, Menubutton, Menu
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton

class AddComponentWindow:
    """This is a pop up window to add a student"""
    def __init__(self, master, component_type: str):
        """Create the window
        
        Parameters
        ----------
        master : master widget
        component_type : type of component to add
        """
        # Window settings
        self.component_type = component_type
        self.screen = Toplevel(master)
        self.screen.title("Add a component")
        # self.screen.grab_set()
        self.screen.geometry("1200x800+0+0")
        self.screen.minsize(1000, 700)
        self.screen["background"] = COLORS.WHITE

        self.create_form()

    def create_form(self):
        """Create component information form"""
        component_label = Label(
            self.screen,
            self.component_type.capitalize(),
            background=COLORS.WHITE,
            font=FONTS.get_font("heading1", bold=True),
            image=f"./images/{self.component_type}.png",
            compound="right"
        )
        component_label.pack(pady=30)

        form_frame = Frame(self.screen, background=COLORS.PRIMARY)
        form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Config the grid
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)
        form_frame.columnconfigure(2, weight=1)
        form_frame.rowconfigure(6, weight=1)

        part_number_label = Label(
            form_frame,
            "Part number",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        part_number_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        part_number_label.grid(row=0, column=0, sticky="w", padx=(34,14), pady=(34,5))
        part_number_entry.grid(row=1, column=0, sticky="ew", padx=(34,14), ipady=4)
        
        price_label = Label(
            form_frame,
            "Price",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        price_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        price_label.grid(row=2, column=0, sticky="w", padx=(34,14), pady=(14,5))
        price_entry.grid(row=3, column=0, sticky="ew", padx=(34,14), ipady=4)
        
        guarantee_label = Label(
            form_frame,
            "Guarantee (months)",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        guarantee_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        guarantee_label.grid(row=4, column=0, sticky="w", padx=(34,14), pady=(14,5))
        guarantee_entry.grid(row=5, column=0, sticky="ew", padx=(34,14), ipady=4)
        
        stock_label = Label(
            form_frame,
            "Stock",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        stock_entry = Entry(form_frame, font=FONTS.get_font("paragraph"))
        stock_label.grid(row=0, column=1, sticky="w", padx=14, pady=(34,5))
        stock_entry.grid(row=1, column=1, sticky="ew", padx=14, ipady=4)

        manu_label = Label(
            form_frame,
            "Manufacturer",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        man_option = StringVar()
        man_option.set("None")
        man_options = ["None", "Samsung", "LG"]
        man_button = Menubutton(
            form_frame,
            textvariable=man_option,
            background="white", 
            relief="flat", 
            borderwidth=0, 
            highlightthickness=0,
            font=FONTS.get_font("paragraph"),
        )
        man_menu = Menu(
            man_button,
            tearoff=False,
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        man_button.config(menu=man_menu)
        for option in man_options:
            def get_option(op):
                return lambda: man_option.set(op)
            man_menu.add_command(label=option, command=get_option(option))
        manu_label.grid(row=2, column=1, sticky="w", padx=14, pady=(14,5))
        man_button.grid(row=3, column=1, sticky="ew", padx=14, ipady=2)
        
        subcategory_label = Label(
            form_frame,
            "Manufacturer",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        subcategory_option = StringVar()
        subcategory_option.set("None")
        subcategory_options = ["None", "Samsung", "LG"]
        subcategory_button = Menubutton(
            form_frame,
            textvariable=subcategory_option,
            background="white", 
            relief="flat", 
            borderwidth=0, 
            highlightthickness=0,
            font=FONTS.get_font("paragraph"),
        )
        subcategory_menu = Menu(
            subcategory_button,
            tearoff=False,
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        subcategory_button.config(menu=subcategory_menu)
        for option in subcategory_options:
            def get_option(op):
                return lambda: subcategory_option.set(op)
            subcategory_menu.add_command(label=option, command=get_option(option))
        subcategory_label.grid(row=4, column=1, sticky="w", padx=14, pady=(14,5))
        subcategory_button.grid(row=5, column=1, sticky="ew", padx=14, ipady=2)

        date_label = Label(
            form_frame,
            "Inventory date",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        def validate_date(date):
            print(date)
            return True
        
        validate_function = (form_frame.register(validate_date), "%P")
        date_entry = Entry(
            form_frame,
            font=FONTS.get_font("paragraph"),
            validate="focusout", 
            validatecommand=validate_function
        )
        date_label.grid(row=0, column=2, sticky="w", padx=(14, 34), pady=(34,5))
        date_entry.grid(row=1, column=2, sticky="ew", padx=(14, 34), ipady=4)

        add_button = AccentButton(
            form_frame, 
            command=lambda: print("hello"), 
            text="Add",
        )

        add_button.grid(row=6, column=0, sticky="w",padx=34, pady=34, ipadx=20)