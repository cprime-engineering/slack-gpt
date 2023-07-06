# documentation: https://python.langchain.com/docs/modules/chains/
# requires environment variable "OPENAI_API_KEY"

import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

user_input = "programming"

prompt = PromptTemplate(
    input_variables=["concept"],
    template="Define {concept} with a real-world example?",
)

print(prompt.format(concept=user_input))

openai_api_key = os.environ.get("CPRIME_OPENAI_API_KEY")
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)
chain = LLMChain(llm=llm, prompt=prompt)

output = chain.run(user_input)
print(output)
