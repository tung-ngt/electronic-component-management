import random
import pickle

from models.db.utils.connect_to_db import get_connection
from models.db.functions import push



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

def create_tables():
    # create a connection to the database
    mydb, mycursor = get_connection('./data/electronic_store_with_classes.db')
    
    # Load the data from pickle
    with open('./generate_data/manufacturers.pickle', 'rb') as f:
        manufacturers = pickle.load(f)
    with open('./generate_data/sensors.pickle', 'rb') as f:
        sensors = pickle.load(f)
    with open('./generate_data/ics.pickle', 'rb') as f:
        ics = pickle.load(f)
    with open('./generate_data/inductors.pickle', 'rb') as f:
        inductors = pickle.load(f)
    with open('./generate_data/resistors.pickle', 'rb') as f:
        resistors = pickle.load(f)
    with open('./generate_data/capacitors.pickle', 'rb') as f:
        capacitors = pickle.load(f)
    with open('./generate_data/customers.pickle', 'rb') as f:
        customers = pickle.load(f)
    with open('./generate_data/orders.pickle', 'rb') as f:
        orders = pickle.load(f)


    # create the manufacturer table
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS manufacturer (
            id VARCHAR(255) PRIMARY KEY, 
            name VARCHAR(255) NOT NULL,
            country VARCHAR(255) NOT NULL, 
            image_path VARCHAR(255) NOT NULL
            )
        """
    )

    for row in manufacturers:
        push(row)

    # Create table for capacitor with same value as component but with capacitance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS capacitor (
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL,
            capacitance REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            image_path VARCHAR(255) NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in capacitors:
        push(row)


    # Create table for resistor with same value as component but with resistance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS resistor(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL, 
            resistance REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            image_path VARCHAR(255) NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in resistors:
        push(row)

    # Create table for inductor with same value as component but with inductance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inductor(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL,
            inductance REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            image_path VARCHAR(255) NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in inductors:
        push(row)

    # Create table for sensor with same value as component but with sensor_type
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sensor(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL,
            sensor_type VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            image_path VARCHAR(255) NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in sensors:
        push(row)

    # Create table for IC with same value as component but with class
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS IC(
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL,
            inventory_date DATE NOT NULL,
            guarantee INT NOT NULL,
            clock REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            image_path VARCHAR(255) NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in ics:
        push(row)

    mydb.commit()


