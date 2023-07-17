import unittest
import pandas as pd

from agents.ada.knowledge_base import get_chunks

class TestCase(unittest.TestCase):
    """knowledge_base unit tests"""

    def test_get_data(self):
        """Test get_data method."""
        print(get_chunks()[0])
        self.assertEqual(1,1)


if __name__ == "__main__":
    unittest.main()