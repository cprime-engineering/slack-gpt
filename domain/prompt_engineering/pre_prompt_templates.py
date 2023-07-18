from dataclasses import dataclass


class PrePromptTemplate:
    template = str()
    path = str()

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
    date_template: PrePromptTemplate
    footer_template: PrePromptTemplate
    persona_template: PrePromptTemplate
    personalized_template: PrePromptTemplate
    version_template: PrePromptTemplate

    def __init__(self, path):
        self.date_template = PrePromptTemplate("date", path)
        self.footer_template = PrePromptTemplate("footer", path)
        self.persona_template = PrePromptTemplate("persona", path)
        self.personalized_template = PrePromptTemplate("personalized", path)
        self.version_template = PrePromptTemplate("version", path)
