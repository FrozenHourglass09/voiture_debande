import RPi.GPIO as GPIO
import time

IR_PIN = 18 

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

def detecter_obstacle():
    return GPIO.input(IR_PIN)

try:
    while True:
        if detecter_obstacle():
            print("Obstacle detecte !")
        else:
            print("Pas d'obstacle")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Arret du programme")

finally:
    GPIO.cleanup()
