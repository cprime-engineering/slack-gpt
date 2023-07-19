import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from domain.pinecone_integration.pinecone_client import PineconeClient

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["ADA_SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["ADA_SLACK_APP_TOKEN"]
OPENAI_API_KEY = os.environ["CPRIME_OPENAI_API_KEY"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)

# Store documents and embeddings in the pinecone vectorstore.
vectorstore = PineconeClient.vectorstore()

# Conversational buffer memory to handle chat history.
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Conversational retrieval qa to instruct our completion llm to base answer on the information returned from our vector store
qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vectorstore.as_retriever(), memory=memory, verbose=True)


# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    query = message["text"]
    say(qa.run(query))


# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
