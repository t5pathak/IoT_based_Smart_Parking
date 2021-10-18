#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#


import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import datetime
import smtplib
continue_reading = True

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def servo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    servo1 = GPIO.PWM(11,50)
    servo1.start(0)
    servo1.ChangeDutyCycle(2)
    time.sleep(3)
    servo1.ChangeDutyCycle(7)
    time.sleep(3)
    servo1.ChangeDutyCycle(2)
    servo1.ChangeDutyCycle(0)
    servo1.stop()
    GPIO.cleanup()

def mail(naame, time_in, time_out, time_total, eemail,loc):
                
                c = str(time_total)
                cost_time = ( (3600*int(c[0])) + (((int(c[2])*10) + int(c[3]))*60) + ((int(c[5])*10) + int(c[6])) ) 
                cost = cost_time * 0.01

                wallet[loc] = wallet[loc] - cost

                #print "Cost is = ",cost

                msg = MIMEMultipart()
                msg['From'] = 'smartparkingiiit@outlook.com'
                msg['To'] = eemail
                msg['Subject'] = 'Smart Parking Bill'
                bill = "Dear "+naame+",\n\nThis is your bill for the parking services.\n\nIn-time : "+str(time_in)+".\nOut-time : "+str(time_out)+".\n\nBased on your parked time and charges price as 36 Rupees/hour,your total bill is: Rs."+str(cost)+"\n\nRemaining balance in Wallet: Rs."+str(wallet[loc])+"\n\nThank You." 
                message = bill
                msg.attach(MIMEText(message))
    
                server = smtplib.SMTP('smtp.outlook.com',587) #Connects to SMTP sever at timeout 587sec
                server.ehlo()
                server.starttls() #Puts SMTP in TLS ( transport layer security) mode for encryption
                server.ehlo()
                server.login('smartparkingiiit@outlook.com', 'Utkarsh@2001') #Username and Password mentioned
                server.sendmail("smartparkingiiit@outlook.com",eemail,msg.as_string())
                server.quit()

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "\n\n****************************Welcome to our IOT project - THE SMART PARKING******************************"
print "\n(Press Ctrl-C to terminate the program)\n"

entry = [0 for i in range(5000)] #Array to check if the car is going in or coming out

card = [ 0 for i in range(5000)] #Array of registered users
card[541] = 1
card[529] = 1
card[758] = 1
card[468] = 1
card[598] = 1


