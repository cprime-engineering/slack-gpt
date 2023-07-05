import unittest

from PromptTemplates.RFPCopilotTemplate import RFPCopilotTemplate

class Testing(unittest.TestCase):
    def test_greeting(self):
        rfp_copilot_template = RFPCopilotTemplate()
        expected_greeting = "Bid Buddy reporting for duty! I'm here to help."
        actual_greeting = rfp_copilot_template.greeting()
        self.assertEqual(expected_greeting, actual_greeting)

if __name__ == '__main__':
    unittest.main()