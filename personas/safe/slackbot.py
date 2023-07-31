import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain import PromptTemplate

from domain.pinecone_integration.safe_reference_pinecone_client import PineconeClient

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SAFE_SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SAFE_SLACK_APP_TOKEN"]
OPENAI_API_KEY = os.environ["CPRIME_OPENAI_API_KEY"]

# Initializes app with your bot token
app = App(token=SLACK_BOT_TOKEN)

# Store documents and embeddings in the pinecone vectorstore.
vectorstore = PineconeClient.vectorstore()


# completion llm
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.0
)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Human Question: {question}
Your Helpful Answer:"""

qa_prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

# memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# keyword arguements for combine_docs_chain
combine_docs_chain_kwargs = {"prompt": qa_prompt}


# question and answer chain chain
qa = ConversationalRetrievalChain.from_llm(
    llm,
    vectorstore.as_retriever(),
    verbose=True,
    memory=memory,
    combine_docs_chain_kwargs=combine_docs_chain_kwargs,
)


# Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    query = message["text"]
    say(qa.run(query))


# Start app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
