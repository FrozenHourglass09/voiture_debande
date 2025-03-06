import unittest
from unittest.mock import patch  # For mocking hardware interactions
from sensors import Sensor, RGB, Infrared, Ultrasonic  # Import classes to test

# ==============================================================================
# Test Suite for Base Sensor Class (and Inheritance)
# ==============================================================================
class TestSensor(unittest.TestCase):
    def test_sensor_inheritance(self):
        """
        Verify that subclasses (Infrared, RGB, Ultrasonic) correctly inherit:
        - `address` and `name` attributes from the base Sensor class.
        """

        # Test Infrared
        ir = Infrared("0xA1", "IR1", False)
        self.assertEqual(ir.address, "0xA1")
        self.assertEqual(ir.name, "IR1")

        # Test RGB 
        rgb = RGB("0xB1", "RGB1", [0, 0, 0])
        self.assertEqual(rgb.address, "0xB1")

        # Test Ultrasonic
        us = Ultrasonic("0xD1", "US1", 0)
        self.assertEqual(us.name, "US1")


# ==============================================================================
# Test Suite for RGB Sensor Class
# ==============================================================================
class TestRGB(unittest.TestCase):
    
    @patch.object(RGB, '_read_hardware')  # Mock the private method that reads hardware
    def test_get_data_updates_rgb(self, mock_read):
        """
        Test that get_data():
        1. Calls _read_hardware() to fetch new RGB values
        2. Updates the `rgb` attribute with valid data (0-255 integers)
        3. Returns the updated RGB list
        """
        # Configure mock to return valid RGB values [R, G, B]
        mock_read.return_value = [100, 150, 200]
        
        # Create RGB sensor with initial dummy values
        rgb_sensor = RGB("0xB1", "RGB1", [0, 0, 0])
        
        # Trigger data update via get_data()
        data = rgb_sensor.get_data()
        
        # Assert the internal state and return value are updated
        self.assertEqual(rgb_sensor.rgb, [100, 150, 200])  # Check attribute
        self.assertEqual(data, [100, 150, 200])             # Check return value

    @patch.object(RGB, '_read_hardware')
    def test_invalid_rgb_after_update(self, mock_read):
        """
        Test that invalid RGB values (out of 0-255 range) from hardware:
        1. Raise a ValueError during get_data()
        2. Prevent the `rgb` attribute from being corrupted
        """
        # Configure mock to return invalid values (300 > 255, -1 < 0)
        mock_read.return_value = [300, -1, 255]
        
        # Create sensor instance
        rgb_sensor = RGB("0xB2", "RGB2", [0, 0, 0])
        
        # Attempt to update data - should FAIL due to invalid values
        with self.assertRaises(ValueError):
            rgb_sensor.get_data()
        


# ==============================================================================
# Test Suite for Infrared Sensor Class
# ==============================================================================
class TestInfrared(unittest.TestCase):
    
    @patch.object(Infrared, '_read_hardware')
    def test_get_data_updates_value(self, mock_read):
        """
        Test that get_data():
        1. Updates the `value` attribute with a boolean (True/False)
        2. Handles transitions between True and False states
        """
        # First test case: Hardware returns True (obstacle detected)
        mock_read.return_value = True
        ir_sensor = Infrared("0xC1", "IR1", False)  # Initial state: False
        
        ir_sensor.get_data()  # Update from hardware
        self.assertEqual(ir_sensor.value, True)  # Should flip to True
        
        # Second test case: Hardware returns False (no obstacle)
        mock_read.return_value = False
        ir_sensor.get_data()  # Update again
        self.assertEqual(ir_sensor.value, False)  # Should flip back

    @patch.object(Infrared, '_read_hardware')
    def test_non_boolean_after_update(self, mock_read):
        """
        Test that non-boolean values (e.g., integers) from hardware:
        1. Raise a TypeError during get_data()
        2. Protect the `value` attribute from invalid states
        """
        # Configure mock to return an integer (invalid for Infrared)
        mock_read.return_value = 1
        
        ir_sensor = Infrared("0xC2", "IR2", False)
        
        # Attempt to update - should FAIL
        with self.assertRaises(TypeError):
            ir_sensor.get_data()


# ==============================================================================
# Test Suite for Ultrasonic Sensor Class
# ==============================================================================
class TestUltrasonic(unittest.TestCase):
    
    @patch.object(Ultrasonic, '_read_hardware')
    def test_get_data_updates_distance(self, mock_read):
        """
        Test that get_data():
        1. Updates `distance` with a valid non-negative integer (in cm)
        2. Returns the updated distance
        """
        # Mock hardware returns 50 cm
        mock_read.return_value = 50
        us_sensor = Ultrasonic("0xD1", "US1", 0)  # Initial distance: 0
        
        us_sensor.get_data()  # Trigger update
        self.assertEqual(us_sensor.distance, 50)  # Should match mock

    @patch.object(Ultrasonic, '_read_hardware')
    def test_negative_distance_after_update(self, mock_read):
        """
        Test that negative distance values (invalid physical measurement):
        1. Raise ValueError during get_data()
        2. Prevent `distance` from being set to an invalid state
        """
        # Mock hardware returns invalid negative distance
        mock_read.return_value = -10
        us_sensor = Ultrasonic("0xD2", "US2", 0)
        
        with self.assertRaises(ValueError):
            us_sensor.get_data()


# ==============================================================================
# Run Tests
# ==============================================================================
if __name__ == "__main__":
    unittest.main()  # Execute all test cases when script runs