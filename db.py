import sqlite3
# table name = pwmanager



# Can have a look at what is in the table.
def look_at_table():
    # Connecting to the DB.
    conn = sqlite3.connect('passwords.db')
    # Create cursor
    c = conn.cursor()

    try:
        # Getting the first 50 lines with the limit use.
        c.execute("SELECT * from pwmanager LIMIT 50")

        items = c.fetchall()

        for item in items:
            print(item)
    except:
        print("Opps is there are data in the table because that is probaly the problem. Put some data in it.")

    # Commiting the changes
    conn.commit()
    # Closing the connection
    conn.close()

# Making a function to search for a app name to see if any exist and
# if there is one return it
def app_name_lookup(app_name):
    # Connecting to the DB.
    conn = sqlite3.connect('passwords.db')
    # Create cursor
    c = conn.cursor()

    try:
        # Looking for app using where clause.
        c.execute("SELECT * from pwmanager WHERE app_name = (?)", (app_name,))

        items = c.fetchall()

        for item in items:
            print(item)
    except:
        print("Opps it looks like there isnt a app with that name or maybe you havent entered any information at all yet.")
        print("You should look at how you spelt it or try to enter some data.")
        print("You could also view the first 50 rows of your data by pressing l.")

    # Commiting the changes
    conn.commit()
    # Closing the connection
    conn.close()

def create_record(app_name, pw, name):
    # Connecting to the DB.
    conn = sqlite3.connect('passwords.db')
    # Create cursor
    c = conn.cursor()

    try:
        # Inserting a new recotd/ Adding a new row in table.
        c.execute("INSERT INTO pwmanager VALUES (?,?,?)", (app_name,pw,name))
        print("Password saved")
    except Exception as e:
        print(str(e))
        print("Error, Maybe try again because something has gone wrong.")

    # Commiting the changes
    conn.commit()
    # Closing the connection
    conn.close()

def delete_one(id):
    # Connecting to the DB.
    conn = sqlite3.connect('passwords.db')
    # Create cursor
    c = conn.cursor()

    try:
        # Deleting a record from table / Deleting a row of data
        c.execute("DELETE FROM pwmanager WHERE rowid = (?)", (id))
        print("Row deleted")
    except:
        print("Error, Maybe try again because something has gone wrong.")

    # Commiting the changes
    conn.commit()
    # Closing the connection
    conn.close()