import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, LLMChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from domain.prompt_engineering.prompt_generator import PromptGenerator
from domain.slack_integration.web_client import WebClient
from domain.pinecone_integration.pinecone_client import PineconeClient

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["ADA_SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["ADA_SLACK_APP_TOKEN"]
OPENAI_API_KEY = os.environ["CPRIME_OPENAI_API_KEY"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)


# Store documents and embeddings in the pinecone vectorstore.
vectorstore = PineconeClient.vectorstore()

# completion llm
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

# retrieval qa to instruct our completion llm to base answer on the information returned from our vector store
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)


# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    query = message["text"]
    say(qa.run(query))


# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
