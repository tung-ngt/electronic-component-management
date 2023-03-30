import random
import sqlite3
from os import path
import sys
path_to_models = path.abspath(r'C:\Users\ciltr\Desktop\USTH\Semester 2\Python\Python project\electronic-component-management\models')
sys.path.append(path_to_models)
from domains import Capacitor, Resistor, Inductor, Sensor, IC, Manufacturer


#Manufacturer:


m1 = Manufacturer("M001", "AVX Corporation", "United States")
m2 = Manufacturer("M002", "KEMET Corporation", "United States")
m3 = Manufacturer("M003", "Yageo Corporation", "Taiwan")
m4 = Manufacturer("M004", "TDK Corporation", "Japan")
m5 = Manufacturer("M005", "Panasonic Corporation", "Japan")
m6 = Manufacturer("M006", "Murata Manufacturing Co., Ltd.", "Japan")
m7 = Manufacturer("M007", "Rohm Semiconductor", "Japan")
m8 = Manufacturer("M008", "Vishay Intertechnology, Inc.", "United States")
m9 = Manufacturer("M009", "Infineon Technologies AG", "Germany")
m10 = Manufacturer("M010", "STMicroelectronics", "Switzerland")

manufacturer = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

#Capacitor:
c1 = Capacitor(m1.get_id(), 0.25, "2022-06-30", 12, "C0805C104K5RACTU", "MLCC", 1000, 0.1)
c2 = Capacitor(m1.get_id(), 0.12, "2022-08-20", 12, "C0402C103K5RACTU", "MLCC", 2000, 0.01)
c3 = Capacitor(m2.get_id(), 0.34, "2022-05-15", 18, "C0603C225K8PACTU", "MLCC", 1500, 2.2)
c4 = Capacitor(m2.get_id(), 0.48, "2022-09-10", 18, "C1206C106K8RACTU", "MLCC", 800, 10.0)
c5 = Capacitor(m3.get_id(), 0.10, "2022-10-15", 24, "CC0402KRX7R7BB103", "MLCC", 5000, 0.01)
c6 = Capacitor(m3.get_id(), 0.20, "2022-11-25", 24, "CC0603KRX7R7BB105", "MLCC", 3000, 1.0)
c7 = Capacitor(m4.get_id(), 0.08, "2022-08-10", 12, "C1005X5R1A105K050BC", "MLCC", 2000, 1.0)
c8 = Capacitor(m4.get_id(), 0.18, "2022-07-20", 12, "C2012X7R1E226M125AC", "MLCC", 1000, 22.0)
c9 = Capacitor(m5.get_id(), 0.05, "2022-06-15", 24, "ECJ-3YB1C106M", "MLCC", 4000, 10.0)
c10 = Capacitor(m5.get_id(), 0.30, "2022-09-30", 24, "ECJ-2VB1H222K", "MLCC", 2000, 2200.0)
c11 = Capacitor(m6.get_id(), 0.16, "2022-07-10", 18, "GCM155R71C104KA55D", "MLCC", 1500, 0.1)
c12 = Capacitor(m6.get_id(), 0.26, "2022-10-25", 18, "GRM155R71C104KA88D", "MLCC", 1000, 0.1)
c13 = Capacitor(m7.get_id(), 0.11, "2022-07-05", 24, "RK73H2BTTD1001F", "Thin Film", 500, 1.0)
c14 = Capacitor(m7.get_id(), 0.22, "2022-10-05", 24, "RK73H2BTTD1211F", "Thin Film", 300, 1.0)
c15 = Capacitor(m8.get_id(), 0.33, "2022-08-15", 12, "SMD0805P010S103L", "Polymer", 200, 10.0)
c16 = Capacitor(m8.get_id(), 0.48, "2022-09-25", 12, "SMD1206P010S471L", "Polymer", 100, 470.0)
c17 = Capacitor(m9.get_id(), 0.18, "2022-08-08", 18, "T491B106K016AT", "Tantalum", 500, 10.0)
c18 = Capacitor(m9.get_id(), 0.30, "2022-10-20", 18, "T491C226K016AT", "Tantalum", 300, 22.0)
c19 = Capacitor(m10.get_id(), 0.13, "2022-07-01", 24, "UVR1E102MHA", "Aluminum Electrolytic", 400, 1000.0)
c20 = Capacitor(m10.get_id(), 0.20, "2022-09-15", 24, "UVR1V102MPD", "Aluminum Electrolytic", 300, 1000.0)
capacitor = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]


#Resistor:


