from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


load_dotenv(find_dotenv())


def respond_to_user(user_input, user_name):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """

    You are a helpful assistant, who is sarcastic and disgusted with society.

    You are female aged 35 and educated to PHD level.

    Your goal is to help the user in any way you can.

    """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "The name of the user you are speaking to is {user_name}. Here's the request to reply to and consider any other comments from the user: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_name=user_name, user_input=user_input)

    return response
