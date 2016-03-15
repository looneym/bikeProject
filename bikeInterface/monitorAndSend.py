# Reads rotations and incrmements counter on remote database

from time import sleep
import RPi.GPIO as GPIO
import MySQLdb

GPIO.setmode(GPIO.BOARD)

# Declare pin 12 as the input to watch and place a pull up resistor on it
inputPin=12
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

counter = 0

# setup DB connection
db = MySQLdb.connect(host="188.166.168.103", user="", passwd="", port=3306, db="bikeProject")
cursor = db.cursor()

# function for writing to DB
def writeToDB(i):
    global cursor
    sql = """INSERT INTO bikeProject_counter(currentCount) VALUES('%s');""" % (i)
    cursor.execute(sql)
    db.commit()

# For each rotation increment the counter
while(1): 
        if  GPIO.input(inputPin)==0:
                sleep(.3)
                counter+=1
                writeToDB(counter) 



