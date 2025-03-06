# tests/test_servo.py

import unittest
from ServoMoteur import Servo
from mock_gpio import MockGPIOAdapter

class TestServo(unittest.TestCase):
    def setUp(self):
        # Crée un mock de l'Adapter GPIO
        self.mock_gpio = MockGPIOAdapter()
        
        # Injecte le mock dans Servo
        self.servo = Servo(gpio_adapter=self.mock_gpio, pin=12)

    def test_initialization(self):
        # Vérifie que le pin est configuré
        self.mock_gpio.setup_pin.assert_called_with(12)
        
        # Vérifie que le PWM est démarré
        self.mock_gpio.pwm_mock.start.assert_called_with(0)

    def test_set_angle(self):
        self.servo.set_angle(90)
        self.mock_gpio.pwm_mock.ChangeDutyCycle.assert_called_with(7.5)

    # ... (autres tests similaires)

if __name__ == '__main__':
    unittest.main()