class Manufacturer:
    """Represents manufacturer's information

    Attributes
    ----------
    id : id of the manufacturer
    name : name of the manufacturer
    country : origin country of the manufacturer
    """
    def __init__(self, id: str, name: str, country: str):
        self.set_id(id)
        self.set_name(name)
        self.set_country(country)
    
    # Getters
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country
    
    # Setters
    def set_id(self, id: str):
        if len(id) > 0:
            self.__id = id
        else:
            raise Exception("ID can not be empty")

    def set_name(self, name: str):
        if len(name) > 0:
            self.__name = name
        else:
            raise Exception("Empty name is not allowed")

    def set_country(self, country: str):
        self.__country = country