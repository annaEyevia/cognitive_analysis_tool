import csv
import matplotlib.pyplot as plt
from scipy import signal
import numpy
from datetime import *
import os
import errno
import cv2
import time as t
import serial
import serial.tools.list_ports
from os.path import expanduser
home = expanduser("~")


def add_new_data(data_point , data_source):
	now = datetime.now().timetuple()
	day = datetime.now().strftime("%Y-%m-%d")
	u_now = t.time()*1000

	fileName = str(now[1])+"_"+ str(now[2]) +"_"+ str(now[3]) + ".csv";
	fileName = data_source+'/'+fileName
	if not os.path.exists(os.path.dirname(fileName)):
		try:
			os.makedirs(os.path.dirname(fileName))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise

	row = [u_now,str(now[2]),str(now[3]),str(now[4]),data_point]

	with open( fileName, 'a') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row)
		csvFile.close()

def logLux(self):

	
	data_source=self.settingsDict['luxFolder']
	ports = list(serial.tools.list_ports.comports())

	for p in ports:
		print (p) 
		if "USB2.0-Serial" in p[1]:
			print ("This is a generic seria thing")
			ser = serial.Serial(
				port=p[0],
				baudrate = 250000,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS,
				timeout=0.3)
			break
	
		if "Adafruit" in p[1]:
			print ("This is an Adafruit")
			ser = serial.Serial(
				port=p[0],
				baudrate = 250000,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS,
				timeout=0.3)
			break

		if "Arduino" in p[1]:
			print ("This is an Arduino")
			ser = serial.Serial(
				port=p[0],
				baudrate = 250000,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS,
				timeout=0.3)
			break

		if "IOUSBHostDevice" in p[1]:
			print ("This is an Moteino")
			ser = serial.Serial(
				port=p[0],
				baudrate = 250000,
				parity=serial.PARITY_NONE,
				stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS,
				timeout=0.3)
			break

	while True:
		message=ser.readline()


		if message:
			try:
				message=float(message.decode(encoding='UTF-8',errors='strict'))
				self.w.luxButtonCaption.set(str(message)+" cd/m2")
				add_new_data(message,data_source)
				print (message)

	
			except Exception as e:
				print (e)
		 

			
		

		
