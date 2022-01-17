from phue import Bridge
import logging
import RPi.GPIO as GPIO
import time
import datetime

logging.basicConfig()

GPIO.setmode(GPIO.BOARD)
GPIO_S1 = 7
GPIO.setup(GPIO_S1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


Current_State = 0
Previous_State = 0

b = Bridge('192.168.xxx.xxx')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single$
#b.connect()

try:
 print "Schalter ist EINgeschaltet, bitte AUSschalten"
 while GPIO.input(GPIO_S1)==1:
  Current_State = 0 
 print "bereit"

#Schleife bis Strg+C
 while True :
  Current_State = GPIO.input(GPIO_S1)

  if Current_State==1 and Previous_State==0:
   #GPIO.wait_for_edge (7, GPIO.RISING)
   b.set_light(1, 'on', True)
   print "%s: eingeschaltet" % datetime.datetime.now()
   Previous_State=1
   time.sleep (1)

  elif  Current_State==0 and Previous_State==1:
   #GPIO.wait_for_edge (7, GPIO.FALLING)
   b.set_light(1, 'on', False)
   print "%s: ausgeschaltet" % datetime.datetime.now()
   Previous_State=0
   time.sleep  (1)

  time.sleep (0.01)


except KeyboardInterrupt:
 print "Beenden"
 GPIO.cleanup()
