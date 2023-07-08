import os
from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import (ConversationBufferMemory, 
                                                  ConversationSummaryMemory, 
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)


#Langchain implementation
template = """Assistant is a large language model trained by OpenAI.

    Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

    Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

    Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

    The name of the human you are talking to is {human_name}. When you first greet the human say their name.

    {{history}}
    Human: {{human_input}}
    Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template.format(human_name="unknown")
)

chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=2),
)

#Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)

    user_id = message["user"]
    user = client.users_info(user=user_id)
    human_name = user["user"]["profile"]["display_name_normalized"]

    custom_template = template.format(human_name=human_name)

    chatgpt_chain.prompt = PromptTemplate(input_variables=["history", "human_input"], template=custom_template)

    


    output = chatgpt_chain.predict(human_input = message['text'])   
    say(output)



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()