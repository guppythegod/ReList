"""
This file should only be used when there is no table in the accounts.sqlite file, and that one should be there
if there is than running this file will result in an error
"""

import sqlite3
import os

sqlite_file = "accounts.sqlite"
cwd = os.path.dirname(os.path.realpath(__file__))
print(cwd)
conn = sqlite3.connect(cwd + "/" + sqlite_file)
c = conn.cursor()

# Creates table, 'url_data' with neccessary columns and keys
c.execute("""CREATE TABLE url_data(id TEXT NOT NULL, name TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL,PRIMARY KEY (id));""")

conn.commit() # commit the changes to the db
conn.close() # close the database
