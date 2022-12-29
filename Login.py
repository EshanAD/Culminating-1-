import sqlite3
from tkinter import END

# Define the Login_Account function
def Login_Account():
    # Get the data from the form
    username = username_entry.get()
    password = password_entry.get()
  
    if not username or not password:
      # One or both of the entry widgets are empty
      messagebox.showerror("Error", "Username and password cannot be empty")
    else:
      conn = sqlite3.connect("database.db")
      cursor = conn.cursor()
      # Check if the data is present in the table
      cursor.execute('''
        SELECT * FROM users
        WHERE username = ? AND password = ?
      ''', (username, password))
  
      # Fetch the results of the query
      results = cursor.fetchone()
  
      if results:
        # Data is present in the table
        messagebox.showinfo("","Cridentials in Database you are now logged in")
        #Destroy This Database before running game
        #BlackJack Game Function goes here
      else:
        # Data is not present in the table
        messagebox.showinfo("","Username or Password incorrect. Please try again or create a new account")
        # Clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)
  
  # Define the Create_Account function
def Create_Account():
      # Get the data from the form
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    if not username or not password:
      # One or both of the entry widgets are empty
      messagebox.showerror("Error", "Username and password cannot be empty")
    else:
      # Check if the data is already present in the table
      cursor.execute('''
          SELECT * FROM users
          WHERE username = ? AND password = ?
      ''', (username, password))
  
      # Fetch the results of the query
      results = cursor.fetchone()
  
      if results:
        # Data is already present in the table
        messagebox.showerror("","Data is already present in the table, You will be logged in and redirected now")
        #Destroy This Database before running game
        #BlackJack Game Function goes here
      else:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        # Insert the data into the table
        cursor.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
          ''', (username, password))
  
          # Commit the transaction
        conn.commit()
  
        # Tells the user if they logged
        messagebox.showinfo("", "Added succesfully!. Now log in through the log in button")
  
        #Clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)