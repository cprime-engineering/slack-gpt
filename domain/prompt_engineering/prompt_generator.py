from datetime import date
from langchain import PromptTemplate

from domain.prompt_engineering.pre_prompt_templates import PrePromptTemplates

class PromptGenerator:

    pre_prompt_templates_path = str()
    date_template_content = str()
    footer_template_content = str()
    persona_template_content = str()
    personalized_template_content = str()
    version_template_content = str()

    def __init__(self, pre_prompt_templates_path):
        self.pre_prompt_templates_path = pre_prompt_templates_path


    def default_template(self):

        self.generate_template_content()

        prompt_template = PromptTemplate(
            input_variables=["history", "human_input"],
            template=self.persona_template_content + self.footer_template_content,
        )
        return prompt_template


    def personalized_template(self, human_name, version_number):

        self.generate_template_content()
        
        prompt_template = PromptTemplate(
            input_variables=["history", "human_input"],
            template=self.persona_template_content
            + self.version_template_content.format(version_number=version_number)
            + self.date_template_content.format(date=date.today().strftime("%B %d, %Y"))
            + self.personalized_template_content.format(human_name=human_name)
            + self.footer_template_content,
        )
        return prompt_template


    def generate_template_content(self):
        
        pre_prompt_templates = PrePromptTemplates(self.pre_prompt_templates_path)

        self.date_template_content = pre_prompt_templates.date_template.content()
        self.footer_template_content = pre_prompt_templates.footer_template.content()
        self.persona_template_content = pre_prompt_templates.persona_template.content()
        self.personalized_template_content = pre_prompt_templates.personalized_template.content()
        self.version_template_content = pre_prompt_templates.version_template.content()
