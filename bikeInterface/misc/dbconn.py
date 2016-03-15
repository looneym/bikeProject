# Connect to remote database and perform queries as needed
# Replace user and paswd with valid credentials

# For command line access use:
# mysql -u <username> -p -h 188.166.168.103

import MySQLdb

# connect to the database
db = MySQLdb.connect(host="188.166.168.103", user="", passwd="", port=3306, db="bikeProject")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Insert raw SQL query, change VALUES() as needed
sql = """INSERT INTO bikeProject_counter(currentCount)  VALUES ();

"""
# Execute query and commit changes
cursor.execute(sql)
db.commit()

# disconnect from server
db.close()




