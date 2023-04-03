import random
import pickle
from os import listdir
from os.path import isfile, join

# abspath to models
import os, sys
sys.path.append(os.path.abspath(r'C:\Users\ciltr\Desktop\USTH\Semester 2\Python\Python project\electronic-store'))

from models.domains import Capacitor, Resistor, Inductor, Sensor, IC, Manufacturer
from models.db.Utils_database import get_connection
from models.pushpull.Pushpulltosql import push, pull



#Manufacturer:
m1 = Manufacturer("M001", "AVX Corporation", "United States", 'avx.png')
m2 = Manufacturer("M002", "KEMET Corporation", "United States", 'kemet.png')
m3 = Manufacturer("M003", "Yageo Corporation", "Taiwan", 'yageo.png')
m4 = Manufacturer("M004", "TDK Corporation", "Japan", 'tdk.png')
m5 = Manufacturer("M005", "Panasonic Corporation", "Japan", 'panasonic.png')
m6 = Manufacturer("M006", "Murata Manufacturing Co., Ltd.", "Japan", 'murata.png')
m7 = Manufacturer("M007", "Rohm Semiconductor", "Japan", 'rohm.png')
m8 = Manufacturer("M008", "Vishay Intertechnology, Inc.", "United States", 'vishay.png')
m9 = Manufacturer("M009", "Infineon Technologies AG", "Germany", 'infineon.png')
m10 = Manufacturer("M010", "STMicroelectronics", "Switzerland", 'st.png')

manufacturer = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]





Capacitor_list = ['MLCC', 'Thin Film', 'Tantalum', 'Aluminum Electrolytic', 'Polymer']
Resistor_list = ['Thick Film', 'Fusible', 'Thin Film']
Inductor_list = ['Power', 'Multilayer Ceramic', 'Wirewound', 'High-frequency', 'Ferrite Bead', 'RF']
Sensor_list = ['Humidity and Temperature Sensor', 'Light Sensor', 'Temperature Sensor', 'Proximity Sensor', 'Pressure Sensor', 'Accelerometer', 'Gas Sensor', 'Motion Sensor', 'Touch Sensor', 'Magnetic Sensor', 'Humidity Sensor', 'Barometric Pressure Sensor', 'Gyroscope', 'Ultrasonic Sensor']

IC_list = ['Audio Amplifier', 'Op-Amp', 'Shift Register', 'Timer', 'Amplifier', 'LED Display Driver', 'Interface', 'Counter', 'Flip-Flop', 'Motor Control', 'Microcontroller', 'Voltage Regulator', 'Transistor', 'RS232 Transceiver', 'Clock Generators & Support Products']

sensor_type_list = ["Thermistor", "Capacitive", "Photodiode", "Piezoresistive", "Hall Effect", "Electrochemical",
                    "Inductive", "Piezoelectric", "MEMS", "Transmitter-Receiver", "Thermocouple", "Resistive", 
                    "Photoresistor", "Accelerometer", "Pressure", "Humidity and Temperature", "Light",
                    "Capacitive Touch"]



