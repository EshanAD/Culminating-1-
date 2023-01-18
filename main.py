import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from sqlite3 import *
from tkinter import END
import BlackJack as bj
import Menu as m
import database 

# Creating main window
def main_login():
  #Creates the wh# Create the main window
  main_database = tk.Tk()
  main_database.title("BlackJack Login")
  main_database.geometry("1280x720")
  
  # Load the image file
  image = tk.PhotoImage(file="login.png")
  
  # Create a label with the image as the background
  label = tk.Label(main_database, image=image)
  label.pack()
  
  # Add a label on top of the image
  window_name = tk.Label(main_database, text="BlackJack Login",bg = '#800080', font=('times new roman', 40, 'bold'))
  window_name.place(x=650, y=50)

  data_frame = Frame(main_database, bg='#800080')
  data_frame.place(x=725,y=360, width=335, height=100)
  
  #Label and box for first name
  username_label = Label(data_frame, bg="#FFFACD", text="Username")
  username_label.grid(row=0, column=0, padx=15, pady=10)
  username_entry = Entry(data_frame)
  username_entry.grid(row=0, column=1, padx=10, pady=10)
  
  #Label and box for last name
  password_label = Label(data_frame, bg="#FFFACD", text="Password")
  password_label.grid(row=1, column=0, padx=15, pady=10)
  password_entry = Entry(data_frame)
  password_entry.grid(row=1, column=1, padx=10, pady=10)
  
  
  
  conn = sqlite3.connect('database.db')
  # Create a cursor object to execute SQL commands
  cursor = conn.cursor()
 
  # Create the "users" table if it does not already exist
  cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    funds REAL DEFAULT 100.0
);
''')
  # Define the Login_Account function
  # login.py

  global username 
  global password

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
        main_database.destroy()
        # Get the user's funds from the database
        funds = database.get_funds(username, password)
        bj.mainGame(funds, username, password)
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
        main_database.destroy()
        funds = database.get_funds(username, password)
        bj.mainGame(funds, username, password)
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
  
        # Show a success message
        messagebox.showinfo("", "Added succesfully!. Now log in through the log in button")
  
        #Clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)
  
  def Remove_Account():
    # Get the username and password from the entry widgets
    username = username_entry.get()
    password = password_entry.get()
    
    # Connect to the database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    if not username or not password:
      # One or both of the entry widgets are empty
      messagebox.showerror("Error", "Username and password cannot be empty")
    else:
    # Check if the data is present in the table
      cursor.execute('''
      SELECT * FROM users
      WHERE username = ? AND password = ?
  ''', (username, password))
  
      # Fetch the results of the query
      results = cursor.fetchone()
  
    if results:
      # Data is present in the table, so delete it
        cursor.execute('''
        DELETE FROM users
        WHERE username = ? AND password = ?
      ''', (username, password))
  
        # Commit the transaction
        conn.commit()
  
        # Show a success message
        messagebox.showinfo("", "Account deleted")
  
        # Clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)
      
    else:
        # Data is not present in the table
        messagebox.showinfo("", "Username or Password not correct. Account  not deleted please try again")
  
      # Clear the entry boxes
        username_entry.delete(0, END)
        password_entry.delete(0, END)
      
  # Close the connection
  conn.close()
  
  #Function preformed once users click exit database
  def Close():
    main_database.destroy()
    m.main_menu()
    
  #Creates the white frame shown on the screen that houses the "add", "remove", "update", and "quit" buttons
  main_frame = Frame(main_database, bg='#800080')
  main_frame.place(x=725,y=225, width=335, height=135)
  
  #Creates the individual buttons needed for the program and connects them to a function that carries out the task
  create_account = Button(main_frame, bg='#FFFACD', text="Create Account", command = Create_Account, font=('times new roman', 7), height=2, width=12, bd=6).place(x=45,y=15)
  
  login_account = Button(main_frame, bg='#FFFACD', text="Login",font=('times new roman', 7), command=Login_Account, height=2, width=12, bd=6).place(x=170,y=15)
  
  remove_account1 = Button(main_frame, bg='#FFFACD', text="Remove Account",font=('times new roman', 7), command=Remove_Account, height=2, width=12, bd=6).place(x=45,y=75)
  
  quit = Button(main_frame, bg='#FFFACD', text="Back to Menu",font=('times new roman', 7), command=Close, height=2, width=12, bd=6).place(x=170,y=75)
  # Run the Tkinter event loop
  main_database.mainloop()
