from models.db.Utils_database import get_connection
class UserSignIn:
    def __init__(self):
        self.conn, self.cursor = get_connection ('electronic_store_with_classes')
    
    def authenticate(self, username, password):
        cur = self.conn.cursor()

        # Execute the SQL query check username and password
        cur.execute("SELECT * FROM user_data WHERE username = %s AND password = %s", (username, password))

        # Get the result
        result = cur.fetchone()

        # Close the cursor and connection
        cur.close()
        self.conn.close()

        if (len(result) != 0):
            return True
        else:
            return False
