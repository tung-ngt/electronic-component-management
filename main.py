import models.db.database_with_classes as mktable
import models.db.Utils_database as utl
from views.App import EComponentStoreManagementGUI

if __name__ == "__main__":
    # Create db file in "models/db/electronic store.db"
    conn, cur = utl.get_connection('electronic_store_with_classes')
    mktable.delete_all_tables(conn)
    mktable.create_tables()
    app = EComponentStoreManagementGUI()
    app.mainloop()  