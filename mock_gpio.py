# tests/mock_gpio.py

from unittest.mock import Mock

class MockGPIOAdapter:
    def __init__(self):
        self.setup_pin = Mock()
        self.cleanup = Mock()
        
        # Simule un objet PWM avec des méthodes mockées
        self.pwm_mock = Mock()
        self.pwm_mock.start = Mock()
        self.pwm_mock.ChangeDutyCycle = Mock()
        self.pwm_mock.stop = Mock()
    
    def create_pwm(self, pin, freq):
        return self.pwm_mock