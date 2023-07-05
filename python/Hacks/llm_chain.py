# documentation: https://python.langchain.com/docs/modules/chains/
# requires environment variable "OPENAI_API_KEY"

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Step 1: Import the necessary modules
import os


# Step 2: Get user input
user_input = input("Enter a concept: ")

# Step 3: Define the Prompt Template
prompt = PromptTemplate(
    input_variables=["concept"],
    template="Define {concept} with a real-world example?",
)

# Step 4: Print the Prompt Template
print(prompt.format(concept=user_input))

# Step 5: Instantiate the LLMChain
llm = OpenAI(temperature=0.9)
chain = LLMChain(llm=llm, prompt=prompt)

# Step 6: Run the LLMChain
output = chain.run(user_input)
print(output)
