from .Serializer import Serializer
from ..domains import Order
from .constants import ORDER_COLUMNS_INDEX
import json

class OrderSerializer(Serializer):
    def __init__(self) -> None:
        super().__init__()

    def load(self, query_result: list[str]) -> Order:
        order_id = query_result[ORDER_COLUMNS_INDEX["order_id"]]
        customer_id = query_result[ORDER_COLUMNS_INDEX["customer_id"]]
        items_json = query_result[ORDER_COLUMNS_INDEX["items_json"]]
        items = json.loads(items_json)
        date = query_result[ORDER_COLUMNS_INDEX["date"]]
        return Order(
            order_id,
            customer_id,
            items,
            date
        )
    
    def load_many(self, query_results: list[list[str]]) -> list[Order]:
        return super().load_many(query_results)
    
    def dump(self, obj: Order) -> list[str]:
        data = [
            obj.get_order_id(),
            obj.get_customer_id(),
            json.dumps(obj.get_items()),
            obj.get_date()
        ]
        return data