name = ["" for i in range(5000)] #Array of names of users
email = ["" for i in range(5000)] # Array of emails of users
wallet = [0 for i in range(5000)] #Array of values in Wallet
wallet[541] = 1000
wallet[529] = 1000
wallet[758] = 1000
wallet[468] = 1000
wallet[598] = 1000

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "CARD DETECTED\n"
         
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
#        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])

        if uid[0] + uid[1] + uid[2] + uid[3] == 541:
            if entry[541] == 0 :
                print 40 * "-" 
                print "Welcome to Parking Lot : Utkarsh Mishra"
                entry[541] = 1
                time_a_in = datetime.datetime.now().replace(microsecond = 0 )
                print "Your in time is : ",time_a_in
                print 40 * "-"
                servo()
            else:
                email_a = "v.utkarsh01@gmail.com"
                time_a_out = datetime.datetime.now().replace(microsecond = 0 )
                time_a = time_a_out - time_a_in
                print 40 * "-"
                print "Thank You for using our service.\nTotal Time Parked: ",time_a,"\nPlease check your mail for total bill"
                print 40 * "-"
                entry[541] = 0
                name_m = "Utkarsh Mishra"
                mail(name_m, time_a_in, time_a_out, time_a, email_a,541)
                servo()


        elif uid[0] + uid[1] + uid[2] + uid[3] == 529:
            if entry[529] == 0 : 
                print 40 * "-"
                print "Welcome to Parking Lot : Tanmay Pathak"
                entry[529] = 1
                time_b_in = datetime.datetime.now().replace(microsecond = 0 )
                print "Your in time is : ",time_b_in
                print 40 * "-"
                servo()
            else:
                email_b = "tanmay.pathak00@gmail.com"
                time_b_out = datetime.datetime.now().replace(microsecond = 0 )
                time_b = time_b_out - time_b_in
                print 40 * "-"
                print "Thank You for using our service.\nTotal Time Parked: ",time_b,"\nPlease check your mail for total bill"
                print 40 * "-"
                entry[529] = 0
                name_m = "Tanmay Pathak" 
                mail(name_m, time_b_in, time_b_out, time_b, email_b,529)
                servo()

        elif uid[0] + uid[1] + uid[2] + uid[3] == 758:
            if entry[758] == 0 : 
                print 40 * "-"
                print "Welcome to Parking Lot : Hasir Mushtaq"
                entry[758] = 1
                time_c_in = datetime.datetime.now().replace(microsecond = 0 )
                print "Your in time is : ",time_c_in
                print 40 * "-"
                servo()
            else:
                email_c = "hasir.mushtaq@students.iiit.ac.in"
                time_c_out = datetime.datetime.now().replace(microsecond = 0 )
                time_c = time_c_out - time_c_in
                print 40 * "-"
                print "Thank You for using our service.\nTotal Time Parked: ",time_c,"\nPlease check your mail for total bill"
                entry[758] = 0
                name_m = "Hasir Mushtaq"
                mail(name_m, time_c_in, time_c_out, time_c, email_c,758)
                servo()


        elif uid[0] + uid[1] + uid[2] + uid[3] == 468:
            if entry[468] == 0 :
                print 40 * "-"
                print "Welcome to Parking Lot : Nikhil Bishnoi"
                entry[468] = 1
                time_d_in = datetime.datetime.now().replace(microsecond = 0 )
                print "Your in time is : ",time_d_in
                print 40 * "-"
                servo()
            else:
                email_d = "nikhilbish@gmail.com"
                time_d_out = datetime.datetime.now().replace(microsecond = 0 )
                time_d = time_d_out - time_d_in
                print 40 * "-"
                print "Thank You for using our service.\nTotal Time Parked: ",time_d,"\nPlease check your mail for total bill"
                print 40 * "-"
                entry[468] = 0
                name_m = "Nikhil Bishnoi"
                mail(name_m, time_d_in, time_d_out, time_d , email_d,468)
                servo()


        elif uid[0] + uid[1] + uid[2] + uid[3] == 598:
            if entry[598] == 0 : 
                print 40 * "-"
                print "Welcome to Parking Lot : Loay Rashid"
                entry[598] = 1
                time_e_in = datetime.datetime.now().replace(microsecond = 0 )
                print "Your in time is : ",time_e_in
                print 40 * "-"
                servo()
            else:
                email_e = "loay.rashid@students.iiit.ac.in"
                time_e_out = datetime.datetime.now().replace(microsecond = 0 )
                time_e = time_e_out - time_e_in
                print 40 * "-"
                print "Thank You for using our service.\nTotal Time Parked: ",time_e,"\nPlease check your mail for total bill"
                print 40 * "-"
                entry[598] = 0
                name_m = "Loay Rashid"
                mail(name_m, time_e_in, time_e_out, time_e, email_e,598)
                servo()

        else :
            if  card [ (uid[0] + uid[1] + uid [2] + uid[3]) ] == 0 :
                
                print "NOT A REGISTERED USER - Pls complete the registration process below\n"
                choice = 0
                while ( choice != 5):
                    print "***************REGISTRATION MENU***************"
                    print "1. Enter Name: "
                    print "2. Enter Email-id: "
                    print "3. Initial Amoount in Wallet:  "
                    print "4. REGISTER"
                    print "\n5. Don't want to register"
                    print "***********************************************"

                    choice = input("Enter your choice: ")

                    if choice == 1 :
                        enter_name = raw_input("Enter your name: ")
                        name [ (uid[0] + uid[1] + uid[2] +uid[3]) ] = enter_name

                    if choice == 2 :
                        enter_email = raw_input("Enter your E-mail id: ")
                        email[ (uid[0] + uid[1] + uid [2] + uid[3] ) ] = enter_email

                    if choice == 3:
                        enter_wallet = input("Enter initial value on wallet: ")
                        wallet[ (uid[0] + uid[1] + uid[2] + uid[3]) ] = enter_wallet
                    if choice == 4:
                        card [ (uid[0] + uid[1] + uid[2] + uid[3]) ] = 1
                        print "REGISTRATION COMPLETE"
                        print 40 * "*"
                        break
            else:

                if entry[(uid[0] + uid[1] + uid[2] + uid[3])] == 0 : 
                    print 40 * "-"
                    print "Welcome to Parking Lot : "+name[(uid[0] + uid[1] + uid[2] + uid[3])]
                    entry[(uid[0] + uid[1] + uid[2] + uid[3])] = 1
                    time_e_in = datetime.datetime.now().replace(microsecond = 0 )
                    print "Your in time is : ",time_e_in
                    print 40 * "-"
                    servo()
                else:
                    email_e = email[(uid[0] + uid[1] + uid[2] + uid[3])]
                    time_e_out = datetime.datetime.now().replace(microsecond = 0 )
                    time_e = time_e_out - time_e_in
                    print 40 * "-"
                    print "Thank You for using our service.\nTotal Time Parked: ",time_e,"\nPlease check your mail for total bill"
                    print 40 * "-"
                    entry[(uid[0] + uid[1] + uid[2] + uid[3])] = 0
                    name_m = name[(uid[0] + uid[1] + uid[2] + uid[3])]
                    mail(name_m, time_e_in, time_e_out, time_e, email_e,(uid[0] + uid[1] + uid[2] + uid[3]))
                    servo()

            time.sleep(1)


#    time.sleep(0.75)
        # Print UID
       # print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
    
        # This is the default key for authentication
       # key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
       # MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        #status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        #if status == MIFAREReader.MI_OK:
         #   MIFAREReader.MFRC522_Read(8)
         #   MIFAREReader.MFRC522_StopCrypto1()
        #else:
        #    print "Authentication error"
        

