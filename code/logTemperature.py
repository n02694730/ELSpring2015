#!/usr/bin/python
# -*- coding: utf-8 -*-


#####https://docs.python.org/2/library/sqlite3.html###########


import sqlite3
import sys
import os
import time
""" Log Current Time, Temperature in Celsius and Fahrenheit
 Returns a list [time, tempC, tempF] """
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-00000698efc7/w1_slave")
	tempfile_text = tempfile.read()
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	return [currentTime, tempC, tempF]


con = None

try:
    con = sqlite3.connect("myTemperature.db")
    cur = con.cursor()    
    cur.execute('CREATE TABLE IF NOT EXISTS tempData2(time text, tempC real, tempF real)')                   
    temp_info = readTemp()
    print "Current temperature is: ", temp_info[2], "F"
    cur.execute('INSERT INTO tempData2 VALUES (?,?,?)', temp_info)
    con.commit()
    print "Temperature logged"     
except sqlite3.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
