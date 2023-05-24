import psycopg2

#  connect to 'chinook' database
connection = psycopg2.connect(database="chinook", user="postgres", password="<pass>")

# built a cursor object of the database (build a list of data)
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select "Name" records from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select tracks where the composer is "Queen" from the "Traks" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# fetch the result (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection 
connection.close()

for result in results:
    print (result)