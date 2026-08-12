from openai import OpenAI
from modules.embedding import Embedding

class Search:
    def __init__(self,client:OpenAI):
        self.client = client
        self.embedding = Embedding(client)
        self.documents = []  # List to store documents and their embeddings
        self.document_embeddings = []  # List to store embeddings of the documents

    def index_documents(self, documents):

        self.documents = documents  # Reset the documents list
        self.document_embeddings = []  # Reset the document embeddings list

        for doc in documents:
             embedded_vector = self.embedding.generate_embedding(doc)
             self.document_embeddings.append(embedded_vector)

    def search(self, query,top_k):
        query_embedding = self.embedding.generate_embedding(query)
        print(f"Query: {query}")
        print(f"Query embedding length: {len(query_embedding)}")
        similarities = []
        for document, embedding in zip(self.documents, self.document_embeddings):
            similarity = self.embedding.cosine_similarity(query_embedding,embedding)
            similarities.append((document,similarity))

        similarities.sort(
            key=lambda x : x[1],
            reverse=True
        )

        return similarities[:top_k]
    


        
       
    