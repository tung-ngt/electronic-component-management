import pymysql
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
from json import dumps

cred = credentials.Certificate("D:/Python Project/Firebase/electronic-componentmanagement-firebase-adminsdk-f90vx-981a48ea9d.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://electronic-componentmanagement-default-rtdb.firebaseio.com/'
})
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='songunner1999',
    db='electronic',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `manufacturer`"
        cursor.execute(sql)
        result = cursor.fetchall()
        ref = db.reference('manufacturer')
        for row in result:
            data = {
                'id' : row['id'],
                'name': row['name'],
                'country': row['country'],
            }
        # check if username exists or not in firebase, if not then add to firebase else update
            if ref.child(row['name']).get() is None:
                ref.child(row['name']).set(data)
            else:
                ref.child(row['name']).update(data)

        sql = "SELECT * FROM `capacitor`"
        cursor.execute(sql)
        result = cursor.fetchall()
        ref = db.reference('capacitor')
        for row in result:
            data = {
                'part_number': row['part_number'],
                'mnf_id': row['mnf_id'],
                'price': row['price'],
                'inventory_date': row['inventory_date'],
                'status' : row['status'],
                'guarantee' : row['guarantee'],
                'capacitance' : row['capacitance'],
                'sub_category' : row['sub_category'],
                'stock' : row['stock'],
            }
        # check if username exists or not in firebase, if not then add to firebase else update
            if ref.child(row['part_number']).get() is None:
                ref.child(row['part_number']).set(data)
            else:
                ref.child(row['part_number']).update(data)
        sql = "SELECT * FROM `ic`"
        cursor.execute(sql)
        result = cursor.fetchall()
        ref = db.reference('ic')
        for row in result:
            data = {
                'part_number': row['part_number'],
                'mnf_id': row['mnf_id'],
                'price': row['price'],
                'inventory_date': row['inventory_date'],
                'status' : row['status'],
                'guarantee' : row['guarantee'],
                'clock' : row['clock'],
                'sub_category' : row['sub_category'],
                'stock' : row['stock'],
            }
        # check if username exists or not in firebase, if not then add to firebase else update
            if ref.child(row['part_number']).get() is None:
                ref.child(row['part_number']).set(data)
            else:
                ref.child(row['part_number']).update(data)
        sql = "SELECT * FROM `inductor`"
        cursor.execute(sql)
        result = cursor.fetchall()
        ref = db.reference('inductor')
        for row in result:
            data = {
                'part_number': row['part_number'],  
                'mnf_id': row['mnf_id'],
                'price': row['price'],
                'inventory_date': row['inventory_date'],
                'status' : row['status'],
                'guarantee' : row['guarantee'],
                'inductance' : row['inductance'],
                'sub_category' : row['sub_category'],
                'stock' : row['stock'],
            }
        # check if username exists or not in firebase, if not then add to firebase else update
            if ref.child(row['part_number']).get() is None:
                ref.child(row['part_number']).set(data)
            else:
                ref.child(row['part_number']).update(data)
        sql = "SELECT * FROM `resistor`"
        cursor.execute(sql)
        result = cursor.fetchall()
        ref = db.reference('resistor')
        for row in result:
            data = {
                'part_number': row['part_number'],  
                'mnf_id': row['mnf_id'],
                'price': row['price'],
                'inventory_date': row['inventory_date'],
                'status' : row['status'],
                'guarantee' : row['guarantee'],
                'resistance' : row['resistance'],
                'sub_category' : row['sub_category'],
                'stock' : row['stock'],
            }
        # check if username exists or not in firebase, if not then add to firebase else update
            if ref.child(row['part_number']).get() is None:
                ref.child(row['part_number']).set(data)
            else:
                ref.child(row['part_number']).update(data)
        sql = "SELECT * FROM `sensor`"
        cursor.execute(sql)
        result = cursor.fetchall()
        ref = db.reference('sensor')
        for row in result:
            data = {
                'part_number': row['part_number'],  
                'mnf_id': row['mnf_id'],
                'price': row['price'],
                'inventory_date': row['inventory_date'],
                'status' : row['status'],
                'guarantee' : row['guarantee'],
                'sensor_type' : row['sensor_type'],
                'sub_category' : row['sub_category'],
                'stock' : row['stock'],
            }
        # check if username exists or not in firebase, if not then add to firebase else update
            if ref.child(row['part_number']).get() is None:
                ref.child(row['part_number']).set(data)
            else:
                ref.child(row['part_number']).update(data)
finally:
    connection.close()