resistor_part_numbers = [
    'Yageo RC0805FR-071K5L',
    'Vishay CRCW0805100RFKEA',
    'Bourns CR1206-FX-1000ELF',
    'KOA Speer RK73H1JTTD1003F',
    'Panasonic ERJ-6GEYJ101V',
    'Susumu RG2012P-221-B-T5',
    'Wurth Elektronik 742792010',
    'TE Connectivity CFR-25JB-52-47K',
    'TT Electronics MCF 0.25W 100K 1%',
    'Ohmite 5FR500JB',
    'Caddock MP930-5.10K-1%',
    'KEMET C0805C104K5RAC',
    'Stackpole RMCF 0805JT-100K',
    'Isabellenhutte PMR20HZPJU1002',
    'RCD Components 0402FR-072K2L',
    'NTE Electronics QW210000',
    'Johanson Technology 500R12S2R4BV4T',
    'ROHM MCR18EZHFX6493',
    'Simpson 3-02-0304',
    'API Delevan RM10JT3R3CT',
    'Royal Ohm 1/2W 470R J',
    'Panasonic ERA-2AEB232X',
    'Yageo RC0402JR-0710KL',
    'Vishay MRS25000C5609FCT00',
    'TE Connectivity RBK0225BKWH100',
    'KEMET C1206C104K5RACTU',
    'IRC / TT Electronics LR2512-R05FW',
    'Stackpole RMCF 1/8W 330K 1%',
    'Susumu RG3216P-1004-B-T5',
    'Iskra RM73B2AT330J',
    'Walsin Technology WR06X1001FTL',
    'KOA Speer RK73H2BTTD1503F',
    'Bourns CRA06S08312K0JTA',
    'Ohmite 15FR050E',
    'RCD Components MFR-25FRF-100R',
    'TT Electronics MCR10EZPJ471',
    'Viking Tech RMCF 0402JT-2K20',
    'Vishay CRCW1210180KFKTA',
    'Yageo RC0603FR-072K7L',
    'Wurth Elektronik 74437304100'
]

capacitor_part_numbers = [
    'Murata GRM188R71H103KA01D',
    'AVX 06035C102KAT2A',
    'TDK C2012X5R1A226M125AC',
    'KEMET C0805C104K5RAC',
    'Vishay K104M15X7RF53L2',
    'NIC Components NACZ101M25V6.3X6.3TR13F',
    'Panasonic EEU-FM1H221L',
    'Samsung CL05C221JB5NNNC',
    'Rubycon YXF Series 50V 220uF',
    'Nichicon UPM2A101MPD6',
    'Wurth Elektronik 885012206027',
    'Murata GRM155R71C104KA88D',
    'AVX TAJB106K010RNJ',
    'TDK C3225X5R1E226M',
    'KEMET T520B476M006ATE070',
    'Vishay MAL215691102E3',
    'NIC Components NACZ680M50V6.3X6.3TR13F',
    'Panasonic ECA-1HM100I',
    'Samsung CL10C470JB8NNNC',
    'Rubycon YXA Series 50V 10uF',
    'Nichicon UVZ2A100MPD',
    'Wurth Elektronik 885060211006',
    'Murata GRM155R60J106ME44D',
    'AVX SR211A102KAT',
    'TDK C5750X7S2A475M',
    'KEMET T530X477M006ATE010',
    'Vishay CRCW06031K00FKEA',
    'NIC Components NACE101M25V4X5.5TR13F',
    'Panasonic EEEFK1C101P',
    'Samsung CL21C471JBANNNC',
    'Rubycon YXE Series 25V 22uF',
    'Nichicon UPW1J102MHD6',
    'Wurth Elektronik 885012204003'
]

