#!/usr/bin/python

# ------------------------------------------------------------------------
# Based on Wii-controller code by Matt Hawkins
# http://www.raspberrypi-spy.co.uk/?p=1101
# 
# GoPiGo code by Dexter Industries
# https://github.com/DexterInd/GoPiGo/tree/master/Software/Python/Examples
# ------------------------------------------------------------------------



# --------------------------------
# Import required Python libraries
# --------------------------------

import cwiid
import time
from gopigo import *
import sys

# --------------------------------
# Set up variables
# --------------------------------

button_delay = 0.1
servo_pos=90

# -----------------------------------
# Connect to Wii bluetooth controller
# -----------------------------------

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Control motors with D-pad, stop motors with A. Control servo with PLUS, MINUS and HOME.'  
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    #print 'Left pressed'
    left()
    time.sleep(button_delay)         
    #io.output(2, True)

  if(buttons & cwiid.BTN_RIGHT):
    #print 'Right pressed'
    right()
    time.sleep(button_delay)          
    #io.output(3, True)

  if (buttons & cwiid.BTN_UP):
    #print 'Up pressed'        
    fwd()
    time.sleep(button_delay)          
    #io.output(4, True)
    
  if (buttons & cwiid.BTN_DOWN):
    #print 'Down pressed'      
    bwd()
    time.sleep(button_delay)  
    #io.output(17, True)
    
  if (buttons & cwiid.BTN_1):
    #print 'Button 1 pressed'
    increase_speed()
    #time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    decrease_speed()
    #print 'Button 2 pressed'
    #time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    #print 'Button A pressed'
    stop()
    time.sleep(button_delay)          
    #for i in pins:
      #io.output(i, False)    

  if (buttons & cwiid.BTN_B):
    #print 'Button B pressed'
    time.sleep(button_delay)          

  old_servo_pos = servo_pos
  if (buttons & cwiid.BTN_HOME):
    #print 'Home Button pressed'
    servo_pos=90
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    #print 'Minus Button pressed'
    servo_pos=servo_pos+10
    time.sleep(button_delay)   
    
    
  if (buttons & cwiid.BTN_PLUS):
    #print 'Plus Button pressed'
    servo_pos=servo_pos-10
    time.sleep(button_delay)

  if servo_pos>180:
    servo_pos=180
  if servo_pos<0:
    servo_pos=0

  if(servo_pos != old_servo_pos):
    servo(servo_pos)                # This function updates the servo with $
    time.sleep(.1)                  # Take a break in between operations.