r1 = Resistor(m1.get_id(), 0.05, "2022-07-20", 36, "CRCW1206100RFKTA", "Thick Film", 500, 100.0)
r2 = Resistor(m1.get_id(), 0.10, "2022-09-05", 36, "CRCW1206100RJNEA", "Thick Film", 400, 1000.0)
r3 = Resistor(m2.get_id(), 0.15, "2022-08-08", 24, "ERA6YEB473V", "Thin Film", 300, 47.0)
r4 = Resistor(m2.get_id(), 0.20, "2022-10-10", 24, "ERA6YEB104V", "Thin Film", 200, 100.0)
r5 = Resistor(m3.get_id(), 0.06, "2022-08-15", 12, "EXB2HV223J", "Fusible", 500, 22.0)
r6 = Resistor(m3.get_id(), 0.12, "2022-10-05", 12, "EXB2HV102JV", "Fusible", 300, 1.0)
r7 = Resistor(m4.get_id(), 0.08, "2022-07-01", 18, "ERJ8GEYJ510V", "Thick Film", 500, 51.0)
r8 = Resistor(m4.get_id(), 0.16, "2022-09-20", 18, "ERJ8GEYJ682V", "Thick Film", 300, 6.8)
r9 = Resistor(m5.get_id(), 0.07, "2022-08-08", 24, "MCT06030C1002FP500", "Thin Film", 500, 10.0)
r10 = Resistor(m5.get_id(), 0.14, "2022-10-20", 24, "MCT06030C2700FP500", "Thin Film", 300, 270.0)
r11 = Resistor(m6.get_id(), 0.09, "2022-07-20", 36, "RC0603FR-074K7L", "Thick Film", 500, 4.7)
r12 = Resistor(m6.get_id(), 0.18, "2022-09-05", 36, "RC0603FR-076K8L", "Thick Film", 400, 6.8)
r13 = Resistor(m7.get_id(), 0.12, "2022-08-15", 12, "RK73H1HTTC2000D", "Thin Film", 500, 200.0)
r14 = Resistor(m7.get_id(), 0.24, "2022-10-05", 12, "RK73H1JTTC1003D", "Thin Film", 300, 10.0)
r15 = Resistor(m8.get_id(), 0.10, "2022-08-08", 24, "SMD0603P010TFA", "Thick Film", 500, 1.0)
r16 = Resistor(m9.get_id(), 0.05, "2022-07-01", 18, "YAGEO-RC0805FR-07100KL", "Thick Film", 500, 10.0)
r17 = Resistor(m9.get_id(), 0.10, "2022-09-20", 18, "YAGEO-RC0805FR-074K7L", "Thick Film", 300, 4.7)
r18 = Resistor(m10.get_id(), 0.15, "2022-08-08", 24, "Yageo-RC0603JR-0710KL", "Thick Film", 500, 10.0)
r19 = Resistor(m10.get_id(), 0.30, "2022-10-20", 24, "Yageo-RC0603JR-072K2L", "Thick Film", 300, 2.2)
r20 = Resistor(m2.get_id(), 0.08, "2022-07-20", 36, "CRCW1206150RFKTA", "Thick Film", 500, 100.0)
resistor = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]


#Inductor:

