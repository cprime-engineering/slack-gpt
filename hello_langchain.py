from langchain.llms import OpenAI
llm=OpenAI(model_name="text-davinci-003")
llm("Explain machine learning in one paragraph")