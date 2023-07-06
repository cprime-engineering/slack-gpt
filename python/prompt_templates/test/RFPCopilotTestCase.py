import unittest

from prompt_templates.RFPCopilotTemplate import RFPCopilotTemplate

class Testing(unittest.TestCase):
    def test_greeting(self):
        rfp_copilot_template = RFPCopilotTemplate()
        expected_greeting = "Hi, I'm Ada, your RFP Support Specialist. How can I help you today?"
        actual_greeting = rfp_copilot_template.greeting()
        self.assertEqual(expected_greeting, actual_greeting)

if __name__ == '__main__':
    unittest.main()
