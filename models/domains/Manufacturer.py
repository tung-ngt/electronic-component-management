import os

class Manufacturer:
    """Represents manufacturer's information

    Attributes
    ----------
    id : id of the manufacturer
    name : name of the manufacturer
    country : origin country of the manufacturer
    """
    def __init__(self, id: str, name: str, country: str, image_path: str = None):
        self.set_id(id)
        self.set_name(name)
        self.set_country(country)
        self.set_image_path(image_path)
    
    # Getters
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country
    
    def get_all_info(self):
        return [self.__id, self.__name, self.__country]
    
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

    def set_image_path(self, image_path):
        if image_path == None:
            self.__image_path = image_path
            return
        
        if os.path.isfile(image_path):
            self.__image_path = image_path
        else:
            raise Exception("Image path not found")