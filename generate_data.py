import models.db.create_database as mktable
import models.db.utils.connect_to_db as utl
from views.App import EComponentStoreManagementGUI
from controllers.AppController import AppController

if __name__ == "__main__":
    app_controller = AppController()
    app_controller.load_data_from_db()
    app = EComponentStoreManagementGUI(app_controller)
    app.mainloop()  