from re import match

def validate_date(d: str):
    if match(r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", d) == None:
        raise Exception("Invalid date, must be the form yyyy-mm-dd")
    else:
        return True

class Order:
    """This class represent a order object
    
    Attributes
    ----------
    order_id : str id of the order
    cusomter_id : id of the customer that made the order
    items : a dict of form
    {
        part_number: number_of_items
    }
    date : the date that the order is made
    """
    def __init__(self,
            order_id: str,
            customer_id: str,
            items: dict[str, int],
            date: str,
        ):
        self.set_order_id(order_id)
        self.set_customer_id(customer_id)
        self.set_items(items)
        self.set_date(date)

    # Getters
    def get_order_id(self):
        return self.__order_id
    
    def get_customer_id(self):
        return self.__customer_id
    
    def get_items(self):
        return self.__items
    
    def get_date(self):
        return self.__date
    
    def get_all_info(self):
        return [self.__order_id, self.__customer_id, self.__items, self.__date]

    # Setters
    def set_order_id(self, order_id: str):
        if len(order_id) < 1:
            raise Exception("ID can not be empty")
        
        self.__order_id = order_id

    def set_customer_id(self, customer_id: str):
        if len(customer_id) < 1:
            raise Exception("Customer ID can not be empty")
        
        self.__customer_id = customer_id

    def set_items(self, items: dict):
        if len(items) < 1:
            raise Exception("Items can not be empty")

        for value in list(items.values()):
            if value < 1:
                raise Exception("Number of items must be positive")
            
        self.__items = items

    def set_date(self, date: str):
        if validate_date(date):
            self.__date = date