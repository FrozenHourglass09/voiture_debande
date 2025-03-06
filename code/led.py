import RPi.GPIO as GPIO  
import time              

LED = 18
BUTTON = 23

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED,GPIO.OUT)  
GPIO.setup(BUTTON,GPIO.IN) 

mode_auto = 0
last_button_statement = 0

try:
    while True:     

        if GPIO.input(BUTTON) == 1 and last_button_statement != 1:
            if mode_auto == 1:
                mode_auto = 0
                print("NoAuto")
            else:
                mode_auto = 1
                print("Auto")
            print("Bouton")
            last_button_statement = 1
        elif GPIO.input(BUTTON) == 0 :
            last_button_statement = 0

        if mode_auto == 1 :
            GPIO.output(LED,GPIO.HIGH)   
            time.sleep(1)               
            GPIO.output(LED,GPIO.LOW)    
            time.sleep(1)               
except KeyboardInterrupt:
        GPIO.output(LED, GPIO.LOW)      
        GPIO.cleanup()                 