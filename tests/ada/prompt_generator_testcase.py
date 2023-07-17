"""Module providing unit tests for Ada Slackbot class."""
import unittest
import json
from datetime import date

from agents.ada.prompt_generator import personalized_template


class TestCase(unittest.TestCase):
    """prompt_generator unit tests"""

    @unittest.skip("refactor test when development more stable")
    def test_personalized_template(self):
        """Test personalized_template method."""

        expected_date = date.today().strftime("%B %d, %Y")
        expected_human_name = "Kevin"
        expected_version_number = "v0.0.0"

        f = open("tests/ada/expected_prompt_content/personalized.json")
        data = json.load(f)
        f.close

        expected_template_content = str(data["content"])

        expected_template_content.format(
            human_name=expected_human_name,
            date=expected_date,
            version_number=expected_version_number,
        )
        actual_template_content = str(personalized_template("INJECTED_USER_NAME"))

        self.assertEqual(expected_template_content, actual_template_content)
        print(actual_template_content)


if __name__ == "__main__":
    unittest.main()
