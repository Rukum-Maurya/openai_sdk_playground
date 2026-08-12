from openai import OpenAI
import math

class Embedding:
    def __init__(self, client:OpenAI):
        self.client = client

    def generate_embedding(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding

    def dot_product(self, vector1, vector2):
        if len(vector1) != len(vector2):
            raise ValueError("Vectors must be of the same length for dot product.")
        return sum(a * b for a, b in zip(vector1,vector2))

    def magnitude(self , vector):
        return math.sqrt(sum(x ** 2 for x in vector))

    def cosine_similarity(self,vector1, vector2):
        dot_prod = self.dot_product(vector1, vector2)
        magnitude1 = self.magnitude(vector1)
        magnitude2 = self.magnitude(vector2)

        if magnitude1 == 0 or magnitude2 == 0:
            raise ValueError("One or both vectors have zero magnitude, cannot compute cosine similarity.")

        return dot_prod / (magnitude1 * magnitude2)
    