l1 = Inductor(m1.get_id(), 0.15, "2022-07-11", 24, "Bourns-SRR1208-100M", "Wirewound", 200, 10.0)
l2 = Inductor(m1.get_id(), 0.10, "2022-08-22", 24, "Bourns-SRR1208-220M", "Wirewound", 300, 22.0)
l3 = Inductor(m2.get_id(), 0.20, "2022-09-15", 18, "Vishay-IMC1812-8R2K", "Multilayer Ceramic", 400, 8.2)
l4 = Inductor(m2.get_id(), 0.40, "2022-10-10", 18, "Vishay-IMC1812-100UH-10", "Multilayer Ceramic", 500, 100.0)
l5 = Inductor(m3.get_id(), 0.15, "2022-07-18", 24, "Taiyo-Yuden-NRS6028-101M", "Wirewound", 200, 100.0)
l6 = Inductor(m3.get_id(), 0.20, "2022-08-30", 24, "Taiyo-Yuden-NRS6028T-151M", "Wirewound", 300, 150.0)
l7 = Inductor(m4.get_id(), 0.35, "2022-09-25", 12, "Panasonic-ELJ-FA101KF", "Ferrite Bead", 150, 100.0)
l8 = Inductor(m4.get_id(), 0.50, "2022-10-12", 12, "Panasonic-ELJ-RE101JF", "Wirewound", 250, 100.0)
l9 = Inductor(m5.get_id(), 0.20, "2022-07-25", 36, "TDK-NLCV32T-R10K-PF", "Multilayer Ceramic", 400, 10.0)
l10 = Inductor(m5.get_id(), 0.40, "2022-09-05", 36, "TDK-NLCV32T-4R7K-PF", "Multilayer Ceramic", 500, 4.7)
l11 = Inductor(m6.get_id(), 1.50, '2021-07-13', 2, 'IND-11', 'High-frequency', 1500, 1.2)
l12 = Inductor(m1.get_id(), 0.75, '2022-01-25', 1, 'IND-12', 'Power', 800, 4.7)
l13 = Inductor(m5.get_id(), 1.20, '2022-04-08', 2, 'IND-13', 'High-frequency', 1000, 2.2)
l14 = Inductor(mnf_id=m4.get_id(), price=0.95, inventory_date='2022-09-19', guarantee=1, part_number='IND-14', sub_category='Power', stock=1200, inductance=6.8)
l15 = Inductor(mnf_id=m2.get_id(), price=0.80, inventory_date='2022-11-28', guarantee=1, part_number='IND-15', sub_category='RF', stock=500, inductance=0.47)
l16 = Inductor(mnf_id=m3.get_id(), price=0.60, inventory_date='2022-12-05', guarantee=1, part_number='IND-16', sub_category='Power', stock=1500, inductance=10.0)
l17 = Inductor(mnf_id=m10.get_id(), price=1.25, inventory_date='2023-01-14', guarantee=2, part_number='IND-17', sub_category='High-frequency', stock=800, inductance=1.0)
l18 = Inductor(mnf_id=m8.get_id(), price=1.40, inventory_date='2023-02-23', guarantee=2, part_number='IND-18', sub_category='RF', stock=1000, inductance=0.33)
l19 = Inductor(mnf_id=m7.get_id(), price=0.90, inventory_date='2023-03-06', guarantee=1, part_number='IND-19', sub_category='Power', stock=1200, inductance=2.7)
l20 = Inductor(mnf_id=m9.get_id(), price=1.00, inventory_date='2023-03-22', guarantee=1, part_number='IND-20', sub_category='High-frequency', stock=500, inductance=0.68)

inductor = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]


#IC:
ic1 = IC(m1.get_id(), 1.25, "2022-02-05", 2, "LM324N", "Amplifier", 100, 1.2)
ic2 = IC(m2.get_id(), 0.85, "2021-11-20", 3, "LM555CN", "Timer", 50, 0.5)
ic3 = IC(m3.get_id(), 0.55, "2022-01-15", 2, "LM386N-1", "Audio Amplifier", 75, 0.8)
ic4 = IC(m4.get_id(), 1.35, "2022-03-10", 1, "CD4017BE", "Counter", 25, 2.0)
ic5 = IC(m5.get_id(), 0.95, "2022-02-15", 2, "NE555P", "Timer", 30, 0.5)
ic6 = IC(m6.get_id(), 2.15, "2022-03-05", 1, "MAX232CPE", "RS232 Transceiver", 20, 2.5)
ic7 = IC(m7.get_id(), 1.05, "2022-02-28", 2, "BD135", "Amplifier", 50, 1.0)
ic8 = IC(m8.get_id(), 1.95, "2022-03-15", 1, "LM317T", "Voltage Regulator", 40, 2.5)
ic9 = IC(m9.get_id(), 1.25, "2022-02-01", 2, "ATmega328P", "Microcontroller", 30, 16.0)
ic10 = IC(m10.get_id(), 0.75, "2021-12-25", 3, "74HC595", "Shift Register", 35, 2.0)
ic11 = IC(m1.get_id(), 1.45, "2022-01-10", 2, "LM324D", "Amplifier", 60, 1.2)
ic12 = IC(m2.get_id(), 1.10, "2022-02-20", 2, "LM358P", "Op-Amp", 45, 1.2)
ic13 = IC(m3.get_id(), 2.35, "2022-03-18", 1, "LM7805", "Voltage Regulator", 25, 1.0)
ic14 = IC(m4.get_id(), 1.80, "2022-03-01", 2, "CD4013BE", "Flip-Flop", 30, 2.0)
ic15 = IC(m5.get_id(), 1.25, "2022-02-05", 2, "NE555N", "Timer", 35, 0.5)
ic16 = IC(m6.get_id(), 2.65, "2022-03-25", 1, "MAX7219CNG", "LED Display Driver", 15, 8.0)
ic17 = IC(m7.get_id(), 0.95, "2022-02-15", 2, "2N3904", "Transistor", 65, 0.2)
ic18 = IC(m7.get_id(), 2.50, "2022-06-18", 3, "BRM4555C-T", "Clock Generators & Support Products", 50, 12.5)
ic19 = IC(mnf_id=m7.get_id(), price=0.75, inventory_date="2022-11-18", guarantee=3, part_number="BD9123F", sub_category="Motor Control", stock=200, clock=8.0)
ic20 = IC(mnf_id=m10.get_id(), price=0.35, inventory_date="2022-12-06", guarantee=2, part_number="ST485BN", sub_category="Interface", stock=500, clock=16.0)
ic = [ic1, ic2, ic3, ic4, ic5, ic6, ic7, ic8, ic9, ic10, ic11, ic12, ic13, ic14, ic15, ic16, ic17, ic18, ic19, ic20]


