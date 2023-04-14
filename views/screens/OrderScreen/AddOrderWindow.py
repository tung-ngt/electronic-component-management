from tkinter import Toplevel, Entry, StringVar, Menubutton, Menu, messagebox
from ...constants import COLORS, FONTS
from ...gui import Label, Frame
from ...components import AccentButton, CustomListView, AccentHorizontalScrollbar
from .AddItemWindow import AddItemWindow
from math import floor
class AddOrderWindow:
    """This is a pop up window to add a student"""
    def __init__(self,
            master,
            app_controller, 
            on_close_fun = None,
        ):
        """Create the window
        
        Parameters
        ----------
        master : master widget
        component_type : type of component to add
        app_controller : app controller
        on_close_fun : function to run when closing window
        """
        # Window settings
        self.screen = Toplevel(master)
        self.screen.title("Add a order")
        self.screen.grab_set()
        self.screen.state("zoomed")
        self.screen["background"] = COLORS.WHITE

        self.on_close_fun = self.get_on_close_fun(on_close_fun)
        if self.on_close_fun != None:
            self.screen.protocol("WM_DELETE_WINDOW", self.on_close_fun)

        self.app_controller = app_controller

        self.add_item_window = AddItemWindow(
            self.screen, 
            self.app_controller, 
            self.add_item
        )
        self.create_form()

    def add_item(self, item):
        self.screen.grab_set()
        self.items_list.add_item((item["part_number"], 0, item["price"], 0))

    def get_all_manufacturers_ids(self):
        manufacturers = self.app_controller.get_manufacturers()
        manufacturers_ids = {}
        for manufacturer in manufacturers:
            manufacturers_ids[manufacturer.get_id()] = manufacturer.get_name()
        return manufacturers_ids

    def get_on_close_fun(self, on_close_fun):
        def close():
            self.screen.destroy()
            on_close_fun()
        return close

    def create_form(self):
        """Create component information form"""
        # self.screen.grid_columnconfigure(0, weight=1)
        # self.screen.grid_rowconfigure(0, weight=1)
        # self.screen.grid_rowconfigure(1, weight=4)

        self.items_frame = Frame(self.screen, background=COLORS.WHITE)
        self.form_frame = Frame(self.screen, background=COLORS.PRIMARY)
        self.form_frame.pack(fill="x")
        self.items_frame.pack(fill="both", expand=True)
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=2)
        self.form_frame.grid_columnconfigure(2, weight=1)
        self.form_frame.grid_rowconfigure(0, weight=1)
        self.form_frame.grid_rowconfigure(1, weight=1)
        self.form_frame.grid_rowconfigure(2, weight=1)

        label = Label(
            self.form_frame,
            "Add order",
            foreground=COLORS.WHITE,
            background="transparent",
            font=FONTS.get_font("heading1", bold=True),
        )
        label.grid(row=0, column=0, rowspan=2)

        self.total_price = Label(
            self.form_frame,
            "Total: 0",
            foreground=COLORS.WHITE,
            background="transparent",
            font=FONTS.get_font("paragraph", bold=True)
        )
        self.total_price.grid(row=2, column=0)


        self.order_id_frame, self.order_id_entry = self.create_input_label("Order id")
        self.order_id_frame.grid(row=0, column=1, sticky="sew", pady=(20, 0))
        
        self.customer_id_frame, self.customer_id_entry = self.create_input_label("Customer id")
        self.customer_id_frame.grid(row=1, column=1, sticky="sew")

        self.date_frame, self.date_entry = self.create_input_label("Purchase date")
        self.date_frame.grid(row=2, column=1, sticky="sew", pady=(0, 20))

        self.add_item_button = AccentButton(
            self.form_frame, 
            self.add_item_window.show_popup, 
            "Add item"
        )
        self.add_item_button.grid(row=0, column=2, sticky="sew", padx=(0, 20))

        self.remove_item_button = AccentButton(self.form_frame, self.delete_item, "Remove item")
        self.remove_item_button.grid(row=1, column=2, sticky="sew", padx=(0, 20))

        self.create_order_button = AccentButton(self.form_frame, self.submit, "Create order")
        self.create_order_button.grid(row=2, column=2, sticky="sew", padx=(0, 20), pady=(0,20))

        self.scroll_bar = AccentHorizontalScrollbar(self.items_frame)
        self.items_list = CustomListView(
            self.items_frame,
            (
                "part_number",
                "amount",
                "price",
                "total",
            ),
            self.scroll_bar.set
        )
        self.scroll_bar.add_command(self.items_list.yview)
    
        self.scroll_bar.pack(side="right", fill="y")
        self.items_list.pack(side="left", fill="both", expand=True)

        self.items_list.config_headings({
            "part_number": {"text": "Part number"},
            "amount": {"text": "Amount"},
            "price": {"text": "Price"},
            "total": {"text": "Total"}
        })

        self.items_list.bind("<Double-1>", self.change_amount)

    def change_amount(self, event):
        region = self.items_list.identify_region(event.x, event.y)
            
        if region != "cell":
            return
        
        column = self.items_list.identify_column(event.x)
        column_index = int(column[1]) - 1

        if column_index != 1:
            return

        selected_iid = self.items_list.focus()
        selected_amount = self.items_list.item(selected_iid)["values"][1]

        column_box = self.items_list.bbox(selected_iid, column)


        entry = Entry(self.items_frame, width=column_box[2])

        entry.edditting_column_index = column_index
        entry.edditting_item_iid = selected_iid
        entry.insert(0, selected_amount)
        entry.select_range(0, "end")
        entry.focus()
        def on_enter(e):
            entry_selected_iid = entry.edditting_item_iid
            new_amount = int(e.widget.get())
            current_value = self.items_list.item(entry_selected_iid)["values"]
            current_value[1] = new_amount
            current_value[-1] = floor(new_amount * float(current_value[2]) * 100) / 100
            self.items_list.item(entry_selected_iid, values=current_value)
            e.widget.destroy()
            self.update_price()

        entry.bind("<FocusOut>", on_enter)
        entry.bind("<Return>", on_enter)

        entry.place(x=column_box[0], y=column_box[1], w=column_box[2], h=column_box[3])

    def delete_item(self):
        selected_iid = self.items_list.focus()
        print(selected_iid)
        if selected_iid == "":
            messagebox.showerror("Can not delete", "A item must be seleted to delete")
            return
        
        self.items_list.delete(selected_iid)
        self.update_price()
    
    def update_price(self):
        total = 0
        for item in self.items_list.get_children():
            info = self.items_list.item(item)["values"]
            total += float(info[-1])

        total = floor(total * 100) / 100
        self.total_price.config(text=f"Total: {total}")

    def create_input_label(self, label):
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
        l.pack(anchor="w", padx=24)
        e.pack(fill="x", padx=24, ipady=4)
        return input_frame, e

    def submit(self):
        """Submit the form"""
        price = float(self.total_price["text"].split(": ")[-1])

        if price <= 0:
            messagebox.showwarning("Can not create order", "Can not create an order with no items")
            return

        data = {
            "order_id": self.order_id_entry.get(),
            "customer_id": self.customer_id_entry.get(),
            "date": self.date_entry.get(),
            "items": {}
        }

        for item in self.items_list.get_children():
            value = self.items_list.item(item)["values"]
            if int(value[1]) > 0:
                data["items"][value[0]] = int(value[1])

        try:
            self.app_controller.add_order(data)
        except Exception as e:
            messagebox.showerror("Error", str(e))
        else:
            messagebox.showinfo("Successfull", "Add order was suscessfull")

        