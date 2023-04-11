import random
import sqlite3

# Sample manufacturers

manufacturer = [
    ['1', 'Apple', 'USA'],
    ['2', 'Samsung', 'South Korea'],
    ['3', 'Toyota', 'Japan'],
    ['4', 'Ford', 'USA'],
    ['5', 'Nestle', 'Switzerland'],
    ['6', 'BMW', 'Germany'],
    ['7', 'Huawei', 'China'],
    ['8', 'Procter & Gamble', 'USA'],
    ['9', 'Sony', 'Japan'],
    ['10', 'General Electric', 'USA']
]


# Sample capacitors

capacitor = [
    ['C1', '1', 1.23, '2022-05-07', 6, 0.001, 'Ceramic', 3000],
    ['C2', '5', 0.45, '2022-06-15', 3, 0.1, 'Film', 5000],
    ['C3', '2', 0.78, '2022-07-23', 12, 0.022, 'Aluminum Electrolytic', 2500],
    ['C4', '9', 0.32, '2022-08-31', 6, 0.0022, 'Ceramic', 3500],
    ['C5', '3', 1.56, '2022-09-08', 9, 0.01, 'Film', 4000],
    ['C6', '8', 1.11, '2022-10-16', 2, 0.33, 'Tantalum', 4500],
    ['C7', '6', 0.67, '2022-11-24', 8, 0.047, 'Aluminum Electrolytic', 3000],
    ['C8', '7', 0.92, '2022-12-01', 4, 0.015, 'Ceramic', 5000],
    ['C9', '4', 1.23, '2023-01-09', 5, 0.0033, 'Film', 3500],
    ['C10', '10', 0.89, '2023-02-17', 7, 0.047, 'Ceramic', 4000],
    ['C11', '1', 0.78, '2023-03-26', 11, 0.22, 'Aluminum Electrolytic', 4500],
    ['C12', '2', 0.56, '2023-04-03', 2, 0.1, 'Film', 3000],
    ['C13', '3', 1.11, '2023-05-11', 4, 0.01, 'Ceramic', 5000],
    ['C14', '5', 0.89, '2023-06-19', 8, 0.001, 'Tantalum', 3500],
    ['C15', '6', 0.45, '2023-07-27', 3, 0.068, 'Aluminum Electrolytic', 4000],
    ['C16', '8', 1.23, '2023-08-04', 9, 0.0068, 'Ceramic', 4500],
    ['C17', '9', 0.67, '2023-09-12', 6, 0.022, 'Film', 3000],
    ['C18', '10', 1.56, '2023-10-20', 5, 0.047, 'Ceramic', 5000],
    ['C19', '4', 0.78, '2023-11-28', 7, 0.33, 'Aluminum Electrolytic', 3500],
    ['C20', '7', 0.92, '2023-12-06', 2, 0.022, 'Ceramic', 4000]
]


# Sample resistors

resistor = [
    ['R1', '5', 0.45, '2022-05-07', 6, 1000, 'Carbon Film', 3000],
    ['R2', '1', 0.78, '2022-06-15', 3, 4700, 'Metal Film', 5000],
    ['R3', '3', 0.32, '2022-07-23', 12, 2200, 'Wirewound', 2500],
    ['R4', '8', 1.11, '2022-08-31', 6, 100, 'Carbon Composition', 3500],
    ['R5', '2', 1.56, '2022-09-08', 9, 3300, 'Metal Oxide Film', 4000],
    ['R6', '9', 0.67, '2022-10-16', 2, 10000, 'Carbon Film', 4500],
    ['R7', '6', 0.92, '2022-11-24', 8, 560, 'Metal Film', 3000],
    ['R8', '7', 1.23, '2022-12-01', 4, 1000, 'Wirewound', 5000],
    ['R9', '4', 0.78, '2023-01-09', 5, 470, 'Carbon Composition', 3500],
    ['R10', '10', 0.89, '2023-02-17', 7, 6800, 'Metal Oxide Film', 4000],
    ['R11', '1', 0.56, '2023-03-26', 11, 220, 'Carbon Film', 4500],
    ['R12', '2', 1.11, '2023-04-03', 2, 8200, 'Metal Film', 3000],
    ['R13', '3', 0.45, '2023-05-11', 4, 1200, 'Wirewound', 5000],
    ['R14', '5', 0.89, '2023-06-19', 8, 1.2, 'Carbon Composition', 3500],
    ['R15', '6', 1.23, '2023-07-27', 3, 1800, 'Metal Oxide Film', 4000],
    ['R16', '8', 0.67, '2023-08-04', 9, 330, 'Carbon Film', 4500],
    ['R17', '9', 1.56, '2023-09-12', 6, 100000, 'Metal Film', 3000],
    ['R18', '10', 0.78, '2023-10-20', 5, 22000, 'Wirewound', 5000],
    ['R19', '4', 0.45, '2023-11-28', 7, 10000, 'Carbon Composition', 3500],
    ['R20', '7', 1.11, '2023-12-06', 2, 5600, 'Metal Oxide Film', 4000]
]

