#Data manufacturer
data_manufacturer =[ 
        ['id','name','country'],
        ['ABC123','ABC Manufacturing','USA'],
        ['DEF456','DEF Manufacturing','Canada'],
        ['GHI789','GHI Manufacturing','Germany'],
        ['JKL012','JKL Manufacturing','Japan'],
        [ 'MNO345','MNO Manufacturing','USA'],
        ['PQR678','PQR Manufacturing','Canada'],
        ['STU901','STU Manufacturing','France'],
        ['VWX234','VWX Manufacturing','Poland'],
        [ 'YZA567','YZA Manufacturing','Philippines'],
        ['BCD890','BCD Manufacturing','UK'],
        ['EFG123','EFG Manufacturing','Ukraine'],
        [ 'HIJ456','HIJ Manufacturing','Vietnam'],
        ['KLM789','KLM Manufacturing','Thailand'],
        ['NOP012','NOP Manufacturing','Laos'],
        ['QRS345','QRS Manufacturing','Cambodia'],
        ['TUV678','TUV Manufacturing','Singapore'],
        [ 'WXY901','WXY Manufacturing','South Korea'],
        ['ZAB234','ZAB Manufacturing','Nepal'],
        ['CDE567','CDE Manufacturing','India'],
        ['FGH890','FGH Manufacturing','Qatar']
    ]
