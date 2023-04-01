from controllers.AppController import AppController


app_controller = AppController()
app_controller.load_data_from_db()
filters = {
    "mnf_id": "",
    "part_number": "MAX",
    "inventory_date" : [("<=",""), (">=", "")],
    "price" : [("<=",""), (">=", "")],
    "guarantee" : [("<=",""), (">=", "")],
    "sub_category" : [],
    "stock": [("<=",""), (">=", "")],
    "clock" : [("<=",""), (">=", "")],
}

no_result, result = app_controller.get_list_with_filters("ic", filters)
print(no_result)
for component in result:
    print(component.get_all_info())