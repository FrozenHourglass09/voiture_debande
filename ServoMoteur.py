# servo.py

class Servo:
    def __init__(self, gpio_adapter, pin=12, freq=50):
        # Injection de la dépendance GPIO (réelle ou mockée)
        self.gpio = gpio_adapter
        
        # Configuration du pin et PWM
        self.gpio.setup_pin(pin)
        self.pwm = self.gpio.create_pwm(pin, freq)
        self.pwm.start(0)
    
    def set_angle(self, angle):
        if not 0 <= angle <= 180:
            raise ValueError("Angle must be between 0 and 180")
        
        duty_cycle = 2.5 + (angle / 180) * 10
        self.pwm.ChangeDutyCycle(duty_cycle)
    
    def cleanup(self):
        self.pwm.stop()
        self.gpio.cleanup()