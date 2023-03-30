import models.db.create_database as mktable 
from views.App import EComponentStoreManagementGUI

if __name__ == "__main__":
    # Create db file in "models/db/electronic store.db"
    conn, cur = mktable.get_connection()
    mktable.delete_all_tables(conn)
    mktable.create_tables()
    app = EComponentStoreManagementGUI()
    app.mainloop()  