from langchain import PromptTemplate

persona_template_content = ""
footer_template_content = ""
personalized_template_content = ""

with open("agents/ada/pre_prompts/persona") as f:
    while True:
        line = f.readline()
        if not line:
            break
        persona_template_content += line

with open("agents/ada/pre_prompts/footer") as f:
    while True:
        line = f.readline()
        if not line:
            break
        footer_template_content += line

with open("agents/ada/pre_prompts/personalized") as f:
    while True:
        line = f.readline()
        if not line:
            break
        personalized_template_content += line


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
