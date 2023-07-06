"""Module providing unit tests for RFPCopilotTemplate class."""
import unittest
from console.prompt_templates.rfp_copilot_template import RFPCopilotTemplate

class TestCase(unittest.TestCase):
    """RFPCopilotTemplate unit tests"""

    def test_greeting(self):
        """Test greeting() method."""
        rfp_copilot_template = RFPCopilotTemplate()
        expected_greeting = "Hi, I'm Ada, your RFP Support Specialist. How can I help you today?"
        actual_greeting = rfp_copilot_template.greeting()
        self.assertEqual(expected_greeting, actual_greeting)

    def test_help(self):
        """Test help() method."""
        rfp_copilot_template = RFPCopilotTemplate()
        expected_help = "I can help with writing RFP responses, finding answers to questions, and more."
        actual_help = rfp_copilot_template.help()
        self.assertEqual(expected_help, actual_help)

if __name__ == '__main__':
    unittest.main()
