import UserSignIn
from tkinter import messagebox
from models.db.Utils_database import get_connection
def signup(self):
        username = self.entry_username.get()
        user_password = self.entry_password.get()
        if username == "" or user_password == "":
            messagebox.showerror("Error", "something is missing")
        else:
            try:
                con, mycursor = get_connection('electronic_store_with_classes')
                mycursor = con.cursor()
            except:
                messagebox.showerror("Error", "Error in connection")
                return
            try:
                query = 'create table user_data(username varchar(255), password varchar(255))'
            except:
                pass
            mycursor.execute(query)
        # check if the user is already in the database
        query = 'select * from user_data where username = %s'
        mycursor.execute(query, username)
        result = mycursor.fetchall()
        if len(result) != 0:
            messagebox.showerror("Error", "Username already exists")
            return
        query = 'insert into user_data(username, password) values(%s, %s)'
        mycursor.execute(query, (username, user_password))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Sign up successfully")
def signin(self):        
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "" or password == "":
            messagebox.showerror("Error", "Username or password is empty")
        try:
            db = UserSignIn.UserSignIn()
            if db.authenticate(username, password):
                messagebox.showinfo("Success", "Login successfully")
            else:
                messagebox.showerror("Error", "Username or password is incorrect")
        except:
            return

