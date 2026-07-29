
from config import client
from modules.prompts import SYSTEM_PROMPT
from modules.memory import Memory


def chat():
    
    
    memory = Memory(SYSTEM_PROMPT)
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            print(memory.get_messages())
            break
        
        memory.add_user_message(user_input)
        with client.responses.stream(
            model="gpt-4.1-mini",
            input=memory.get_messages()
        ) as stream:
            
            assistant_response = ""
            print("Assistant: ", end="")
            for event in stream:
                if event.type == "response.output_text.delta":
                    
                    print(event.delta, end="", flush=True)
                    assistant_response += event.delta
            
            print()
            memory.add_assistant_message(assistant_response)
