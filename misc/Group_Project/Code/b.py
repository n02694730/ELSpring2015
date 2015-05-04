#!/usr/bin/python3
import os.path
import csv 
import sqlite3 as mydb
import sys 
import time


def readTemp():
#-------------------------------------------------------------------------------------------------------------------------
        tempfile = open("/sys/bus/w1/devices/28-00000697426f/w1_slave")    # temp sensor 2 meters
        tempfile_text = tempfile.read()    
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000      # gets temperature from sensor. It will be in C.
        date=time.strftime('%Y/%m/%d-%X')                                  # gets date and time 
        meter2=tempC*9.0/5.0+32.0                                          # converts the temperature to F.



        tempfile = open("/sys/bus/w1/devices/28-00043a5747ff/w1_slave")   # temp sensor 4 meters
        tempfile_text = tempfile.read()    
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000    
        meter4=tempC*9.0/5.0+32.0    

        tempfile = open("/sys/bus/w1/devices/28-00043a570dff/w1_slave")    # temp sensor 6 meters
        tempfile_text = tempfile.read()    
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000    
        meter6=tempC*9.0/5.0+32.0    

        tempfile = open("/sys/bus/w1/devices/28-00043cc047ff/w1_slave")    # temp sensor 8 meters
        tempfile_text = tempfile.read()    
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000    
        meter8=tempC*9.0/5.0+32.0    


        tempfile = open("/sys/bus/w1/devices/28-00043eb78eff/w1_slave")    # temp sensor 10 meters
        tempfile_text = tempfile.read()
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000    
        meter10=tempC*9.0/5.0+32.0    

        con = mydb.connect('/home/pi/b.db')

        with con:
                cur = con.cursor()
                cur.execute('''insert into temps(date, meter2, meter4, meter6, meter8, meter10)values(?,?,?,?,?,?)''', (date, meter2, meter4, meter6, meter8, meter10))
                data = cur.execute("select * from temps")

readTemp()

