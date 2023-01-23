#Name: Eshan Adatia
#Date: January 20 2023
#Program name: BlackJack with database and GUI
#Purpose: Creating a fun inovative game that incorporates a database component as well as GUI.

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

# Creating main window function
def mainLogin():
  # Creates the main window
  mainDatabase = tk.Tk()
  mainDatabase.title("BlackJack Login")
  mainDatabase.geometry("1280x720")

  # Load the image file
  image = tk.PhotoImage(file="login.png")

  # Create a label with the image as the background
  label = tk.Label(mainDatabase, image=image)
  label.pack()

  # Add a label on top of the image
  windowName = tk.Label(mainDatabase, text="BlackJack Login",bg = '#800080', font=('times new roman', 40, 'bold'))
  windowName.place(x=650, y=50)

  # Create a frame with specific background color
  dataFrame = Frame(mainDatabase, bg='#800080')
  dataFrame.place(x=725,y=360, width=335, height=100)

  #Label and box for first name
  usernameLabel = Label(dataFrame, bg="#FFFACD", text="Username")
  usernameLabel.grid(row=0, column=0, padx=15, pady=10)
  usernameEntry = Entry(dataFrame)
  usernameEntry.grid(row=0, column=1, padx=10, pady=10)

  #Label and box for last name
  passwordLabel = Label(dataFrame, bg="#FFFACD", text="Password")
  passwordLabel.grid(row=1, column=0, padx=15, pady=10)
  passwordEntry = Entry(dataFrame)
  passwordEntry.grid(row=1, column=1, padx=10, pady=10)

  # Connecting to the database
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
  #Logs a user in if their account is present in the database or if no boxes left empty. Otherwise error message is created 
  #function to log user in
  #Ins:(Username, Password entry)
  #Outs: (Msg)
  def loginAccount():
    # Get the data from the form
    username = usernameEntry.get()
    password = passwordEntry.get()
  
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
        mainDatabase.destroy()
        # Get the user's funds from the database
        funds = database.getFunds(username, password)
        bj.mainGame(funds, username, password)
      else:
        # Data is not present in the table
        messagebox.showerror("Error", "Username or Password incorrect. Please try again or create a new account")
        # Clear the entry boxes
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
  #Adds a user to the database if no boxes left entry, password contains at least 4 characters and data is not already present in the table. Otherwise error message is created 
  #function to create user in
  #Ins:(Username, Password entry)
  #Outs: (Msg)
  def createAccount():
    # Get the data from the form
    username = usernameEntry.get()
    password = passwordEntry.get()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    if len(password) < 4 or len(password) > 20:
      messagebox.showerror("Error", "Password must be between 4 and 20 characters long")
      return
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
          messagebox.showerror("Error","Data is already present in the table, You will be logged in and redirected now")
          mainDatabase.destroy()
          funds = database.getFunds(username, password)
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
          usernameEntry.delete(0, END)
          passwordEntry.delete(0, END)
  #Removes an account from the database if creditionals in database and no boxes left empty. Otherwise error message is created 
  #function to remove user
  #Ins:(Username, Password entry)
  #Outs: (Msg)
  def removeAccount():
    # Get the username and password from the entry widgets
    username = usernameEntry.get()
    password = passwordEntry.get()
    
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
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
      
    else:
        # Data is not present in the table
        messagebox.showerror("Error", "Username or Password not correct. Account  not deleted please try again")
  
      # Clear the entry boxes
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)
      
  # Close the connection
  conn.close()
  
  #Function preformed once users click exit database
  def close():
    mainDatabase.destroy()
    m.mainMenu()
    
  #Creates the white frame shown on the screen that houses the "add", "remove", "update", and "quit" buttons
  mainFrame = Frame(mainDatabase, bg='#800080')
  mainFrame.place(x=725,y=225, width=335, height=135)
  
  #Creates the individual buttons needed for the program and connects them to a function that carries out the task
  createAccount = Button(mainFrame, bg='#FFFACD', text="Create Account", command = createAccount, font=('times new roman', 7), height=2, width=12, bd=6).place(x=45,y=15)
  
  loginAccount = Button(mainFrame, bg='#FFFACD', text="Login",font=('times new roman', 7), command=loginAccount, height=2, width=12, bd=6).place(x=170,y=15)
  
  removeAccount = Button(mainFrame, bg='#FFFACD', text="Remove Account",font=('times new roman', 7), command=removeAccount, height=2, width=12, bd=6).place(x=45,y=75)
  
  close = Button(mainFrame, bg='#FFFACD', text="Back to Menu",font=('times new roman', 7), command=close, height=2, width=12, bd=6).place(x=170,y=75)
  # Run the Tkinter event loop
  mainDatabase.mainloop()
