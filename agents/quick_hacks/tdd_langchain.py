import os
from langchain.llms import OpenAI

openai_api_key = os.environ.get("CPRIME_OPENAI_API_KEY")
llm = OpenAI(openai_api_key=openai_api_key, model_name="text-davinci-003")
print(llm("Explain TDD in one paragraph"))
