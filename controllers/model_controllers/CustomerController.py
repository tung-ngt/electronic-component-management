from .ModelController import ModelController
from models.domains import Customer
from models.serializers import CustomerSerializer

class CustomerController(ModelController):
    def __init__(self) -> None:
        super().__init__(
            "customer",
            "id",
            {
                "id": "search",
                "name": "search",
                "phone_number": "search"
            },
            CustomerSerializer()
        )

    def get_list(self) -> list[Customer]:
        return super().get_list()
    
    def add(self, data: dict) -> Customer:
        if self.item_exists(data["id"]) != None:
            raise Exception("Customer's id must be unique")
        
        new_customer = Customer(
            data["id"],
            data["name"],
            data["phone_number"]
        )
        self.add_to_list(new_customer)
        self.create_db_row(new_customer)
        return new_customer
    
    def item_exists(self, key: str) -> Customer:
        for customer in self._list:
            if key == customer.get_id():
                return customer
        return None

    def get_filtered_list(
            self, 
            filters: dict[str, str] = ..., 
            sort_options: dict[str, str] = ...
        ) -> list[Customer]:
        return super().get_filtered_list(filters, sort_options)