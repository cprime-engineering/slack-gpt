import openai

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible."},
{"role": "user", "content" : "Can you describe what the company Cprime does?"}]
)
print(completion)