#Data capacitor
data_capactior = [
    ['mnf_id', 'price', 'inventory_date', 'guarantee', 'part_number', 'sub_category', 'stock', 'capacitance'],
    ['ABC123', 90, '2022-03-15', 12, 'PRT344', 'CAP TRIMMER ', 500,  '5.1NF'],
    ['DEF456', 160, '2022-03-16', 12, 'PRT672', 'CAP TRIMMER ', 950,  '4.7NF'],
    ['GHI789', 30, '2022-03-17', 3, 'PRT901', 'CAP TRIMMER', 700, '5.6NF'],
    ['JKL012', 210, '2022-03-18', 4, 'PRT232', 'CAP CER RAD', 1050,  '6.2NF'],
    ['MNO345', 50, '2022-03-19', 5, 'PRT673', 'CAP CER RAD', 900,  '6.8NF'],
    ['PQR678', 190, '2022-03-20', 8, 'PRT902', 'CAP CER RAD', 600, '4.9NF'],
    ['STU901', 70, '2022-03-21', 2, 'PRT233', 'CAP TANT POLY', 1200, '7.3NF'],
    ['VWX234', 140, '2022-03-22', 3, 'PRT566', 'CAP TANT POLY', 450, '4.5NF'],
    ['YZA567', 30, '2022-03-23', 4, 'PRT890', 'CAP TANT POLY', 800,  '8.2NF'],
    ['BCD890', 110, '2022-03-24', 5, 'PRT123', 'CAP NIOB OXID', 650, '9.4NF'],
    ['EFG123', 220, '2022-03-25', 10, 'PRT456', 'CAP NIOB OXID', 1100,  '4.1NF'],
    ['HIJ456', 90, '2022-03-26', 5, 'PRT789', 'OXICAP', 350,  '4.8NF'],
    ['KLM789', 170, '2022-03-27', 3, 'PRT012', 'CAP FILM', 700,  '9.2NF'],
    ['NOP012', 60, '2022-03-28', 4, 'PRT345', 'CAP FILM', 950,  '9.3NF'],
    ['QRS345', 200, '2022-03-29', 5, 'PRT674', 'CAP FILM', 500,  '5.3NF'],
    ['TUV678', 80, '2022-03-30', 10, 'PRT903', 'CAP ALUM POLY', 850,  '2.3NF'],
    ['WXY901', 150, '2022-03-31', 12, 'PRT234', 'CAP ALUM POLY', 400,  '3.3NF'],
    ['ZAB234', 40, '2022-04-01', 3, 'PRT567', 'CAP ALUM POLY', 750,  '10.3NF'],
    ['CDE567', 120, '2022-04-02', 4, 'PRT891', 'CAP ALUM POLY', 100,  '4.6NF'],
    ['FGH890', 230, '2022-04-03', 5, 'PRT124', 'CAP ALUM POLY', 550,  '4.7NF']
]
#Data IC
data_ic = [
    ['mnf_id', 'price', 'inventory_date', 'guarantee', 'part_number', 'sub_category','stock', 'clock'],
    ['ABC123', 90, '2022-03-31', 6, 'PRT1234', 'IC MODULATOR', 409, '1.7GHZ'],
    ['DEF456', 40, '2022-04-01', 3, 'PRT2345', 'IC AUDIO ', 754, '1.8GHZ'],
    ['GHI789', 120, '2022-04-02', 4, 'PRT3456', 'IC SAMPLE RATE', 1003, '1.9GHZ'],
    ['JKL012', 230, '2022-04-03', 5, 'PRT4567', 'IC AUDIO SIGNAL PROCESSOR ', 551, '2.0GHZ'],
    ['MNO345', 140, '2022-03-31', 6, 'PRT5678', 'IC VOLUME CONTROL ', 407, '1.7GHZ'],
    ['PQR678', 270, '2022-05-01', 3, 'PRT6789', 'IC MODULATOR', 458, '2.5GHZ'],
    ['STU901', 130, '2022-04-02', 5, 'PRT7890', 'IC AUDIO RECEIVER', 655, '2.2GHZ'],
    ['VWX234', 190, '2022-03-03', 8, 'PRT8901', 'IC LINE DRIVER', 307, '1.5GHZ'],
    ['YZA567', 80, '2022-03-31', 9, 'PRT9012', 'IC CLK BUFFER', 254, '1.2GHZ'],
    ['BCD890', 160, '2022-04-01', 6, 'PRT0123', 'IC CLK BUFFER', 506, '1.6GHZ'],
    ['EFG123', 110, '2022-04-02', 4, 'PRT2345A', 'IC CLK BUFFER', 804, '2.3GHZ'],
    ['HIJ456', 260, '2022-05-03', 7, 'PRT3456A', 'IC FANOUT BUFFER', 353, '1.8GHZ'],
    ['KLM789', 70, '2022-09-30', 2, 'PRT4567A', 'IC FANOUT BUFFER', 204, '1.1GHZ'],
    ['NOP012', 150, '2022-02-01', 5, 'PRT5678A', 'IC CLK MULTPX', 600, '1.4GHZ'],
    ['QRS345', 220, '2022-04-02', 6, 'PRT6789A', 'IC CLK MULTPX', 901, '2.1GHZ'],
    ['TUV678', 100, '2022-09-03', 3, 'PRT7890A', 'IC CLK MULTIPLXR ', 303, '1.3GHZ'],
    ['WXY901', 180, '2022-03-31', 2, 'PRT8901A', 'IC CLK MULTIPLXR ', 704, '1.5GHZ'],
    ['ZAB234', 40, '2022-02-01', 3, 'PRT9012A', 'IC ADC', 751, '1.8GHZ'],
    ['CDE567', 120, '2022-01-02', 4, 'PRT0123A', 'IC ADC', 100, '1.9GHZ'],
    ['FGH890', 230, '2022-08-03', 5, 'PRT1234B', 'IC ADC', 552, '2.0GHZ']
]
#Data Resistor
data_resistor =[ 
['mnf_id', 'price', 'inventory_date', 'guarantee', 'part_number', 'sub_category','stock', 'resistance'],
    ['ABC123', 59, '2022-03-23', 5, 'PRT1234', 'RES 120K OHM ', 123, '120K'],
    ['DEF456', 43, '2022-04-09', 7, 'PRT2345', 'RES 120K OHM  ', 589, '120K'],
    ['GHI789', 132, '2022-04-12', 8, 'PRT3456', 'RES 88.7K OHM ', 345, '88.7K'],
    ['JKL012', 492, '2022-02-04', 12, 'PRT4567', 'RES 88.7K OHM', 120, '88.7K'],
    ['MNO345', 123, '2022-03-05', 8, 'PRT5678', 'RES 88.7K OHM ', 490, '88.7K'],
    ['PQR678', 580, '2022-04-21', 24, 'PRT6789', 'RES 120K OHM ', 495, '120K'],
    ['STU901', 124, '2022-01-30', 12, 'PRT7890', 'RES 120K OHM ', 235, '120K'],
    ['VWX234', 389, '2022-03-31',4, 'PRT8901', 'RES 1.69K OHM ', 123, '1.69K'],
    ['YZA567', 302, '2022-03-28', 9, 'PRT9012', 'RES 1.69K OHM' , 950, '1.69K'],
    ['BCD890', 305, '2022-01-23', 24, 'PRT0123', 'RES 1.69K OHM ', 390, '1.69K'],
    ['EFG123', 308, '2022-03-27', 12, 'PRT2345A', 'RES 2.8K OHM', 420, '2.8K'],
    ['HIJ456', 250, '2022-04-20', 8, 'PRT3456A', 'RES 2.8K OHM', 345, '2.8K'],
    ['KLM789', 70,  '2022-03-12', 4, 'PRT4567A', 'RES 2.8K OHM', 201, '2.8K'],
    ['NOP012', 160, '2022-02-26', 7, 'PRT5678A', 'RES 9.09K OHM ', 620, '9.09K'],
    ['QRS345', 230, '2022-08-29', 3, 'PRT6789A', 'RES 9.09K OHM ', 910, '9.09K'],
    ['TUV678', 127, '2022-06-22', 5, 'PRT7890A', 'RES 13.8K OHM ', 329, '13.8K'],
    ['WXY901', 198, '2022-07-21', 9, 'PRT8901A', 'RES 13.8K OHM ', 710, '13.8K'],
    ['ZAB234', 494, '2022-09-20', 12, 'PRT9012A', 'RES 43.2K OHM', 755, '43.2K'],
    ['CDE567', 129, '2022-04-17', 4, 'PRT0123A', 'RES 43.2K OHM', 102, '43.2K'],
    ['FGH890', 232, '2022-12-13', 5, 'PRT1234B', 'RES 43.2K OHM', 559, '43.2K']
]
#Data Inductor
data_inductor =[
['mnf_id', 'price', 'inventory_date', 'guarantee', 'part_number', 'sub_category','stock', 'inductance'],
    ['ABC123', 234, '2022-03-12', 2, 'PRT3045','FIXED IND 10UH  ', 123, '10UH'],
    ['DEF456', 230, '2022-04-02', 5, 'PRT2034', 'FIXED IND 10UH  ', 589, '10UH'],
    ['GHI789', 123, '2022-04-13', 7, 'PRT3040', 'FIXED IND 10UH  ', 345, '10UH'],
    ['JKL012', 544, '2022-02-01', 12, 'PRT2033', 'FIXED IND 2.2UH ', 120, '2.2UH'],
    ['MNO345', 232, '2022-03-09', 2, 'PRT2035', 'FIXED IND 2.2UH  ', 490, '2.2UH'],
    ['PQR678', 540, '2022-04-23', 9, 'PRT3201', 'FIXED IND 2.2UH  ', 495, '2.2UH'],
    ['STU901', 124, '2022-04-12', 2, 'PRT7460', 'FIXED IND 18NH  ', 235, '18NH'],
    ['VWX234', 388, '2022-04-13',1, 'PRT3245', 'FIXED IND 18NH  ', 123, '18NH'],
    ['YZA567', 332, '2022-03-21', 2, 'PRT1203', 'FIXED IND 18NH ' , 950, '18NH'],
    ['BCD890', 342, '2022-04-23', 3, 'PRT0545', 'FIXED IND 10UH ', 390, '10UH'],
    ['EFG123', 325, '2022-02-27', 9, 'PRT1205', 'FIXED IND 10UH', 420, '10UH'],
    ['HIJ456', 219, '2022-04-04', 1, 'PRT1200', 'FIXED IND 10UH', 345, '10UH'],
    ['KLM789', 254, '2022-02-12', 2, 'PRT8054', 'FIXED IND 1UH', 201, '1UH'],
    ['NOP012', 281, '2022-01-29', 7, 'PRT1204', 'FIXED IND 1UH ', 620, '1UH'],
    ['QRS345', 295, '2022-04-29', 6, 'PRT2013', 'FIXED IND 1UH ', 910, '1UH'],
    ['TUV678', 119, '2022-02-22', 3, 'PRT2013A', 'FIXED IND 4.7UH ', 329, '4.7UH'],
    ['WXY901', 123, '2022-03-21', 7, 'PRT5453', 'FIXED IND 4.7UH', 710, '4.7UH'],
    ['ZAB234', 421, '2022-03-20', 10, 'PRT2504', 'FIXED IND 4.7UH', 755, '4.7UH'],
    ['CDE567', 141, '2022-09-17', 5, 'PRT1004', 'FIXED IND 100NH', 102, '100NH'],
    ['FGH890', 235, '2022-08-13', 2, 'PRT0710', 'FIXED IND 100NH', 559, '100NH']
]
#Data Sensor
data_sensor =[
['mnf_id', 'price', 'inventory_date', 'guarantee', 'part_number','status', 'sub_category','stock', 'sensor_type'],
    ['ABC123', 123, '2022-02-13', 1, 'PRT2304','IGITAL FLOW SENSOR ', 124, 'Temperature'],
    ['DEF456', 850, '2022-06-05', 5, 'PRT2903', 'DIGITAL FLOW SENSOR  ', 232, 'Temperature'],
    ['GHI789', 392, '2022-02-10', 5, 'PRT2909', 'DIGITAL FLOW SENSOR ', 215, 'Temperature'],
    ['JKL012', 204, '2022-05-20', 9, 'PRT0712', 'FLOW SENSOR MEMS ', 543, 'Liquid conduction'],
    ['MNO345', 123, '2022-01-22', 2, 'PRT5940', 'FLOW SENSOR MEMS', 499, 'Liquid conduction'],
    ['PQR678', 493, '2022-09-27', 12, 'PRT3021', 'FLOW SENSOR MEMS ', 491, 'Liquid conduction'],
    ['STU901', 144, '2022-03-04', 7, 'PRT4304','SENSOR GAS FLOW ', 221, 'Gas'],
    ['VWX234', 312, '2022-05-05',2,  'PRT2301' ,'SENSOR GAS FLOW  ', 185, 'Gas'],
    ['YZA567', 395, '2022-06-12', 3, 'PRT3040','SENSOR GAS FLOW' , 912, 'Gas'],
    ['BCD890', 321, '2022-08-13', 12, 'PRT5345','AIRFLOW SENSOR ', 360, 'Temperature'],
    ['EFG123', 323, '2022-01-09', 5, 'PRT2302','AIRFLOW SENSOR', 412, 'Temperature'],
    ['HIJ456', 212, '2022-03-03', 2, 'PRT8542','AIRFLOW SENSOR', 345, 'Temperature'],
    ['KLM789', 224, '2022-08-10', 24, 'PRT1294', 'SENSOR GAS FLOW TYPE 0-1L/MIN ', 249, 'Gas'],
    ['NOP012', 291, '2022-02-22', 12, 'PRT1231','FSENSOR GAS FLOW TYPE 0-1L/MIN  ', 605, 'Gas'],
    ['QRS345', 215, '2022-08-27', 7, 'PRT2042', 'SENSOR GAS FLOW TYPE 0-1L/MIN  ', 802, 'Gas'],
    ['TUV678', 129, '2022-11-20', 2, 'PRT2121', 'SENSOR MICRO-FLOW ', 323, 'Liquid conduction'],
    ['WXY901', 106, '2022-07-30', 5, 'PRT5454', 'SENSOR MICRO-FLOW', 769, 'Liquid conduction'],
    ['ZAB234', 481, '2022-12-12', 8, 'PRT9922', 'SENSOR MICRO-FLOW', 723, 'Liquid conduction'],
    ['CDE567', 111, '2022-10-18', 9, 'PRT4400', 'FLOW SENSOR MEMS 20L/MIN', 129, 'Liquid conduction'],
    ['FGH890', 212, '2022-09-14', 12, 'PRT1111', 'FLOW SENSOR MEMS 20L/MIN', 510, 'Liquid conduction']
]





