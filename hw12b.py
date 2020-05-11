# Homework 12 (b) - 17.1
# ---
# Example exercises with SQL
# ---
# Matt Pembroke, 2020

import sqlite3
import pandas as pd

# create a connection to the sql database file
connection = sqlite3.connect('books.db')

# set some options for pandas
pd.options.display.max_columns = 10

# (a)
print('-----')
print('> a <')
print('-----')
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))

# (b)
print('-----')
print('> b <')
print('-----')
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))

# (c)
print('-----')
print('> c <')
print('-----')
print('*** Books written by Paul Deitel ***')
print(pd.read_sql('SELECT title, copyright, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn WHERE author_ISBN.id=1 ORDER BY title ASC', connection))

# (d)
print('-----')
print('> d <')
print('-----')
cursor = connection.cursor()
cursor.execute('INSERT INTO authors (first, last) VALUES (\'Matt\', \'Pembroke\')')
authors = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
print(authors)

# (e)
print('-----')
print('> e <')
print('-----')
cursor.execute('INSERT INTO author_ISBN (id, isbn) VALUES (6, \'0000000000\')')
cursor.execute('INSERT INTO titles (isbn, title, edition, copyright) VALUES (\'0000000000\',\'Example Book\',1,\'2020\')')
print(pd.read_sql('SELECT * FROM author_ISBN', connection))
print(pd.read_sql('SELECT * FROM titles', connection))

# close the connection to the database
connection.close()