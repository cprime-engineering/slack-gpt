import unittest
import pandas as pd

from agents.ada.knowledge_base import get_data

class TestCase(unittest.TestCase):
    """knowledge_base unit tests"""

    def test_get_data(self):
        """Test get_data method."""
        data_frame = pd.DataFrame(get_data())
        print(data_frame.iloc[0][0])
        self.assertEqual(1,1)


if __name__ == "__main__":
    unittest.main()