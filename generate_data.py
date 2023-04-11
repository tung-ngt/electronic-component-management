import random
import pickle
import os
from models.domains import Capacitor, Resistor, Inductor, Sensor, IC, Manufacturer, Customer, Order

customers = [Customer("C001", "Steven Johnston", "505-261-9544"),
Customer("C002", "Emmett Rogers", "+1 202-918-2132"),
Customer("C003", "Ethan Bright", "+84 394 568 234"),
Customer("C004", "Darian Vargas", "361-760-7352"),
Customer("C005", "Ally Cooper", "413-283-3474"),
Customer("C006", "Sloane Carlson", "973-797-1294"),
Customer("C007", "Katelyn Ramsey", "919-430-0596"),
Customer("C008", "Kaylynn Pierce", "484-651-6061"),
Customer("C009", "Gisselle Carrillo", "817-250-8146"),
Customer("C010", "Abraham Benson", "615-656-5114"),]


capacitors_list = ['MLCC', 'Thin Film', 'Tantalum', 'Aluminum Electrolytic', 'Polymer']
resistors_list = ['Thick Film', 'Fusible', 'Thin Film']
inductors_list = ['Power', 'Multilayer Ceramic', 'Wirewound', 'High-frequency', 'Ferrite Bead', 'RF']
sensors_list = ['Humidity and Temperature Sensor', 'Light Sensor', 'Temperature Sensor', 'Proximity Sensor', 'Pressure Sensor', 'Accelerometer', 'Gas Sensor', 'Motion Sensor', 'Touch Sensor', 'Magnetic Sensor', 'Humidity Sensor', 'Barometric Pressure Sensor', 'Gyroscope', 'Ultrasonic Sensor']

ics_list = ['Audio Amplifier', 'Op-Amp', 'Shift Register', 'Timer', 'Amplifier', 'LED Display Driver', 'Interface', 'Counter', 'Flip-Flop', 'Motor Control', 'Microcontroller', 'Voltage Regulator', 'Transistor', 'RS232 Transceiver', 'Clock Generators & Support Products']

