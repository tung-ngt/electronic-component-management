import random
import pickle
# abspath to models
import os, sys
sys.path.append(os.path.abspath(os.path.join('..', 'models')))

from models.domains import Component, Capacitor, Resistor, Inductor, Sensor, IC, Manufacturer
from models.db.Utils_database import get_connection
from models.pushpull.Pushpulltosql import push, pull







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
    with open('./data/sensor.pickle', 'rb') as f:
        sensor = pickle.load(f)
    with open('./data/ic.pickle', 'rb') as f:
        ic = pickle.load(f)
    with open('./data/inductor.pickle', 'rb') as f:
        inductor = pickle.load(f)
    with open('./data/resistor.pickle', 'rb') as f:
        resistor = pickle.load(f)
    with open('./data/capacitor.pickle', 'rb') as f:
        capacitor = pickle.load(f)
    with open('./data/manufacturer.pickle', 'rb') as f:
        manufacturer = pickle.load(f)



    # create the manufacturer table
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS manufacturer (
            image_path VARCHAR(255) NOT NULL,
            id VARCHAR(255) PRIMARY KEY, 
            name VARCHAR(255) NOT NULL,
            country VARCHAR(255) NOT NULL
            )
        """
    )

    for row in manufacturer:
        push(row)

    # Create table for capacitor with same value as component but with capacitance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS capacitor (
            image_path VARCHAR(255) NOT NULL,
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL,
            capacitance REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in capacitor:
        push(row)


    # Create table for resistor with same value as component but with resistance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS resistor(
            image_path VARCHAR(255) NOT NULL,
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL, 
            resistance REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in resistor:
        push(row)

    # Create table for inductor with same value as component but with inductance
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inductor(
            image_path VARCHAR(255) NOT NULL,
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL,
            inductance REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in inductor:
        push(row)

    # Create table for sensor with same value as component but with sensor_type
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sensor(
            image_path VARCHAR(255) NOT NULL,
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL, 
            inventory_date DATE NOT NULL, 
            guarantee INT NOT NULL,
            sensor_type VARCHAR(255) NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in sensor:
        push(row)

    # Create table for IC with same value as component but with class
    mycursor.execute(
        """
        CREATE TABLE IF NOT EXISTS IC(
            image_path VARCHAR(255) NOT NULL,
            part_number VARCHAR(255) PRIMARY KEY,
            mnf_id VARCHAR(255) NOT NULL, 
            price REAL NOT NULL,
            inventory_date DATE NOT NULL,
            guarantee INT NOT NULL,
            clock REAL NOT NULL,
            sub_category VARCHAR(255) NOT NULL,
            stock BIGINT NOT NULL,
            FOREIGN KEY (mnf_id) REFERENCES manufacturer(id))
        """
    )
    for row in ic:
        push(row)

    mydb.commit()






