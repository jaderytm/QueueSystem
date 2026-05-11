# test_queuesystem.py
"""
Tests for QueueSystem module.
"""

import unittest
from queuesystem import QueueSystem

class TestQueueSystem(unittest.TestCase):
    """Test cases for QueueSystem class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QueueSystem()
        self.assertIsInstance(instance, QueueSystem)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QueueSystem()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
