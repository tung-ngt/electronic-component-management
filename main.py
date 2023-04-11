from views.App import EComponentStoreManagementGUI
from controllers.AppController import AppController

if __name__ == "__main__":
    app_controller = AppController()
    app = EComponentStoreManagementGUI(app_controller)
    app.mainloop()  