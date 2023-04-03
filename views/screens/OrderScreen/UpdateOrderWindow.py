from tkinter import Toplevel, Entry, StringVar, Menubutton, Menu, messagebox
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton
from re import match

class UpdateOrderWindow:
    """This is a pop up window to add a student"""
    def __init__(self,
            master,
            component_type: str,
            app_controller, 
            initial_values,
            on_close_fun = None,
        ):
        """Create the window
        
        Parameters
        ----------
        master : master widget
        component_type : type of component to add
        app_controller : app controller
        initial_values : initial values of the component
        on_close_fun : function to run when closing window
        """
        # Window settings
        self.component_type = component_type
        self.screen = Toplevel(master)
        self.screen.title("Add a component")
        # self.screen.grab_set()
        self.screen.geometry("1200x800+0+0")
        self.screen.minsize(1000, 700)
        self.screen["background"] = COLORS.WHITE
        self.screen.grab_set()
        self.on_close_fun = on_close_fun

        self.app_controller = app_controller
        self.manufacturer_options = self.get_all_manufacturers_ids()
        self.subcategory_options = self.app_controller.get_sub_categories(self.component_type)
        self.initial_values = initial_values
        self.create_form()

    def get_all_manufacturers_ids(self):
        manufacturers = self.app_controller.get_manufacturers()
        manufacturers_ids = {}
        for manufacturer in manufacturers:
            manufacturers_ids[manufacturer.get_id()] = manufacturer.get_name()
        return manufacturers_ids

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

        self.form_frame = Frame(self.screen, background=COLORS.PRIMARY)
        self.form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Config the grid
        self.form_frame.columnconfigure(0, weight=1)
        self.form_frame.columnconfigure(1, weight=1)
        self.form_frame.columnconfigure(2, weight=1)
        self.form_frame.rowconfigure(3, weight=1)

        part_number_frame, self.part_number_entry = self.create_input_label("Part number", self.initial_values[0])
        part_number_frame.grid(row=0, column=0, sticky="ew")
        self.part_number_entry.config(state="disabled")
        
        price_frame, self.price_entry = self.create_input_label("Price", self.initial_values[1])
        price_frame.grid(row=1, column=0, sticky="ew")
        
        guarantee_frame, self.guarantee_entry = self.create_input_label("Guarantee (months)", self.initial_values[2])
        guarantee_frame.grid(row=2, column=0, sticky="ew")
        
        stock_frame, self.stock_entry = self.create_input_label("Stock", self.initial_values[6])
        stock_frame.grid(row=0, column=1, sticky="ew")

        # Create manufacturers option menu
        manu_frame = Frame(self.form_frame, background="transparent")
        manu_label = Label(
            manu_frame,
            "Manufacturer",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.man_option = StringVar()
        self.man_option.set(self.initial_values[3].split(")")[1:])
        self.man_label_option = StringVar()
        self.man_label_option.set(self.initial_values[3])
        man_button = Menubutton(
            manu_frame,
            textvariable=self.man_label_option,
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
        for man_id, man_name in list(self.manufacturer_options.items()):
            def get_option(id, name):
                local_id = id
                local_name = name
                def callback():
                    self.man_option.set(local_id)
                    self.man_label_option.set(local_name)
                return callback
            man_menu.add_command(label=man_name, command=get_option(man_id, man_name))
        manu_label.pack(anchor="w", padx=24, pady=(24,5))
        man_button.pack(fill="x", padx=24, ipady=2)
        manu_frame.grid(row=1, column=1, sticky="ew")
        
        # Create subcategories option menu
        subcategory_frame = Frame(self.form_frame, background="transparent")
        subcategory_label = Label(
            subcategory_frame,
            "Subcategory",
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.subcategory_option = StringVar()
        self.subcategory_option.set(self.initial_values[5])
        subcategory_button = Menubutton(
            subcategory_frame,
            textvariable=self.subcategory_option,
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
        for option in self.subcategory_options:
            def get_option(op):
                return lambda: self.subcategory_option.set(op)
            subcategory_menu.add_command(label=option, command=get_option(option))
        subcategory_label.pack(anchor="w", padx=24, pady=(24,5))
        subcategory_button.pack(fill="x", padx=24, ipady=2)
        subcategory_frame.grid(row=2, column=1, sticky="ew")

        date_frame, self.date_entry = self.create_input_label("Inventory date", self.initial_values[4])    
        date_frame.grid(row=0, column=2, sticky="ew")

        if self.component_type == "ic":
            clock_frame, self.clock_entry = self.create_input_label("Clock", self.initial_values[7])
            clock_frame.grid(row=1, column=2, sticky="ew")
        if self.component_type == "capacitor":
            capacitance_frame, self.capacitance_entry = self.create_input_label("Capacitance", self.initial_values[7])
            capacitance_frame.grid(row=1, column=2, sticky="ew")
        if self.component_type == "inductor":
            inductance_frame, self.inductance_entry = self.create_input_label("Inductance", self.initial_values[7])
            inductance_frame.grid(row=1, column=2, sticky="ew")
        if self.component_type == "resistor":
            resitance_frame, self.resitance_entry = self.create_input_label("Resistance", self.initial_values[7])
            resitance_frame.grid(row=1, column=2, sticky="ew")
        if self.component_type == "sensor":
            sensor_type_frame = Frame(self.form_frame, background="transparent")
            sensor_type_label = Label(
                sensor_type_frame,
                "Sensor type",
                background="transparent",
                foreground="white",
                font=FONTS.get_font("paragraph", bold=True)
            )
            self.sensor_type = StringVar()
            self.sensor_type.set(self.initial_values[7])
            sensor_types = self.app_controller.get_sensor_types()
            sensor_type_button = Menubutton(
                sensor_type_frame,
                textvariable=self.sensor_type,
                background="white", 
                relief="flat", 
                borderwidth=0, 
                highlightthickness=0,
                font=FONTS.get_font("paragraph"),
            )
            sensor_type_menu = Menu(
                sensor_type_button,
                tearoff=False,
                background=COLORS.ACCENT,
                foreground="white",
                font=FONTS.get_font("paragraph")
            )
            sensor_type_button.config(menu=sensor_type_menu)
            for option in sensor_types:
                def get_option(op):
                    return lambda: self.sensor_type.set(op)
                sensor_type_menu.add_command(label=option, command=get_option(option))
            sensor_type_label.pack(anchor="w", padx=24, pady=(24,5))
            sensor_type_button.pack(fill="x", padx=24, ipady=2)
            sensor_type_frame.grid(row=1, column=2, sticky="ew")

        add_button = AccentButton(
            self.form_frame, 
            command=self.submit, 
            text="Add",
        )

        add_button.grid(row=3, column=0, sticky="w", padx=24, pady=24, ipadx=20)
        
    def create_input_label(self, label, initial_value):
        """Create a input label and entry in a frame and return it
        
        Parameters
        ----------
        label : label of the entry

        Return (input_frame, entry)
        """
        input_frame = Frame(self.form_frame, background="transparent")
        l = Label(
            input_frame,
            label,
            background="transparent",
            foreground="white",
            font=FONTS.get_font("paragraph", bold=True)
        )
        e = Entry(input_frame, font=FONTS.get_font("paragraph"))
        e.insert(0, initial_value)
        l.pack(anchor="w", padx=24, pady=(24,5))
        e.pack(fill="x", padx=24, ipady=4)
        return input_frame, e

    def submit(self):
        """Submit the form"""
        data = {
            "part_number": self.part_number_entry.get(),
            "price": self.price_entry.get(),
            "guarantee": self.guarantee_entry.get(),
            "mnf_id": self.man_option.get(),
            "inventory_date": self.date_entry.get(),
            "sub_category": self.subcategory_option.get(),
            "stock": self.stock_entry.get(),
        }
        if self.component_type == "ic":
            data["clock"] = self.clock_entry.get()
        if self.component_type == "capacitor":
            data["capacitance"] = self.capacitance_entry.get()
        if self.component_type == "inductor":
            data["inductance"] = self.inductance_entry.get()
        if self.component_type == "resistor":
            data["resistance"] = self.resitance_entry.get()
        if self.component_type == "sensor":
            data["sensor_type"] = self.sensor_type.get()
        
        try:
            self.app_controller.update_component(self.component_type, data, data["part_number"])
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Successfull", "Add component was suscessfull")
            updated_values = list(data.values())
            self.screen.destroy()
            self.on_close_fun({"component_type": self.component_type, "values": updated_values})
            


        