from langchain import PromptTemplate

from agents.ada.pre_prompt_templates import PrePromptTemplates

pre_prompt_templates = PrePromptTemplates("agents/ada/pre_prompts/")

persona_template_content = pre_prompt_templates.persona_template.content()
footer_template_content = pre_prompt_templates.footer_template.content()
personalized_template_content = pre_prompt_templates.personalized_template.content()


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
        + personalized_template_content.format(human_name=human_name)
        + footer_template_content,
    )
    return prompt_template
