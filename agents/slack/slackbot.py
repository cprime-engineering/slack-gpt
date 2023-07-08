import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, LLMChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from prompt_templates import default_template
from prompt_templates import personalized_template
from slack_functions import get_username_from_message

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)

# LLMChain to handle conversations
chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0), 
    prompt=default_template(), 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=2),
)

#Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    human_name = get_username_from_message(message)
    chatgpt_chain.prompt = personalized_template(human_name=human_name)
    output = chatgpt_chain.predict(human_input = message['text'])   
    say(output)

# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()