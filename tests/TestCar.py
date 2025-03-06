import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 
from source.Car import Car

class TestCar(unittest.TestCase):

    def setUp(self):
        # Create an instance of Car to be used in the tests
        self.car = Car()
    
    def test_run(self):
        self.car.run()

    @patch('source.Car.Car.run')
    def test_start(self, mock_run):
        self.car.start()
        self.assertTrue(mock_run.called)

    def test_stop(self):
        self.car.stop()

    def test_check_obstacles(self):
        self.car.check_obstacles()

    def test_check_finish(self):
        self.car.check_finish()

    @patch('source.Car.Car.start')
    def test_check_start(self, mock_start):
        self.car.check_start()
        self.assertTrue(mock_start.called)

if __name__ == '__main__':
    unittest.main()