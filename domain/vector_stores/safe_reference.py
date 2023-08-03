from domain.vector_stores.pinecone_client import PineconeClient

class SafeReference(PineconeClient):
   
    def vectorstore(self):
        return self.pincone_vectorstore(index_name="safe-reference")
