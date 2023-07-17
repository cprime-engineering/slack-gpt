"""Module providing unit tests for Ada Slackbot class."""
import unittest
import json
from agents.ada.prompt_generator import personalized_template


class TestCase(unittest.TestCase):
    """prompt_generator unit tests"""

    def test_personalized_template(self):
        """Test personalized_template method."""

        f = open('tests/ada/expected_prompt_content/personalized.json')
        data = json.load(f)
        f.close

        expected_template_content = str(data["content"])
        actual_template_content = str(personalized_template("INJECTED_USER_NAME"))

        self.assertEqual(expected_template_content, actual_template_content)
        print(actual_template_content)



if __name__ == "__main__":
    unittest.main()