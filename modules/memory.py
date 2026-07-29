class Memory:
    def __init__(self, SYSTEM_PROMPT=None):
        self.conversation = [SYSTEM_PROMPT]
    def add_user_message(self, user_input):
        self.conversation.append(
            {
                "role": "user",
                "content": user_input
            }
        )
    def add_assistant_message(self, assistant_response):
        self.conversation.append(
            {
                "role": "assistant",
                "content": assistant_response
            }
        )

    def get_messages(self):
        return self.conversation
    