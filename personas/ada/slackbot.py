import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, LLMChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from domain.prompt_engineering.prompt_generator import PromptGenerator
from domain.slack_integration.web_client import WebClient
from domain.pinecone_integration.pinecone_client import PineconeClient

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["ADA_SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["ADA_SLACK_APP_TOKEN"]
OPEN_API_KEY = os.environ["CPRIME_OPENAI_API_KEY"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)

# Persona version number
persona_version_number = "v0.0.0"

# Path to pre prompt templates
pre_prompt_templates_path = "personas/ada/pre_prompts/"


# LLMChain to handle conversations
chatgpt_chain = LLMChain(
    llm=OpenAI(openai_api_key=OPEN_API_KEY, temperature=0),
    prompt=PromptGenerator(
        pre_prompt_templates_path=pre_prompt_templates_path
    ).default_template(),
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)

# Store documents and embeddings in the pinecone vectorstore.
vectorstore = PineconeClient.vectorstore()


# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    human_name = WebClient().get_username_from_message(message)
    chatgpt_chain.prompt = PromptGenerator(
        pre_prompt_templates_path=pre_prompt_templates_path
    ).personalized_template(
        human_name=human_name, version_number=persona_version_number
    )
    output = chatgpt_chain.predict(human_input=message["text"])
    say(output)


# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
