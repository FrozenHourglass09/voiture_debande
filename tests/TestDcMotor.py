import unittest
from unittest.mock import MagicMock, patch
from code import DCMotor
import RPi.GPIO as GPIO

class TestDCMotor(unittest.TestCase):
    def setUp(self):
        GPIO.setmode = MagicMock()
        GPIO.setup = MagicMock()
        GPIO.PWM = MagicMock(return_value=MagicMock())
        self.motor = DCMotor(17, 18, 27)
        self.motor.pwm = MagicMock()

    def test_stop(self):
        self.motor.set_speed(50)
        self.motor.stop()
        self.motor.pwm.ChangeDutyCycle.assert_called_with(0)
        self.assertEqual(self.motor.speed, 0)

    def test_accelerate(self):
        self.motor.set_speed(50)
        self.motor.accelerate()
        self.motor.pwm.ChangeDutyCycle.assert_called_with(60)
        self.assertEqual(self.motor.speed, 60)

    def test_decelerate(self):
        self.motor.set_speed(50)
        self.motor.decelerate()
        self.motor.pwm.ChangeDutyCycle.assert_called_with(40)
        self.assertEqual(self.motor.speed, 40)

if __name__ == '__main__':
    unittest.main()