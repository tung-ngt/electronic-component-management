from tkinter import Toplevel, Entry, StringVar, Menu, Menubutton
from ...gui import Frame, Label
from ...components import CustomListView, AccentHorizontalScrollbar, AccentButton
from ...constants import COLORS, FONTS

class AddItemWindow:
    def __init__(self,
            master,
            app_controller,
            on_add = None
        ) -> None:
        self.master = master
        self.app_controller = app_controller
        self.on_add = on_add
        self.components = self.get_components()
        self.search_string = ""
        self.type_option = StringVar()

    def get_components(self):
        components = []
        for c in ["ic", "capacitor", "inductor", "sensor", "resistor"]:
            result = self.app_controller.get_list(c)
            for r in result:
                components.append([
                    r.get_part_number(),
                    c.capitalize(),
                    r.get_price()
                ])
        return components
    
    def search(self):
        self.search_string = self.part_number_entry.get().lower()
        self.create_list()

    def clear_items(self):
        for item in self.list_view.get_children():
            self.list_view.delete(item)
    
    def create_list(self):
        self.clear_items()
        for c in self.components:
            if self.search_string not in c[0].lower():
                continue
                
            if self.type_option.get() != "None" and c[1] != self.type_option.get():
                continue

            self.list_view.add_item(c)

    def toggle(self, op):
        if self.type_option.get() == op:
            self.type_option.set("None")
        else:
            self.type_option.set(op)

        self.create_list()

    def show_popup(self):
        self.search_string = ""
        self.type_option.set("None")
        self.screen = Toplevel(self.master)
        self.screen["background"] = "white"
        self.screen.title("Add a item")
        self.screen.grab_set()
        self.screen.state("zoomed")


        search_frame = Frame(self.screen, background=COLORS.WHITE)
        search_frame.pack(fill="x")

        self.part_number_entry = Entry(search_frame, font=FONTS.get_font("paragraph"))
        search_button = AccentButton(search_frame, self.search, "Search")
        self.part_number_entry.pack(side="left", fill="y", ipady=10, pady=10, padx=10)
        search_button.pack(side="left", pady=10)


        type_label = Label(
            search_frame,
            "Type",
            background="transparent",
            font=FONTS.get_font("paragraph", bold=True)
        )
        
        type_button = Menubutton(
            search_frame,
            textvariable=self.type_option,
            background=COLORS.SECONDARY, 
            foreground="white",
            relief="flat", 
            borderwidth=0, 
            highlightthickness=0,
            font=FONTS.get_font("paragraph"),
        )
        type_menu = Menu(
            type_button,
            tearoff=False,
            background=COLORS.ACCENT,
            foreground="white",
            font=FONTS.get_font("paragraph")
        )
        type_button.config(menu=type_menu)
        for option in ["Ic", "Capacitor", "Resistor", "Sensor", "Inductor"]:
            def get_option(op):
                return lambda: self.toggle(op)
            type_menu.add_command(label=option, command=get_option(option))
        type_label.pack(side="left", padx=(40, 10), pady=10)
        type_button.pack(side="left", ipady=2, pady=10)

        list_view_frame = Frame(self.screen, background=COLORS.WHITE)
        list_view_frame.pack(fill="both", expand=True)

        scroll_bar = AccentHorizontalScrollbar(list_view_frame)
        self.list_view = CustomListView(
            list_view_frame,
            (
                "part_number",
                "type",
                "price"
            ),
            scroll_bar.set
        )
        scroll_bar.add_command(self.list_view.yview)

        scroll_bar.pack(side="right", fill="y")
        self.list_view.pack(side="left", fill="both", expand=True)

        self.list_view.config_headings({
            "part_number": {"text": "Part number"},
            "type": {"text": "Component type"},
            "price": {"text": "Price"}
        })
        self.create_list()

        self.list_view.bind("<Double-1>", self.choose)

    def choose(self, event):
        region = self.list_view.identify_region(event.x, event.y)

        if region != "cell":
            return
        
        selected_iid = self.list_view.focus()
        values = self.list_view.item(selected_iid)["values"]

        self.screen.destroy()
        self.screen.grab_release()
        self.on_add({
            "part_number": values[0],
            "price": values[2]
        })

