from views.App import EComponentStoreManagementGUI
from controllers.AppController import AppController
from controllers.utils import file_utils

if __name__ == "__main__":
    app_controller = AppController()
    app_controller.unzip_images()
    app_controller.load_data_from_db()
    app = EComponentStoreManagementGUI(app_controller)
    app.mainloop()  
    app_controller.zip_images()