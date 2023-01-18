import sqlite3

def get_funds(username, password):
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()
  # Check if the data is present in the table
  cursor.execute('''
    SELECT username, password, funds FROM users
    WHERE username = ? AND password = ?
  ''', (username, password))

  # Fetch the results of the query
  results = cursor.fetchone()

  if results:
    # Data is present in the table
    return results[2]
  else:
    # Data is not present in the table
    return None

def update_funds(funds, username, password):
                # Update the database with the new funds value
                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users
                    SET funds = ?
                    WHERE username = ? AND password = ?
                    ''', (funds, username, password))
                conn.commit()
