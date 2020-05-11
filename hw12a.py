# Homework 12 (a) - 17.2
# ---
# Example of how to navigate a SQL books database
# ---
# Matt Pembroke, 2020

import sqlite3
import pandas as pd

# create a connection to the sql database file
connection = sqlite3.connect('books.db')

# set some options for pandas
pd.options.display.max_columns = 10

# make a selection from the 'authors', 'titles', and 'author_ISBN' tables and display
authors = pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])
titles = pd.read_sql('SELECT * FROM titles', connection)
isbns = pd.read_sql('SELECT * FROM author_ISBN', connection)
print('----------------')
print('> SOME AUTHORS <')
print('----------------')
print(authors)
print('---------------')
print('> SOME TITLES <')
print('---------------')
print(titles)
print('---------------')
print('> SOME ISBN\'S <')
print('---------------')
print(isbns.head())

# an example of a select query that only chooses certain columns
authors = pd.read_sql('SELECT first, last FROM authors', connection)
print('---------------------')
print('> AUTHORS NAME ONLY <')
print('---------------------')
print(authors)

# select some titles that were written after the year 2016
titles = pd.read_sql('SELECT title, edition, copyright FROM titles WHERE copyright > \'2016\'', connection)
print('------------------------------------')
print('> SOME TITLES PUBLISHED AFTER 2016 <')
print('------------------------------------')
print(titles)

# select authors with last name beginning with 'D'
authors = pd.read_sql('SELECT id, first, last FROM authors WHERE last LIKE \'D%\'', connection)
print('-----------------------------------')
print('> AUTHORS LAST NAME STARTS WITH D <')
print('-----------------------------------')
print(authors)

# select authors with first name beginning with '_b'
authors = pd.read_sql('SELECT id, first, last FROM authors WHERE first LIKE \'_b%\'', connection)
print('-------------------------------------')
print('> AUTHORS FIRST NAME STARTS WITH _b <')
print('-------------------------------------')
print(authors)

# select books ordered by title in ascending order
titles = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print('----------------------------------')
print('> SOME TITLES IN ASCENDING ORDER <')
print('----------------------------------')
print(titles)

# sort authors by last name then first name
authors = pd.read_sql('SELECT id, first, last FROM authors ORDER BY last, first', connection)
print('-------------------------------------------')
print('> AUTHORS SORTED BY LAST, THEN FIRST NAME <')
print('-------------------------------------------')
print(authors)

# sort authors by last name descending then first name ascending
authors = pd.read_sql('SELECT id, first, last FROM authors ORDER BY last DESC, first ASC', connection)
print('----------------------------------------------')
print('> AUTHORS SORTED BY LAST DESC, THEN FIRST ASC<')
print('----------------------------------------------')
print(authors)

# select books where title contains 'How to Program'
titles = pd.read_sql('SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE \'%How to Program\' ORDER BY title', connection)
print('----------------------------')
print('> TITLES ABOUT PROGRAMMING <')
print('----------------------------')
print(titles)

# inner join example
info = pd.read_sql('SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first', connection)
print('--------------')
print('> INNER JOIN <')
print('--------------')
print(info.head())

# insert statement
cursor = connection.cursor()
cursor = cursor.execute('INSERT INTO authors (first, last) VALUES (\'Sue\', \'Red\')')
authors = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
print('------------------')
print('> AUTHORS INSERT <')
print('------------------')
print(authors)

# update statement
cursor = cursor.execute('UPDATE authors SET last=\'Black\' WHERE last=\'Red\' AND first=\'Sue\'')
authors = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
print('------------------')
print('> AUTHORS UPDATE <')
print('------------------')
print('*** '+str(cursor.rowcount)+' row updated ***')
print(authors)

# delete statement
cursor = cursor.execute('DELETE FROM authors WHERE id=6')
authors = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
print('------------------')
print('> AUTHORS DELETE <')
print('------------------')
print('*** '+str(cursor.rowcount)+' row deleted ***')
print(authors)

# self check exercises
print('---------------------')
print('> SELF CHECK 17.2.1 <')
print('---------------------')
print(pd.read_sql('SELECT title, edition FROM titles ORDER BY edition DESC', connection).head(3))
print('---------------------')
print('> SELF CHECK 17.2.2 <')
print('---------------------')
print(pd.read_sql('SELECT * FROM authors WHERE first LIKE \'A%\'', connection))
print('---------------------')
print('> SELF CHECK 17.2.3 <')
print('---------------------')
print(pd.read_sql('SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE \'%How to Program\' ORDER BY title', connection))

# close the connection to the database
connection.close()
















