from .Serializer import Serializer
from ..domains import Customer
from .constants import CUSTOMER_COLUMNS_INDEX

class CustomerSerializer(Serializer):
    def __init__(self) -> None:
        super().__init__()

    def load(self, query_result: list[str]) -> Customer:
        id = query_result[CUSTOMER_COLUMNS_INDEX["id"]]
        name = query_result[CUSTOMER_COLUMNS_INDEX["name"]]
        phone_number = query_result[CUSTOMER_COLUMNS_INDEX["phone_number"]]
        return Customer(
            id,
            name,
            phone_number
        )
    
    def load_many(self, query_results: list[list[str]]) -> list[Customer]:
        return super().load_many(query_results)
    
    def dump(self, obj: Customer) -> list[str]:
        data = [
            obj.get_id(),
            obj.get_name(),
            obj.get_phone_number()
        ]
        return data