sensor_part_numbers = [
    'Omron E3S-AR71',
    'Sensirion SHT31-DIS-B',
    'Honeywell HSCDRRN001PD2A5',
    'Bosch BMP280',
    'TE Connectivity 6-2230041-1',
    'STMicroelectronics LIS3DH',
    'Murata NDC15-AA',
    'Amphenol Advanced Sensors SM-UART-04L',
    'Texas Instruments TMP36GT9Z',
    'Infineon Technologies TLE493D-A1B6',
    'NXP Semiconductors MPL3115A2',
    'TE Connectivity 3-1393812-3',
    'Maxim Integrated DS18B20Z+T&R',
    'Omron D6T-1A-01',
    'Honeywell HMC5883L',
    'Bourns Inc. PDB182-GTR02-504B0-103',
    'Analog Devices ADXL345BCCZ-RL7',
    'Murata NCP15WB473D03RC',
    'TE Connectivity 1825919-1',
    'STMicroelectronics LPS22HBTR',
    'Amphenol Advanced Sensors NPA-201B-015D',
    'Infineon Technologies XENSIV DPS368',
    'NXP Semiconductors MMA8451QT',
    'TE Connectivity 6-1393809-7',
    'Maxim Integrated MAX31855KASA+',
    'Omron E2E2-X2C1',
    'Honeywell SSCMRNN001PG2A5',
    'Bosch BMI088',
    'Analog Devices ADXL375BCPZ',
    'Murata NCS1K05T',
    'TE Connectivity 1825100-1',
    'STMicroelectronics LSM6DS3TR',
    'Amphenol Advanced Sensors T9602-3-D-1',
    'Infineon Technologies XENSIV TLI4970-D050T4',
    'NXP Semiconductors MMA9555L',
    'TE Connectivity 6-2230820-5'
]
ic_part_numbers = [
    'Microchip Technology ATmega328P-PU',
    'Texas Instruments LM324N',
    'Analog Devices ADXL355BCCZ-3',
    'Maxim Integrated MAX232ESE+T',
    'ON Semiconductor MC7805CTG',
    'Cypress Semiconductor CY8C4147AZI-S443',
    'Infineon Technologies IRF540NPBF',
    'STMicroelectronics STM32F103C8T6',
    'NXP Semiconductors LPC1768FBD100',
    'Microsemi Corporation APT1001RKN',
    'Allegro MicroSystems A4940KJPTR-T',
    'Linear Technology LT3080ETS8#PBF',
    'Renesas Electronics R5F100LEAFA#V0',
    'Maxim Integrated MAX7219CNG+',
    'Texas Instruments SN74LS08N',
    'Analog Devices AD8317ACPZ',
    'Microchip Technology MCP602-I/P',
    'ON Semiconductor LM358N',
    'Cypress Semiconductor CY8C4146AZI-S453',
    'Infineon Technologies BSS138N',
    'STMicroelectronics STM32F401RE',
    'NXP Semiconductors LPC2148FBD64',
    'Microsemi Corporation APT1001M2LLG',
    'Allegro MicroSystems A4988SETTR-T',
    'Linear Technology LT3081EDD#PBF',
    'Renesas Electronics R5F100PJAFB#V0',
    'Maxim Integrated MAX7221CNG+',
    'Texas Instruments SN',
    'Microchip Technology ATmega328P-PU',
    'Texas Instruments LM324N',
    'Analog Devices ADXL355BCCZ-3',
    'Maxim Integrated MAX232ESE+T',
    'ON Semiconductor MC7805CTG',
    'Cypress Semiconductor CY8C4147AZI-S443',
    'Infineon Technologies IRF540NPBF',
    'STMicroelectronics STM32F103C8T6',
    'NXP Semiconductors LPC1768FBD100',
    'Microsemi Corporation APT1001RKN',
    'Allegro MicroSystems A4940KJPTR-T',
    'Linear Technology LT3080ETS8#PBF',
    'Renesas Electronics R5F100LEAFA#V0',
    'Maxim Integrated MAX7219CNG+',
    'Texas Instruments SN74LS08N',
    'Analog Devices AD8317ACPZ',
    'Microchip Technology MCP602-I/P',
    'ON Semiconductor LM358N',
    'Cypress Semiconductor CY8C4146AZI-S453',
    'Infineon Technologies BSS138N',
    'STMicroelectronics STM32F401RE',
    'NXP Semiconductors LPC2148FBD64',
    'Microsemi Corporation APT1001M2LLG',
    'Allegro MicroSystems A4988SETTR-T',
    'Linear Technology LT3081EDD#PBF',
    'Renesas Electronics R5F100PJAFB#V0',
    'Maxim Integrated MAX7221CNG+',
    'Texas Instruments SN7404N',
    'Analog Devices ADXL345BCCZ-RL7',
    'Microchip Technology PIC16F877A-I/P',
    'ON Semiconductor LM317T',
    'Cypress Semiconductor CY8C4245AXI-483',
    'Infineon Technologies BSS84P',
    'STMicroelectronics STM32F407VGT6',
    'NXP Semiconductors LPC1114FN28',
    'Microsemi Corporation APT1002RKN',
    'Allegro MicroSystems ACS758LCB-050B-PFF-T',
    'Linear Technology LTC3106EDE#PBF',
    'Renesas Electronics R5F104CAGSP#U0',
    'Maxim Integrated MAX3232CSE+T',
    'Texas Instruments CD4011BE',
    'Analog Devices ADMP401ACEZ-RL7',
    'Microchip Technology ATtiny85-20PU',
    'ON Semiconductor LM7805CT',
    'Cypress Semiconductor CY8C4247AZI-M485',
    'Infineon Technologies BC817-40W',
    'STMicroelectronics STM32F429ZIT6',
    'NXP Semiconductors LPC4370FET100',
    'Microsemi Corporation APT1002M3LLG',
    'Allegro MicroSystems ACS758ECB-100B-PFF-T',
    'Linear Technology LT1512IS8#PBF',
    'Renesas Electronics R5F10KCLAFP#V0'
]
inductor_part_numbers = [
    'Bourns SRN8040-2R2M',
    'Murata LQW18ANR22J00D',
    'Vishay Dale IHLP2525CZER1R0M01',
    'Taiyo Yuden NR8040T2R2N',
    'TDK Corporation VLF3010AT-2R2N1R0',
    'Wurth Elektronik 7443550470',
    'Sumida CDRH6D28NP-220NC',
    'Coilcraft XEL6030-102MEC',
    'Panasonic ELL6RH2R2M',
    'AVX Corporation LQW2BASR22J00L',
    'KEMET LQG18HN2R2J00D',
    'Murata LQH32CN2R2M23L',
    'TDK Corporation NL453232T-2R2J-PF',
    'Vishay Dale IHD1EBR2R2L',
    'Wurth Elektronik 7443760633',
    'Bourns SRN4018-2R2M',
    'Taiyo Yuden NR4018T2R2N',
    'TDK Corporation VLS201610ET-2R2N',
    'Coilcraft XAL5030-222MEC',
    'Panasonic ELJ-NJR22KF',
    'AVX Corporation LQW2BHN2R2M01L',
    'KEMET LQH43MN2R2K03L',
    'Murata LQG21NR22K10T1M',
    'TDK Corporation MLF1608E2R2J',
    'Vishay Dale IHLP2525CZ01R2M01',
    'Wurth Elektronik 744313220',
    'Sumida CDRH4D28NP-2R2NC',
    'Bourns SRU8043-2R2Y',
    'Taiyo Yuden NR8040T2R2N',
    'TDK Corporation VLF3010AT-2R2N1R0',
    'Coilcraft XFL3012-222MEC',
    'Panasonic ELLATV2R2N',
    'AVX Corporation LQH3NPN2R2MM0L',
    'KEMET LQG15HS2R2J02D',
    'Murata LQH31MN2R2K03L',
    'TDK Corporation NLV25T-2R2J-PF',
    'Vishay Dale IHD1EBR2R2L',
    'Wurth Elektronik 744383140068',
    'Sumida CDRH6D28NP-2R2NC',
    'Bourns SDE0805A-2R2M',
    'Taiyo Yuden NR8040T2R2N',
    'TDK Corporation VLF3010AT-2R2N1R0',
    'Coilcraft XPL4020-222MEC',
    'Panasonic ELL-6RH2R2N',
    'AVX Corporation LQW15AN2R2J00D',
    'KEMET LQH32CN2R2M23L'
]