# Sample inductors

inductor = [
    ['L1', '2', 1.56, '2022-05-07', 6, 0.1, 'Air Core', 3000],
    ['L2', '5', 0.89, '2022-06-15', 3, 1, 'Ferrite Core', 5000],
    ['L3', '3', 1.23, '2022-07-23', 12, 0.022, 'Iron Core', 2500],
    ['L4', '9', 0.45, '2022-08-31', 6, 0.001, 'Air Core', 3500],
    ['L5', '7', 0.67, '2022-09-08', 9, 0.056, 'Ferrite Core', 4000],
    ['L6', '10', 1.23, '2022-10-16', 2, 0.0033, 'Iron Core', 4500],
    ['L7', '6', 0.78, '2022-11-24', 8, 0.1, 'Air Core', 3000],
    ['L8', '8', 0.56, '2022-12-01', 4, 0.056, 'Ferrite Core', 5000],
    ['L9', '4', 1.11, '2023-01-09', 5, 0.022, 'Iron Core', 3500],
    ['L10', '1', 0.67, '2023-02-17', 7, 0.1, 'Air Core', 4000],
    ['L11', '2', 1.56, '2023-03-27', 11, 1, 'Ferrite Core', 2500],
    ['L12', '3', 0.89, '2023-04-04', 3, 0.056, 'Iron Core', 3500],
    ['L13', '5', 1.23, '2023-05-12', 10, 0.001, 'Air Core', 3000],
    ['L14', '6', 0.45, '2023-06-20', 1, 0.022, 'Ferrite Core', 4500],
    ['L15', '7', 0.78, '2023-07-28', 4, 0.1, 'Iron Core', 4000],
    ['L16', '10', 0.67, '2023-08-05', 9, 0.056, 'Air Core', 5000],
    ['L17', '8', 1.11, '2023-09-13', 6, 0.0033, 'Ferrite Core', 3500],
    ['L18', '9', 0.56, '2023-10-21', 5, 0.022, 'Iron Core', 3000],
    ['L19', '4', 1.23, '2023-11-29', 7, 0.1, 'Air Core', 4500],
    ['L20', '7', 0.89, '2023-12-07', 2, 1, 'Ferrite Core', 4000]
]


# Sample ICs

IC = [
    ['IC1', '1', 2.34, '2022-05-08', 6, 50, 'Microcontroller', 3000],
    ['IC2', '2', 1.67, '2022-06-16', 3, 100, 'Amplifier', 5000],
    ['IC3', '3', 4.56, '2022-07-24', 12, 200, 'Converter', 2500],
    ['IC4', '4', 0.89, '2022-08-01', 6, 500, 'Regulator', 3500],
    ['IC5', '5', 3.45, '2022-09-09', 9, 1000, 'Sensor Interface', 4000],
    ['IC6', '6', 2.34, '2022-10-17', 2, 150, 'Microcontroller', 4500],
    ['IC7', '7', 1.56, '2022-11-25', 8, 75, 'Amplifier', 3000],
    ['IC8', '8', 4.78, '2022-12-02', 4, 300, 'Converter', 5000],
    ['IC9', '9', 0.67, '2023-01-10', 5, 250, 'Regulator', 3500],
    ['IC10', '10', 3.33, '2023-02-18', 7, 500, 'Sensor Interface', 4000],
    ['IC11', '1', 2.22, '2023-03-28', 11, 150, 'Microcontroller', 2500],
    ['IC12', '2', 1.11, '2023-04-05', 3, 75, 'Amplifier', 3500],
    ['IC13', '3', 4.44, '2023-05-13', 10, 300, 'Converter', 3000],
    ['IC14', '4', 0.78, '2023-06-21', 1, 250, 'Regulator', 4500],
    ['IC15', '5', 2.22, '2023-07-29', 4, 500, 'Sensor Interface', 4000],
    ['IC16', '6', 1.67, '2023-08-06', 9, 150, 'Microcontroller', 5000],
    ['IC17', '7', 4.56, '2023-09-14', 6, 75, 'Amplifier', 3500],
    ['IC18', '8', 0.89, '2023-10-22', 5, 300, 'Converter', 3000],
    ['IC19', '9', 3.45, '2023-11-30', 7, 250, 'Regulator', 4500],
    ['IC20', '10', 2.34, '2023-12-08', 2, 500, 'Sensor Interface', 4000]
]


# Sample sensors

