import sqlite3

CONN = sqlite3.connect('functions.db')
CURSOR = CONN.cursor()