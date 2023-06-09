from controllers.AppController import AppController
from time import sleep
app_controller = AppController()
# filters = {
#     "mnf_id": "",
#     "part_number": "MAX232CPE",
#     "inventory_date" : [("<=",""), (">=", "")],
#     "price" : [("<=",""), (">=", "")],
#     "guarantee" : [("<=",""), (">=", "")],
#     "sub_category" : [],
#     "stock": [("<=",""), (">=", "")],
#     "clock" : [("<=",""), (">=", "")],
# }

# result = app_controller.get_list("ic")
# print(len(result))

# data = {
#     "mnf_id": "M006",
#     "part_number": "MAX232CPEa",
#     "inventory_date" : "2022-03-05",
#     "price" : "2.15",
#     "guarantee" : "1",
#     "sub_category" : "RS232 Transceiver",
#     "stock": "20",
#     "clock" : "5",
# }
# app_controller.add("ic", data)

# result = app_controller.get_list("ic")
# print(len(result))
# print(result[-1].get_all_info())

results = app_controller.get_filtered_list("ic", sort_options={"mnf_id": "desc", "price": "asc"})

for r in results:
    print(f"{r.get_mnf_id()} {r.get_price()}")


# no_result, result = app_controller.get_list_with_filters("ic", filters)
# print(no_result)
# for component in result:
#     print(component.get_all_info())

# app_controller.compress_all_images()
# sleep(5)
# app_controller.decompress_all_images()

# no_result, result = app_controller.get_list_of_orders({"items": "8"}, sort_options=[("items", "asc")])

# for r in result:
#     print(r.get_all_info())

# result = app_controller.get_all_components_prices()
# print(result)
# print('Bosch BMI088' in result.keys())