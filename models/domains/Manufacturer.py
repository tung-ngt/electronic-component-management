class Manufacturer:
    """Represents manufacturer's information

    Attributes
    ----------
    id, name, country
    """
    def __init__(self, id, name, country):
        self.__id = id
        self.__name = name
        self.__country = country
    def getID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getCountry(self):
        return self.__country
    def setName(self, name):
        self.__name = name
    def setID(self, id):
        self.__id = id
    def setCountry(self, country):
        self.__country = country