#Sensor Samples

s1 = Sensor(m1.get_id(), 1.99, "2022-01-05", 2, "SNS001", "Temperature Sensor", 50, "Thermistor")
s2 = Sensor(m2.get_id(), 3.49, "2022-03-10", 1, "SNS002", "Humidity Sensor", 20, "Capacitive")
s3 = Sensor(m3.get_id(), 2.99, "2022-02-15", 3, "SNS003", "Light Sensor", 40, "Photodiode")
s4 = Sensor(m4.get_id(), 5.99, "2022-04-20", 2, "SNS004", "Pressure Sensor", 10, "Piezoresistive")
s5 = Sensor(m5.get_id(), 4.99, "2022-05-02", 1, "SNS005", "Magnetic Sensor", 30, "Hall Effect")
s6 = Sensor(m6.get_id(), 7.99, "2022-06-08", 2, "SNS006", "Gas Sensor", 15, "Electrochemical")
s7 = Sensor(m7.get_id(), 2.49, "2022-07-12", 3, "SNS007", "Proximity Sensor", 50, "Inductive")
s8 = Sensor(m8.get_id(), 6.99, "2022-08-18", 1, "SNS008", "Accelerometer", 20, "Piezoelectric")
s9 = Sensor(m9.get_id(), 9.99, "2022-09-25", 2, "SNS009", "Gyroscope", 10, "MEMS")
s10 = Sensor(m10.get_id(), 8.49, "2022-10-30", 3, "SNS010", "Ultrasonic Sensor", 30, "Transmitter-Receiver")
s11 = Sensor(m1.get_id(), 4.99, "2022-11-05", 2, "SNS011", "Temperature Sensor", 25, "Thermocouple")
s12 = Sensor(m2.get_id(), 6.49, "2022-12-10", 1, "SNS012", "Humidity Sensor", 15, "Resistive")
s13 = Sensor(m3.get_id(), 5.99, "2023-01-15", 3, "SNS013", "Light Sensor", 30, "Photoresistor")
s14 = Sensor(m4.get_id(), 8.99, "2023-02-20", 2, "SNS014", "Pressure Sensor", 10, "Capacitive")
s15 = Sensor(m3.get_id(), 2.55, "2022-07-15", 2, "KM500", "Motion Sensor", 500, "Accelerometer")
s16 = Sensor(m4.get_id(), 1.75, "2022-08-22", 1, "BP320", "Barometric Pressure Sensor", 320, "Pressure")
s17 = Sensor(m5.get_id(), 3.99, "2022-09-07", 3, "HTH1", "Humidity and Temperature Sensor", 150, "Humidity and Temperature")
s18 = Sensor(m6.get_id(), 0.99, "2022-10-02", 2, "LS100", "Light Sensor", 200, "Light")
s19 = Sensor(m7.get_id(), 2.25, "2022-11-10", 1, "MS200", "Magnetic Sensor", 100, "Magnetic")
s20 = Sensor(m8.get_id(), 1.50, "2022-12-25", 2, "TS300", "Touch Sensor", 50, "Capacitive Touch")
sensor = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20]

# Shuffle the lists
random.shuffle(sensor)
random.shuffle(ic)
random.shuffle(inductor)
random.shuffle(resistor)
random.shuffle(capacitor)

def get_connection():
    conn = sqlite3.connect('models/db/electronic_store_with_classes.db')
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
        push(row)

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
        push(row)

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
        push(row)

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
        push(row)

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
        push(row)

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
    for row in ic:
        push(row)

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
 

from pushpull.Pushpulltosql import push