sensor_part_numbers = list(set(sensor_part_numbers))
ic_part_numbers = list(set(ic_part_numbers))
inductor_part_numbers = list(set(inductor_part_numbers))
resistor_part_numbers = list(set(resistor_part_numbers))
capacitor_part_numbers = list(set(capacitor_part_numbers))

capacitor_image_path = './images/components/Capacitor'
capacitor_images = [f for f in listdir(capacitor_image_path) if isfile(join(capacitor_image_path, f))]

resistor_image_path = './images/components/Resistor'
resistor_images = [f for f in listdir(resistor_image_path) if isfile(join(resistor_image_path, f))]

inductor_image_path = './images/components/Inductor'
inductor_images = [f for f in listdir(inductor_image_path) if isfile(join(inductor_image_path, f))]

sensor_image_path = './images/components/Sensor'
sensor_images = [f for f in listdir(sensor_image_path) if isfile(join(sensor_image_path, f))]

ic_image_path = './images/components/IC'
ic_images = [f for f in listdir(ic_image_path) if isfile(join(ic_image_path, f))]


capacitor_samples = []
for i in range(100):
    mnf_id = random.choice(manufacturer).get_id()
    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)
    part_number = random.choice(capacitor_part_numbers) + str(i)
    sub_category = random.choice(Capacitor_list)
    stock = random.randint(100, 1000)
    capacitance = round(random.uniform(0.1, 100), 2)
    image_path = 'Capacitor' + '/' + random.choice(capacitor_images) 
    
    capacitor_samples.append(Capacitor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, capacitance, image_path))


