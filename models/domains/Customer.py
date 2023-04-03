class Customer:
    """This class represent a customer which by components
    
    Attributes
    ----------
    id : id of the customer (str)
    name : name of the customer (str)
    phone_number : phone number to contact (str)
    """
    def __init__(self,
            id: str,
            name: str,
            phone_number: str,
        ):
        self.set_id(id)
        self.set_name(name)
        self.set_phone_number(phone_number)
        
    # Getter
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_phone_number(self):
        return self.__phone_number

    def get_all_info(self):
        return [self.__id, self.__name, self.__phone_number]

    # Setter
    def set_id(self, id: str):
        if len(id) < 1:
            raise Exception("ID can not be empty")
        
        self.__id = id

    def set_name(self, name: str):
        if len(name) < 1:
            raise Exception("Name can not be empty")
        
        self.__name = name

    def set_phone_number(self, phone_number: str):
        if len(phone_number) < 1:
            raise Exception("Phone number can not be emty")
        
        self.__phone_number = phone_number