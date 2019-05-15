import time
from serial import Serial
import socket

def Main():
    SER = Serial(
            port = '/dev/ttyS0', #Replace with the serial port that you are using to read information
            baudrate = 9600, #Replace with baudrate that is used by the thing writing to serial
            timeout = 1,
            )
    #UDP CLIENT#

    target_server = "0.0.0.0" #Replace with IP addres for server
    target_port = "80" #Replace with the PORT for the server

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Read Serial Port and Send Data Over UDP

    while True:
        DATA = ser.readline()
        client.sendto(DATA,(target_server, target_port))

Main()
