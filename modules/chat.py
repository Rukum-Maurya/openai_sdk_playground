from openai import OpenAI


class Chat:
    def __init__(self, client: OpenAI):
        self.client = client

    def generate(self, messages):


        with self.client.responses.stream(
            model="gpt-4.1-mini",
            input=messages
        ) as stream:

            assistant_response = ""
            print("=="*50)
            print("Final Response: ")
            for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="", flush=True)
                    assistant_response += event.delta

            print()

        return assistant_response