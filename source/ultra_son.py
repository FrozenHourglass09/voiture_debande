import RPi.GPIO as GPIO
import time

TRIG = 23  # Broche Trig du HC-SR04
ECHO = 24  # Broche Echo du HC-SR04

# Configuration des GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def mesurer_distance():
    GPIO.output(TRIG, True)
    GPIO.output(TRIG, False)

    # Mesure du temps aller-retour de l'onde sonore
    debut_pulse = time.time()
    while GPIO.input(ECHO) == 0:
        debut_pulse = time.time()

    fin_pulse = time.time()
    while GPIO.input(ECHO) == 1:
        fin_pulse = time.time()

    # Calcul de la distance
    duree = fin_pulse - debut_pulse
    distance = (duree * 34300) / 2 

    return round(distance, 2)

try:
    while True:
        dist = mesurer_distance()
        print(f"Distance mesu : {dist} cm")
        time.sleep(1)  # Pause d'1 seconde

except KeyboardInterrupt:
    print("Ar du programme")
    GPIO.cleanup()
