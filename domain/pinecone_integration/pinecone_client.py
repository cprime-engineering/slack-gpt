import os
import pinecone

from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings


class PineconeClient:
    def vectorstore():
        # Set pinecone credentials
        PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
        PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
        OPENAI_API_KEY = os.environ["CPRIME_OPENAI_API_KEY"]

        # initialize pinecone
        pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

        index_name = "savings-accounts"
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore = Pinecone.from_existing_index(index_name, embeddings)

        return vectorstore