sensor_types_list = ["Thermistor", "Capacitive", "Photodiode", "Piezoresistive", "Hall Effect", "Electrochemical",
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

#sensor_part_numbers = list(set(sensor_part_numbers))
#ic_part_numbers = list(set(ic_part_numbers))
#inductor_part_numbers = list(set(inductor_part_numbers))
#resistor_part_numbers = list(set(resistor_part_numbers))
#capacitor_part_numbers = list(set(capacitor_part_numbers))

#manu_cap = []
#for i in capacitor_part_numbers:
#    manu_cap.append(i.split(' ', 1)[0])

#manu_res = []
#for i in resistor_part_numbers:
#    manu_res.append(i.split(' ', 1)[0])

#manu_ind = []
#for i in inductor_part_numbers:
#    manu_ind.append(i.split(' ', 1)[0])

#manu_ic = []
#for i in ic_part_numbers:
#    manu_ic.append(i.split(' ', 1)[0])

#manu_sen = []   
#for i in sensor_part_numbers:
#    manu_sen.append(i.split(' ', 1)[0])

#manufacturers = manu_cap + manu_res + manu_ind + manu_ic + manu_sen
#manufacturers = list(set(manufacturers))
#manufacturers.sort()
#print(manufacturers)
#print(len(manufacturers))

#Manufacturer:
m1 = Manufacturer("M001", "API Technologies Corp", "United States", "api.png")
m2 = Manufacturer("M002", "AVX Corporation", "United States", 'avx.png')
m3 = Manufacturer("M003", "Allegro MicroSystems", "United States", "allegro.png")
m4 = Manufacturer("M004", "Amphenol", "United States", "amphenol.png")
m5 = Manufacturer("M005", "Analog", "United States", "analog.png")
m6 = Manufacturer("M006", "Bosch", "Germany", "bosch.png")
m7 = Manufacturer("M007", "Bourns", "United States", 'bourns.png')
m8 = Manufacturer("M008", "Caddock", "United States", 'caddock.png')
m9 = Manufacturer("M009", "Coilcraft", "United States", 'coilcraft.png')
m10 = Manufacturer("M010", "Cypress", "United States", "cypress.png")
m11 = Manufacturer("M011", "Honeywell", "United State", "honeywell.png")
m12 = Manufacturer("M012", "IRC", "United Kingdom", "irc.png")
m13 = Manufacturer("M013", "Infineon", "Germany", "infineon.png")
m14 = Manufacturer("M014", "IsabellenhUtte", "United States", 'isabellenhutte.png')
m15 = Manufacturer("M015", "Iskra", "Slovenia", "iskra.png")
m16 = Manufacturer("M016", "Johanson Technology", "United States", "johanson.png")
m17 = Manufacturer("M017", "KEMET Corporation", "United States", 'kemet.png')
m18 = Manufacturer("M018", "KOA Speer", "Japan", "koa.png")
m19 = Manufacturer("M019", "Linear Electric Inc", "United States", "linear.png")
m20 = Manufacturer("M020", "Maxim Integrated", "United States", "maxim.png")
m21 = Manufacturer("M021", "Microchip Technology", "United States", "microchip.png")
m22 = Manufacturer("M022", "Microsemi", "United States", 'microsemi.png')
m23 = Manufacturer("M023", "Murata Manufacturing Co., Ltd.", "Japan", 'murata.png')
m24 = Manufacturer("M024", "NIC Components Corp", "United States", "nic.png")
m25 = Manufacturer("M025", "NTE Electronics Inc", "United States", "nte.png")
m26 = Manufacturer("M026", "NXP Semiconductors", "Netherlands", "nxp.png")
m27 = Manufacturer("M027", "Nichicon", "Japan", 'nichicon.png')
m28 = Manufacturer("M028", "ON Semiconductor", "United States", "on.png")
m29 = Manufacturer("M029", "Ohmite", "United States", 'ohmite.png')
m30 = Manufacturer("M030", "Omron", "Japan", 'omron.png')
m31 = Manufacturer("M031", "Panasonic Corporation", "Japan", 'panasonic.png')
m32 = Manufacturer("M032", "RCD Components", "United States", 'rcd.png')
m33 = Manufacturer("M033", "Rohm Semiconductor", "Japan", 'rohm.png')
m34 = Manufacturer("M034", "Renesas Electronics", "Japan", 'renesas.png')
m35 = Manufacturer("M035", "ROYALOHM", "Thailand", 'royalohm.png')
m36 = Manufacturer("M036", "Rubycon", "Japan", 'rubycon.png')
m37 = Manufacturer("M037", "STMicroelectronics", "Switzerland", 'st.png')
m38 = Manufacturer("M038", "Samsung Electronics", "South Korea", "samsung.png")
m39 = Manufacturer("M039", "Sensirion", "Switzerland", "sensirion.png")
m40 = Manufacturer("M040", "Simpson", "United States", "simpson.png")
m41 = Manufacturer("M041", "Stackpole International Inc", "Hong Konh", "stackpole.png")
m42 = Manufacturer("M042", "Sumida Corporation", "Japan", 'sumida.png')
m43 = Manufacturer("M043", "Susumu Co., Ltd.", "Japan", 'susumu.png')
m44 = Manufacturer("M044", "TDK Corporation", "Japan", 'tdk.png')
m45 = Manufacturer("M045", "TE Connectivity", "Switzerland", 'te.png')
m46 = Manufacturer("M046", "TT Electronics", "United Kingdom", "tt.png")
m47 = Manufacturer("M047", "Taiyo Yuden", "Japan", 'taiyo.png')
m48 = Manufacturer("M048", "Texas Instruments", "United States", "ti.png")
m49 = Manufacturer("M049", "Viking Tech Corporation", "China", 'viking.png')
m50 = Manufacturer("M050", "Vishay Intertechnology, Inc.", "United States", 'vishay.png')
m51 = Manufacturer("M051", "Walsin Technology Corp", "Taiwan", 'walsin.png')
m52 = Manufacturer("M052", "Wurth Elektronik", "Germany", 'wurth.png')
m53 = Manufacturer("M053", "Yageo Corporation", "Taiwan", 'yageo.png')

manufacturers = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10,
                 m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, 
                 m21, m22, m23, m24, m25, m26, m27, m28, m29, m30,
                 m31, m32, m33, m34, m35, m36, m37, m38, m39, m40,
                 m41, m42, m43, m44, m45, m46, m47, m48, m49, m50,
                 m51, m52, m53]



capacitor_images = [f"C{n}.png" for n in range(1, 11)]
resistor_images = [f"R{n}.png" for n in range(1, 11)]
inductor_images = [f"I{n}.png" for n in range(1, 11)]
sensor_images = [f"S{n}.png" for n in range(1, 11)]
ic_images = [f"IC{n}.png" for n in range(1, 11)]



capacitor_samples = []
for i in range(100):
    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)

    part_number = random.choice(capacitor_part_numbers) + str(i)
    mnf = part_number.split(' ', 1)[0]

    mnf_id = None
    for m in manufacturers:
        if m.get_name().split(' ', 1)[0] == mnf:
            mnf_id = m.get_id()
            break

    sub_category = random.choice(capacitors_list)
    stock = random.randint(100, 1000)
    capacitance = round(random.uniform(0.1, 100), 2)
    image_path = random.choice(capacitor_images) 
    
    capacitor_samples.append(Capacitor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, capacitance, image_path))



resistor_samples = []
for i in range(120):

    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)

    part_number = random.choice(capacitor_part_numbers) + str(i)
    mnf = part_number.split(' ', 1)[0]

    mnf_id = None
    for m in manufacturers:
        if m.get_name().split(' ', 1)[0] == mnf:
            mnf_id = m.get_id()
            break

    sub_category = random.choice(resistors_list)
    stock = random.randint(100, 1000)
    resistance = round(random.uniform(0.1, 100), 2)
    image_path = random.choice(resistor_images)

    
    resistor_samples.append(Resistor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, resistance, image_path))

