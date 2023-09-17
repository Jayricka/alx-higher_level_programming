#!/usr/bin/python3
"""This script lists states starting with 'N' from the hbtn_0e_0_usa database."""

import mysql.connector
import sys

def filter_states_by_name(username, password, db_name):
    """Connects to MySQL and retrieves states starting with 'N'."""
    # Connect to the MySQL server
    db = mysql.connector.connect(host="localhost", user=username, password=password, database=db_name)
    cursor = db.cursor()

    # Execute the SQL query to select states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all the rows
    filtered_states = cursor.fetchall()

    # Display the results
    for state in filtered_states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    filter_states_by_name(username, password, db_name)