sensor = [
    ['S1', '1', 2.34, '2022-01-01', 6, 'Temperature', 'Thermocouple', 2500],
    ['S2', '2', 3.45, '2022-02-09', 9, 'Pressure', 'Strain Gauge', 3000],
    ['S3', '3', 4.56, '2022-03-19', 12, 'Humidity', 'Capacitive', 3500],
    ['S4', '4', 5.67, '2022-04-27', 2, 'Infrared', 'Thermal', 4000],
    ['S5', '5', 6.78, '2022-05-05', 7, 'Motion', 'Accelerometer', 4500],
    ['S6', '6', 7.89, '2022-06-13', 4, 'Light', 'Photodiode', 5000],
    ['S7', '7', 8.90, '2022-07-21', 8, 'Temperature', 'RTD', 2500],
    ['S8', '8', 9.87, '2022-08-29', 10, 'Pressure', 'Piezoelectric', 3000],
    ['S9', '9', 1.23, '2022-09-06', 3, 'Humidity', 'Resistive', 3500],
    ['S10', '10', 2.34, '2022-10-14', 5, 'Infrared', 'Pyroelectric', 4000],
    ['S11', '1', 3.45, '2022-11-22', 11, 'Motion', 'Gyroscope', 4500],
    ['S12', '2', 4.56, '2022-12-30', 1, 'Light', 'Phototransistor', 2500],
    ['S13', '3', 5.67, '2023-01-07', 7, 'Temperature', 'Thermistor', 3000],
    ['S14', '4', 6.78, '2023-02-15', 4, 'Pressure', 'Resonant', 3500],
    ['S15', '5', 7.89, '2023-03-25', 12, 'Humidity', 'Inductive', 4000],
    ['S16', '6', 8.90, '2023-04-02', 2, 'Infrared', 'Active', 4500],
    ['S17', '7', 9.87, '2023-05-10', 10, 'Motion', 'Magnetometer', 2500],
    ['S18', '8', 1.23, '2023-06-18', 3, 'Light', 'Photoresistor', 3000],
    ['S19', '9', 2.34, '2023-07-26', 5, 'Temperature', 'Infrared', 3500],
    ['S20', '10', 3.45, '2023-08-03', 8, 'Pressure', 'Capacitive', 4000]
]


# Shuffle the lists
random.shuffle(sensor)
random.shuffle(IC)
random.shuffle(inductor)
random.shuffle(resistor)
random.shuffle(capacitor)

def get_connection():
    conn = sqlite3.connect('models/db/electronic_store.db')
    cursor = conn.cursor()
    return conn, cursor


def create_tables():
    # create a connection to the database
    mydb, mycursor = get_connection()
    # create a cursor to execute SQL queries

    # create the manufacturer table
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS manufacturer (
            id VARCHAR(255) PRIMARY KEY, 
            name VARCHAR(255) NOT NULL,
            country VARCHAR(255) NOT NULL
            )
        """
    )

    for row in manufacturer:
        mycursor.execute(
            '''
            INSERT INTO manufacturer (id, name, country) VALUES (?, ?, ?);
            ''', row
        )

    # Create table for capacitor with same value as component but with capacitance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS capacitor (
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date TEXT NOT NULL, 
            guarantee INT NOT NULL,
            capacitance VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in capacitor:
        mycursor.execute(
            '''
            INSERT INTO capacitor (part_number, mnf_id, price, inventory_date, guarantee, capacitance, sub_category, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', row
        )

    # Create table for resistor with same value as component but with resistance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS resistor(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date TEXT NOT NULL, 
            guarantee INT NOT NULL, 
            resistance VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in resistor:
        mycursor.execute(
            '''
            INSERT INTO resistor (part_number, mnf_id, price, inventory_date, guarantee, resistance, sub_category, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', row
        )

    # Create table for inductor with same value as component but with inductance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inductor(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date TEXT NOT NULL, 
            guarantee INT NOT NULL,
            inductance VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in inductor:
        mycursor.execute(
            '''
            INSERT INTO inductor (part_number, mnf_id, price, inventory_date, guarantee, inductance, sub_category, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', row
        )

    # Create table for sensor with same value as component but with sensor_type
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sensor(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date TEXT NOT NULL, 
            guarantee INT NOT NULL,
            sensor_type VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in sensor:
        mycursor.execute(
            '''
            INSERT INTO sensor (part_number, mnf_id, price, inventory_date, guarantee, sensor_type, sub_category, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', row
        )

    # Create table for IC with same value as component but with class
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS IC(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL,
            inventory_date TEXT NOT NULL,
            guarantee INT NOT NULL,
            clock VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in IC:
        mycursor.execute(
            '''
            INSERT INTO IC (part_number, mnf_id, price, inventory_date, guarantee, clock, sub_category, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', row
        )

    mydb.commit()


TABLE_PARAMETER = "{TABLE_PARAMETER}"
DROP_TABLE_SQL = f"DROP TABLE {TABLE_PARAMETER};"
GET_TABLES_SQL = "SELECT name FROM sqlite_schema WHERE type='table';"


def delete_all_tables(con):
    tables = get_tables(con)
    delete_tables(con, tables)


def get_tables(con):
    cur = con.cursor()
    cur.execute(GET_TABLES_SQL)
    tables = cur.fetchall()
    cur.close()
    return tables


def delete_tables(con, tables):
    cur = con.cursor()
    for table, in tables:
        sql = DROP_TABLE_SQL.replace(TABLE_PARAMETER, table)
        cur.execute(sql)
    cur.close()

