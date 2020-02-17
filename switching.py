import os 
import subprocess
import serial
from time import sleep
ser=serial.Serial('/dev/ttyACM0',57600)
flag=0
while ser.in_waiting==True:
	ser.readline()
while True:
	if ser.isOpen()==True:
		x=ser.readline()
		x.strip()
		print int(x)
	else:
		subprocess.call("sh urc_1.sh",shell=True)
		subprocess.call("sh kill.sh",shell=True)		
