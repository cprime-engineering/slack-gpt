"""Module providing basic implementation of a interactive agent to test prompt templates."""
from prompt_templates.rfp_copilot_template import RFPCopilotTemplate

rfp_copilot_template = RFPCopilotTemplate()

print(rfp_copilot_template.greeting())
