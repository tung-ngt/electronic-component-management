from .ModelController import ModelController
from models.domains import Order
from models.serializers import OrderSerializer

class OrderController(ModelController):
    def __init__(self) -> None:
        super().__init__(
            "orders",
            "order_id",
            {
                "order_id": "search",
                "customer_id": "search",
                "date": "range",
                "items": "search"
            },
            OrderSerializer()
        )

    def get_list(self) -> list[Order]:
        return super().get_list()

    def add(self, data: dict) -> Order:
        if self.item_exists(data["order_id"]) != None:
            raise Exception("Order id must be unique")
        
        new_order = Order(
            data["order_id"],
            data["customer_id"],
            data["items"],
            data["date"],
        )
        self.add_to_list(new_order)
        self.create_db_row(new_order)
        return new_order

    def item_exists(self, key: str) -> Order:
        for order in self._list:
            if key == order.get_order_id():
                return order
        return None

    def update(self, data: dict, key: str) -> Order:
        order_to_update = self.item_exists(key)
        if order_to_update == None:
            raise Exception("Order id not found")

        if "customer_id" in data.keys() and data["customer_id"] != "":
            order_to_update.set_customer_id(data["customer_id"])
        if "items" in data.keys() and data["items"] != "":
            order_to_update.set_items(data["items"])
        if "date" in data.keys() and data["date"] != "":
            order_to_update.set_date(data["date"])

        self.update_db_row(data, key)
        return order_to_update
    
    def get_filtered_list(
            self, 
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Order]:
        return super().get_filtered_list(filters, sort_options)