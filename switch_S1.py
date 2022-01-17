from phue import Bridge
import logging
import RPi.GPIO as GPIO
import time
import datetime

logging.basicConfig()

#Die GPIO sind meinen eingänge am Raspi Mit GPIO7 wir Schalter1 = S1 ausgewertet
GPIO.setmode(GPIO.BOARD)
GPIO_S1 = 7
GPIO.setup(GPIO_S1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Setzten der Variablen auf 0, um einen definierten Anfangszustand zu haben
Current_State_S1 = 0
Previous_State_S1 = 0

#definieren der HUE-Bridge
b = Bridge('192.168.xxx.xxx')

#Bekanntmachen des scriptes in der Bridge
#If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single$
#b.connect()

#Prüfung dass der Schalter ausgeschaltet ist
try:
 print "Schalter ist EINgeschaltet, bitte AUSschalten"
 while GPIO.input(GPIO_S1)==1:
  Current_State_S1 = 0 
 print "bereit"

#Schleife bis Strg+C
 while True :
  Current_State_S1 = GPIO.input(GPIO_S1)

  if Current_State_S1==1 and Previous_State_S1==0:
   #GPIO.wait_for_edge (7, GPIO.RISING)
   b.set_light(1, 'on', True)
   b.set_light(9, 'on', True)
   print "%s: eingeschaltet" % datetime.datetime.now()
   Previous_State_S1=1
   time.sleep (1)

  elif  Current_State_S1==0 and Previous_State_S1==1:
   #GPIO.wait_for_edge (7, GPIO.FALLING)
   b.set_light(1, 'on', False)
   b.set_light(9, 'on', False)
   print "%s: ausgeschaltet" % datetime.datetime.now()
   Previous_State_S1=0
   time.sleep  (1)

  time.sleep (0.01)

#Change the light state
#b.set_light(1, 'on', True)

except KeyboardInterrupt:
 print "Beenden"
 GPIO.cleanup()