inductor_samples = []
for i in range(120):

    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)

    part_number = random.choice(capacitor_part_numbers) + str(i)
    mnf = part_number.split(' ', 1)[0]

    mnf_id = None
    for m in manufacturers:
        if m.get_name().split(' ', 1)[0] == mnf:
            mnf_id = m.get_id()
            break

    sub_category = random.choice(inductors_list)
    stock = random.randint(100, 1000)
    inductance = round(random.uniform(0.1, 100), 2)
    image_path = random.choice(inductor_images)

    
    inductor_samples.append(Inductor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, inductance, image_path))


sensor_samples = []
for i in range(120):

    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)

    part_number = random.choice(capacitor_part_numbers) + str(i)
    mnf = part_number.split(' ', 1)[0]

    mnf_id = None
    for m in manufacturers:
        if m.get_name().split(' ', 1)[0] == mnf:
            mnf_id = m.get_id()
            break

    sub_category = random.choice(sensors_list)
    stock = random.randint(100, 1000)
    sensor_type = random.choice(sensor_types_list)
    image_path = random.choice(sensor_images)
    
    sensor_samples.append(Sensor(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, sensor_type, image_path))


ic_samples = []
for i in range(120):

    price = round(random.uniform(0.1, 10), 2)
    inventory_date = f"{random.randint(2020, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    guarantee = random.randint(6, 24)

    part_number = random.choice(capacitor_part_numbers) + str(i)
    mnf = part_number.split(' ', 1)[0]

    mnf_id = None
    for m in manufacturers:
        if m.get_name().split(' ', 1)[0] == mnf:
            mnf_id = m.get_id()
            break

    sub_category = random.choice(ics_list)
    stock = random.randint(100, 1000)
    clock = round(random.uniform(0.1, 100), 2)
    image_path = random.choice(ic_images)
    
    ic_samples.append(IC(mnf_id, price, inventory_date, guarantee, part_number, sub_category, stock, clock, image_path))



orders = [
Order("O001", "C001", {ic_samples[2].get_part_number(): 3, inductor_samples[80].get_part_number(): 4, capacitor_samples[15].get_part_number(): 2}, "2022-03-05"),
Order("O003", "C002", {resistor_samples[6].get_part_number() : 5, ic_samples[15].get_part_number(): 6, sensor_samples[10].get_part_number(): 1}, "2023-01-15"),
Order("O007", "C006", {sensor_samples[45].get_part_number(): 1}, "2021-12-30"),
Order("O002", "C001", {inductor_samples[20].get_part_number() : 2}, "2022-06-19"),
Order("O004", "C003", {capacitor_samples[62].get_part_number(): 5, sensor_samples[40].get_part_number(): 4}, "2022-08-25"),
Order("O006", "C005", {sensor_samples[45].get_part_number(): 10}, "2022-04-14"),
Order("O008", "C006", {sensor_samples[40].get_part_number(): 6}, "2022-03-05"),
Order("O005", "C004", {sensor_samples[60].get_part_number(): 4, sensor_samples[92].get_part_number(): 5}, "2023-02-01"),
Order("O012", "C010", {capacitor_samples[40].get_part_number(): 3}, "2022-01-31"),
Order("O009", "C009", {resistor_samples[40].get_part_number(): 3}, "2022-03-18"),
Order("O010", "C008", {ic_samples[40].get_part_number(): 2}, "2022-03-05"),
Order("O011", "C007", {inductor_samples[40].get_part_number(): 1}, "2021-10-22"),
]



## Shuffle the lists
random.shuffle(sensor_samples)
random.shuffle(ic_samples)
random.shuffle(inductor_samples)
random.shuffle(resistor_samples)         
random.shuffle(capacitor_samples)
random.shuffle(orders)
random.shuffle(customers)
random.shuffle(manufacturers)


if not os.path.isdir("./generated_data"):
    os.makedirs("./generated_data")

# Pickle all lists
with open('./generated_data/sensors.pickle', 'wb') as f:
    pickle.dump(sensor_samples, f)

with open('./generated_data/ics.pickle', 'wb') as f:
    pickle.dump(ic_samples, f)

with open('./generated_data/inductors.pickle', 'wb') as f:
    pickle.dump(inductor_samples, f)

with open('./generated_data/resistors.pickle', 'wb') as f:
    pickle.dump(resistor_samples, f)

with open('./generated_data/capacitors.pickle', 'wb') as f:
    pickle.dump(capacitor_samples, f)

with open('./generated_data/manufacturers.pickle', 'wb') as f:
    pickle.dump(manufacturers, f)

with open('./generated_data/customers.pickle', 'wb') as f:
    pickle.dump(customers, f)

with open('./generated_data/orders.pickle', 'wb') as f:
    pickle.dump(orders, f)


