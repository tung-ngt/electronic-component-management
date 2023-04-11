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

    def get_filtered_list(
            self, 
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Order]:
        return super().get_filtered_list(filters, sort_options)