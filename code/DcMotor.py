import RPi.GPIO as GPIO
import time

class DCMotor():
    def __init__(self, pin1, pin2, pin_pwm):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin_pwm = pin_pwm
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin_pwm, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin_pwm, 100)
        self.pwm.start(0)
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        self.pwm.ChangeDutyCycle(self.speed)

    def get_speed(self):
        return self.speed

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        if self.speed > 100:
            self.speed = 100
        self.pwm.ChangeDutyCycle(self.speed)

    def decelerate(self):
        self.speed -= 10
        if self.speed < -50:
            self.speed = -50
        self.pwm.ChangeDutyCycle(self.speed)