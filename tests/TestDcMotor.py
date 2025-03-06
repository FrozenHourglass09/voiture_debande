import unittest
from unittest.mock import MagicMock, patch
from code import DCMotor
import RPi.GPIO as GPIO
import time

class TestDCMotor(unittest.TestCase):
    def test_stop(self):
        self.motor.set_speed(50)
        self.motor.stop()
        self.motor.stop.assert_called_once()
        self.motor.speed = 0
        self.assertEqual(self.motor.speed, 0)

    def test_accelerate(self):
        self.motor.set_speed(50)
        self.motor.accelerate()
        self.motor.accelerate.assert_called_once()
        self.motor.speed = 60
        self.assertEqual(self.motor.speed, 60)
        

    def test_decelerate(self):
        self.motor.set_speed(50)
        self.motor.decelerate()
        self.motor.decelerate.assert_called_once()
        self.motor.speed = 40
        self.assertEqual(self.motor.speed, 40)

if __name__ == '__main__':
    unittest.main()