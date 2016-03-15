# Testing script which implements counter by 1 indefinitely

import MySQLdb
from time import sleep


db = MySQLdb.connect(host="188.166.168.103", user="", passwd="", port=3306, db="bikeProject")
cursor = db.cursor()

def incr(i):
    global cursor
    sql = """INSERT INTO bikeProject_counter(currentCount) VALUES('%s');""" % (i)
    cursor.execute(sql)
    db.commit()
    i = i + 1
    sleep(.5)
    incr(i)

incr(1)

