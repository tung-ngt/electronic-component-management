from controllers.AppController import AppController


app_controller = AppController("electronic_store_with_classes.db")
app_controller.load_data_from_db()
print(app_controller.get_capacitors())