resistor_samples = []
for i in range(120):
    mnf_id = random.choice(manufacturer).get_id()
    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)
    part_number = random.choice(resistor_part_numbers) + str(i)
    sub_category = random.choice(Resistor_list)
    stock = random.randint(100, 1000)
    resistance = round(random.uniform(0.1, 100), 2)
    image_path = 'Resistor' + '/' +random.choice(resistor_images)
    
    resistor_samples.append(Resistor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, resistance, image_path))

inductor_samples = []
for i in range(120):
    mnf_id = random.choice(manufacturer).get_id()
    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)
    part_number = random.choice(inductor_part_numbers) + str(i)
    sub_category = random.choice(Inductor_list)
    stock = random.randint(100, 1000)
    inductance = round(random.uniform(0.1, 100), 2)
    image_path = 'Inductor' + '/' +random.choice(inductor_images)
    
    inductor_samples.append(Inductor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, inductance, image_path))


sensor_samples = []
for i in range(120):
    mnf_id = random.choice(manufacturer).get_id()
    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)
    part_number = random.choice(sensor_part_numbers) + str(i)
    sub_category = random.choice(Sensor_list)
    stock = random.randint(100, 1000)
    sensor_type = random.choice(sensor_type_list)
    image_path = 'Sensor' + '/' +random.choice(sensor_images)
    
    sensor_samples.append(Sensor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, sensor_type, image_path))


ic_samples = []
for i in range(120):
    mnf_id = random.choice(manufacturer).get_id()
    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)
    part_number = random.choice(ic_part_numbers) + str(i)
    sub_category = random.choice(IC_list)
    stock = random.randint(100, 1000)
    clock = round(random.uniform(0.1, 100), 2)
    image_path = 'IC' + '/' + random.choice(ic_images)
    
    ic_samples.append(IC(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, clock, image_path))





## Shuffle the lists
#random.shuffle(sensor_samples)
#random.shuffle(ic_samples)
#random.shuffle(inductor_samples)
#random.shuffle(resistor_samples)         
#random.shuffle(capacitor_samples)


# Pickle all lists
with open('./data/sensor.pickle', 'wb') as f:
    pickle.dump(sensor_samples, f)

with open('./data/ic.pickle', 'wb') as f:
    pickle.dump(ic_samples, f)

with open('./data/inductor.pickle', 'wb') as f:
    pickle.dump(inductor_samples, f)

with open('./data/resistor.pickle', 'wb') as f:
    pickle.dump(resistor_samples, f)

with open('./data/capacitor.pickle', 'wb') as f:
    pickle.dump(capacitor_samples, f)

with open('./data/manufacturer.pickle', 'wb') as f:
    pickle.dump(manufacturer, f)



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

print(len(ic))