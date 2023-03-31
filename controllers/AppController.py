from models.pushpull.Pushpulltosql import pull
from models.db.Utils_database import get_connection



class AppController:
    def __init__(self, database_path):
        self.__ics = []
        self.__capacitors = []
        self.__inductors = []
        self.__manufacturers = []
        self.__resistors = []
        self.__sensors = []

        self.connect_to_db(database_path)


    def connect_to_db(self, database_path):
        self.db_conn, cursor = get_connection(database_path)
        print(cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
    

    def load_data_from_db(self):
        cap_num, self.__capacitors = pull(self.db_conn, 'capacitor')
        ic_num, self.__ics = pull(self.db_conn, 'ic')
        res_num, self.__resistors = pull(self.db_conn, 'resistor')
        ind_num, self.__inductors = pull(self.db_conn, 'inductor')
        sen_num, self.__sensors = pull(self.db_conn, 'sensor')
        manu_num, self.__manufacturers = pull(self.db_conn, 'manufacturer')

    def get_capacitors(self):
        return self.__capacitors

    def get_ics(self):
        return self.__ics

    def get_inductors(self):
        return self.__inductors

    def get_manufacturers(self):
        return self.__manufacturers

    def get_resistors(self):
        return self.__resistors

    def get_sensors(self):
        return self.__sensors
    

