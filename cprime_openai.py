import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
{"role": "user", "content" : "Can you describe what the company Cprime does?"}]
)
print(completion)