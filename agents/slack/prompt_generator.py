
from langchain import PromptTemplate

header_template_content = ""
footer_template_content = ""
personalized_template_content = ""

with open('agents/slack/pre_prompts/header') as f:
    while True:
        line = f.readline()
        if not line:
            break
        header_template_content += line

with open('agents/slack/pre_prompts/footer') as f:
    while True:
        line = f.readline()
        if not line:
            break
        footer_template_content += line

with open('agents/slack/pre_prompts/personalized') as f:
    while True:
        line = f.readline()
        if not line:
            break
        personalized_template_content += line

def default_template():
    prompt_template = PromptTemplate(
    input_variables=["history", "human_input"],
    template= header_template_content + footer_template_content,
    )
    return prompt_template

def personalized_template(human_name):

    prompt_template = PromptTemplate(
    input_variables=["history", "human_input"],
    template= header_template_content + personalized_template_content.format(human_name=human_name) + footer_template_content,
    )
    return prompt_template