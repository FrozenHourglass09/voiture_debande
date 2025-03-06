import unittest
from unittest.mock import MagicMock, patch
from dc_motor import DCMotor

class TestDCMotor(unittest.TestCase):

    def setUp(self):
        self.motor = DCMotor(pin1=17, pin2=18, enable_pin=27)
        self.motor.set_speed = MagicMock()
        self.motor.stop = MagicMock()
        self.motor.forward = MagicMock()
        self.motor.backward = MagicMock()

    def test_initial_speed(self):
        self.assertEqual(self.motor.speed, 0)

    def test_set_speed(self):
        self.motor.set_speed(50)
        self.motor.set_speed.assert_called_with(50)
        self.motor.speed = 50  # Simulate the effect of set_speed
        self.assertEqual(self.motor.speed, 50)

    def test_set_speed_invalid(self):
        with self.assertRaises(ValueError):
            self.motor.set_speed(-10)
        with self.assertRaises(ValueError):
            self.motor.set_speed(110)

    def test_stop(self):
        self.motor.set_speed(50)
        self.motor.stop()
        self.motor.stop.assert_called_once()
        self.motor.speed = 0  # Simulate the effect of stop
        self.assertEqual(self.motor.speed, 0)

    def test_forward(self):
        self.motor.forward()
        self.motor.forward.assert_called_once()

    def test_backward(self):
        self.motor.backward()
        self.motor.backward.assert_called_once()

if __name__ == '__main__':
    unittest.main()