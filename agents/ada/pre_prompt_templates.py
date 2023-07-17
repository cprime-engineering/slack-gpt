from dataclasses import dataclass


class PrePromptTemplate:
    template = ""
    path = ""

    def __init__(self, template, path):
        self.path = path
        self.template = self.read_template(template)

    def content(self):
        return self.template

    def read_template(self, template_name):
        path = self.path + template_name
        with open(path) as f:
            return f.read()


@dataclass
class PrePromptTemplates:
    persona_template: PrePromptTemplate
    footer_template: PrePromptTemplate
    personalized_template: PrePromptTemplate

    def __init__(self, path):
        self.persona_template = PrePromptTemplate("persona", path)
        self.footer_template = PrePromptTemplate("footer", path)
        self.personalized_template = PrePromptTemplate("personalized", path)
