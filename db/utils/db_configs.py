COMPONENT_COLUMNS = [
    "part_number",
    "mnf_id",
    "price",
    "inventory_date",
    "guarantee",
    "sub_category",
    "stock",
    "image_path",
    "special_attr",
]

COMPONENT_SPECIAL_ATTR = {
    "sensor": "sensor_type",
    "ic": "clock",
    "capacitor": "capacitance",
    "inductor": "inductance",
    "resistor": "resistance"
}

MANUFACTURER_COLUMNS = [
    "id",
    "name",
    "country",
    "image_path"
]

CUSTOMER_COLUMNS = [
    "id",
    "name",
    "phone_number"
]

ORDER_COLUMNS = [
    "order_id",
    "customer_id",
    "items",
    "date",
]

DB_PATH = "./data/database.db"