#!/usr/bin/env python
# BRICKPI LEGO EV3 Ultrasonic SENSOR EXAMPLE.
############################################
#
# NOTE: This program is in BETA now
# 
# This example will show you how to use the LEGO EV3 Ultrasonic sensor with the BrickPi.  
# Note you must have the latest firmware installed on the BrickPi or this example to work.  
# Sensor is attached to Port 4.
##
# Select the mode of operation below.  These are the modes of operation for the gyro.
# TYPE_SENSOR_EV3_INFRARED_M0  		# Proximity, 0 to 100
# TYPE_SENSOR_EV3_INFRARED_M1   	# IR Seek, -25 (far left) to 25 (far right)
# TYPE_SENSOR_EV3_INFRARED_M2   	# IR Remote Control, 0 - 11 
##
#
# Original Author: John
# Initial Date: June 13, 2014
# http://www.dexterindustries.com/BrickPi
#
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)

from BrickPi import *   								#import BrickPi.py file to use BrickPi operations
BrickPiSetup()  										# setup the serial port for communication
############################################
# !  Set the sensor type on the line below.  
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_EV3_INFRARED_M0   	#Set the type of sensor at PORT_4.  M0 is proximity, 0 to 100. 
BrickPiSetupSensors()   									#Send the properties of sensors to BrickPi.  Set up the BrickPi.
# There's often a long wait for setup with the EV3 sensors.  Up to 5 seconds.

while True:
	result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors 
	if not result :
		infrared = BrickPi.Sensor[PORT_1]
		print str(infrared)
		
	time.sleep(.1)     # sleep for 10 ms

