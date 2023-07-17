import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, LLMChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.embeddings.openai import OpenAIEmbeddings

from agents.ada.prompt_generator import default_template
from agents.ada.prompt_generator import personalized_template
from slack_functions import get_username_from_message

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
OPEN_API_KEY = os.environ["CPRIME_OPENAI_API_KEY"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)

# Text embedding model name
model_name = 'text-embedding-ada-002'

# Embedding model used for retrieval augmentation
embed = OpenAIEmbeddings(
document_model_name=model_name,
query_model_name=model_name,
openai_api_key=OPEN_API_KEY
)

# LLMChain to handle conversations
chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=default_template(),
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)


# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    human_name = get_username_from_message(message)
    chatgpt_chain.prompt = personalized_template(human_name=human_name)
    output = chatgpt_chain.predict(human_input=message["text"])
    say(output)


# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
