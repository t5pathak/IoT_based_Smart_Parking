import RPi.GPIO as GPIO
import time
import sys


#CURSOR_UP_ONE = '\x1b[1A'
#ERASE_LINE = '\x1b[2k'

sensor_a = 8
sensor_b = 10
sensor_c = 12
sensor_d = 16
sensor_e = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_a,GPIO.IN)
GPIO.setup(sensor_b,GPIO.IN)
GPIO.setup(sensor_c,GPIO.IN)
GPIO.setup(sensor_d,GPIO.IN)
GPIO.setup(sensor_e,GPIO.IN)

print "Slot Availability Status :\n"
#print "IR Sensor Ready....."
#print " "

# 0 for occupied

total_toggle = 0.0

toggle_a = 0.0
toggle_a_change = 0 

toggle_b = 0.0
toggle_b_change = 0

toggle_c = 0.0
toggle_c_change = 0

toggle_d = 0.0
toggle_d_change = 0

toggle_e = 0.0
toggle_e_change = 0

try:
    while True:

      f = open ( "output.txt","w" )
      file_txt = ""
#**********************************************************************************************#
      file_txt += "Slot A: "
      print"Slot A: ",
      if GPIO.input(sensor_a) == 1:
          if (total_toggle > 0):
              if ( toggle_a_change == 1 ):
                  toggle_a_change = 0
                  file_txt += "Available\t"+ str((100.0 - ((toggle_a/total_toggle)*100.0)))+"%\n"
                  print "Available\t"+str((100.0 - ((toggle_a/total_toggle)*100.0)))+"%\n"
          else:
              file_txt += "Available\n"
              print "Available\n"

      if GPIO.input(sensor_a)== 0:
          total_toggle = total_toggle + 1
          toggle_a = toggle_a + 1
          toggle_a_change = 1
          print "Occupied\t"+str((100.0 - ((toggle_a/total_toggle)*100.0)))+"%\n"
          file_txt += "Occupied\t"+str((100.0 - ((toggle_a/total_toggle)*100.0)))+"%\n"
#**********************************************************************************************#
      file_txt += "Slot B: "
      print"Slot B: ",
      if GPIO.input(sensor_b) == 1 :
          if total_toggle > 0 :
              file_txt += "Available\t"+str((100.0 - ((toggle_b/total_toggle)*100.0)))+"\n"
              print "Available\t"+(100.0 - ((toggle_b/total_toggle)*100.0)))+"\n"
          else:
              file_txt += "Available\n"
              print "Available\n"

      if GPIO.input(sensor_b) == 0:
          total_toggle = total_toggle + 1
          toggle_b = toggle_b + 1
          toggle_b_change = 1
          print "Occupied\t"+str((100.0 - ((toggle_b/total_toggle)*100.0)))+"%\n"
          file_txt += "Occupied\t"+str((100.0 - ((toggle_b/total_toggle)*100.0)))+"%\n"
#**********************************************************************************************#
      file_txt += "Slot C: "
      print"Slot C: ",
      if GPIO.input(sensor_c) == 1:
          if total_toggle > 0:
              file_txt += "Available\t"+str((100.0-((toggle_c/total_toggle)*100.0)))+"%\n"
              print "Available\t"+str((100.0-((toggle_c/total_toggle)*100.0)))+"%\n"
          else:
              print "Available\n"
              file_txt += "Available\n"

      if GPIO.input(sensor_c) == 0:
          total_toggle = total_toggle + 1
          toggle_c = toggle_c + 1
          print "Occupied\t"+str((100.0 - ((toggle_c/total_toggle)*100.0)))+"%\n"
          file_txt += "Occupied\t"+str((100.0 - ((toggle_c/total_toggle)*100.0)))+"%\n"
#***********************************************************************************************#
      file_txt += "Slot D: "
      print"Slot D: ",
      if GPIO.input(sensor_d) == 1:
          if total_toggle > 0:
              file_txt += "Available\t"+str((100.0-((toggle_d/total_toggle)*100.0)))+"%\n"
              print "Available\t"+str((100.0-((toggle_d/total_toggle)*100.0)))+"%\n"
          else:
              print "Available\n"
              file_txt += "Available\n"

      if GPIO.input(sensor_d) == 0:
          total_toggle = total_toggle + 1
          toggle_d = toggle_d + 1
          print "Occupied\t"+str((100.0 - ((toggle_d/total_toggle)*100.0)))+"%\n"
          file_txt += "Occupied\t"+str((100.0 - ((toggle_d/total_toggle)*100.0)))+"%\n"
#***********************************************************************************************#
      print"Slot E: ",
      file_txt += "Slot E: "
      if GPIO.input(sensor_e) == 1:
          if total_toggle > 0:
              file_txt += "Available\t"+str((100.0-((toggle_e/total_toggle)*100.0)))+"%\n"
              print "Available\t"+str((100.0-((toggle_e/total_toggle)*100.0)))+"%\n"
          else:
              print "Available\n"
              file_txt += "Available\n"

      if GPIO.input(sensor_e) == 0:
          total_toggle = total_toggle + 1
          toggle_e = toggle_e + 1
          print "Occupied\t"+str((100.0 - ((toggle_e/total_toggle)*100.0)))+"%\n"
          file_txt += "Occupied\t"+str((100.0 - ((toggle_e/total_toggle)*100.0)))+"%\n"
#***********************************************************************************************#
      f.write(file_txt)
      f.close()
      time.sleep(0.5)

      for i in range(10): 
          sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

except KeyboardInterrupt:

    GPIO.cleanup()
