"""Module providing unit tests for Ada Slackbot class."""
import unittest
from agents.ada.prompt_generator import personalized_template

expected_personalized_template_content = ""

with open("tests/ada/expected_prompt_content/personalized") as f:
    while True:
        line = f.readline()
        if not line:
            break
        expected_personalized_template_content += line


class TestCase(unittest.TestCase):
    """prompt_generaqtor unit tests"""

    def test_personalized_template(self):
        """Test personalized_template method."""
        test_template = personalized_template("Ada")
        self.assertEqual(expected_personalized_template_content, str(test_template))


if __name__ == "__main__":
    unittest.main()
