from datetime import date
from langchain import PromptTemplate

from agents.ada.pre_prompt_templates import PrePromptTemplates

version_number = "v0.0.0"

pre_prompt_templates = PrePromptTemplates("agents/ada/pre_prompts/")

date_template_content = pre_prompt_templates.date_template.content()
footer_template_content = pre_prompt_templates.footer_template.content()
persona_template_content = pre_prompt_templates.persona_template.content()
personalized_template_content = pre_prompt_templates.personalized_template.content()
version_template_content = pre_prompt_templates.version_template.content()


def default_template():
    prompt_template = PromptTemplate(
        input_variables=["history", "human_input"],
        template=persona_template_content + footer_template_content,
    )
    return prompt_template


def personalized_template(human_name):
    prompt_template = PromptTemplate(
        input_variables=["history", "human_input"],
        template=persona_template_content
        + version_template_content.format(version_number=version_number)
        + date_template_content.format(date=date.today().strftime("%B %d, %Y"))
        + personalized_template_content.format(human_name=human_name)
        + footer_template_content,
    )
    return prompt_template
