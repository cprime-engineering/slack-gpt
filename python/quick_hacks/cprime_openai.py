import os
import openai


openai_api_key = os.environ.get("CPRIME_OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    api_key=openai_api_key,
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.",
        },
        {"role": "user", "content": "Can you describe what the company Cprime does?"},
    ],
)
print(completion)
