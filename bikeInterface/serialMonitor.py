import serial
ser = serial.Serial('/dev/tty.usbmodem1411', 9600) # Establish the connection on a specific port at 9600 baud


while True: # run forever
     print ser.readline() # Read the output from the arduino and print it to the console
     
