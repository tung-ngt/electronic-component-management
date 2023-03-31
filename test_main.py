from controllers.component_controller import convert_condition

print(convert_condition({"mnf_id": "abc",
                         "part_number": "123xyz",
                         "inventory_date": [("<=", '2022-09-01'), (">=", "2022-01-02")],
                         "price": [("<=", 50), (">=", 40)],
                         "guarantee": [("<=", ""), (">=", 20)],
                         "sub_category": ["item 1", "item 2", "item 3"],
                         "stock": [("<=", ""), (">=", "")],
                         "capacitance": [("<=", 30), (">=", 60)],
                         "sensor_type": ["type 1", "type 2", "type 3"]}))