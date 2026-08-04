import tiktoken

class Tokenizer:
    def __init__(self,model_name="gpt-4.1-mini"):
        self.encoding = tiktoken.encoding_for_model(model_name)

    def encode(self, text):
        return self.encoding.encode(text)
    def decode(self, tokens):
        return self.encoding.decode(tokens)

    def count_tokens(self, text):
        return len(self.encode(text))

    def compare(self,text):
        return {
            "characters": len(text),
            "words": len(text.split()),
            "tokens": self.count_tokens(text)
        }
    def estimated_cost(self,text,price_per_million_tokens):
        return ((self.count_tokens(text) / 1000000) * price_per_million_tokens)