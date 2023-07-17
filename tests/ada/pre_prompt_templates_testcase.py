"""Module providing unit tests for Ada Slackbot class."""
import unittest
from agents.ada.pre_prompt_templates import PrePromptTemplates

pre_prompt_templates = PrePromptTemplates("agents/ada/pre_prompts/")
expected_pre_prompt_templates = PrePromptTemplates("tests/ada/expected_pre_prompts/")


class TestCase(unittest.TestCase):
    """pre_prompt_templates unit tests"""

    def test_date_template(self):
        """Test date_template.content() method."""
        actual_template = pre_prompt_templates.date_template.content()
        expected_template = expected_pre_prompt_templates.date_template.content()
        self.assertEqual(expected_template, actual_template)

    def test_footer_template(self):
        """Test footer_template.content() method."""
        actual_template = pre_prompt_templates.footer_template.content()
        expected_template = expected_pre_prompt_templates.footer_template.content()
        self.assertEqual(expected_template, actual_template)

    def test_persona_template(self):
        """Test persona_template.content() method."""
        actual_template = pre_prompt_templates.persona_template.content()
        expected_template = expected_pre_prompt_templates.persona_template.content()
        self.assertEqual(expected_template, actual_template)

    def test_personalized_template(self):
        """Test personalized_template.content() method."""
        actual_template = pre_prompt_templates.personalized_template.content()
        expected_template = (
            expected_pre_prompt_templates.personalized_template.content()
        )
        self.assertEqual(expected_template, actual_template)

    def test_version_template(self):
        """Test personalized_template.content() method."""
        actual_template = pre_prompt_templates.version_template.content()
        expected_template = expected_pre_prompt_templates.version_template.content()
        self.assertEqual(expected_template, actual_template)


if __name__ == "__main__":
    unittest.main()
