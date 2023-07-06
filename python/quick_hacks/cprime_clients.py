import os
import json

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

client_information = {
   "cprime_customers":[
      {
         "name":"Willy Wonker's Chocolate Factory",
         "total_value_invoices_2023":"1,000,000",
         "currency":"GBP"
      },
      {
         "name":"Monsters INC",
         "total_value_invoices_2023":"500,000",
         "currency":"GBP"
      }
   ]
}

openai_api_key = os.environ.get("CPRIME_OPENAI_API_KEY")

prompt = PromptTemplate(
    input_variables=["client_information"],
    template=" Who are Cprime's biggest clients? You may use this JSON data in forming your response {client_information}",
)

llm = OpenAI(openai_api_key=openai_api_key,temperature=0)

chain = LLMChain(llm=llm, prompt=prompt)

output = chain.run(json.dumps(client_information))

print(output)
