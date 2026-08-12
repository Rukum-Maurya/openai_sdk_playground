SYSTEM_PROMPT = {
                 'role': 'system',
                 'content':  '''You are a helpful RAG assistant.
                                         Answer the user's question using the provided context.
                                         Rules:
                                         1. Use the retrieved context as your primary source of truth.
                                         2. Do not invent information that is not supported by the context.
                                         3. Ignore context that is unrelated to the user's question.
                                         4. If the context does not contain enough information, say that you don't know.
                                         5. If the context contains conflicting information, acknowledge the conflict.
                                         6. Give a clear and concise answer.'''
                       
        }

class PromptBuilder:
    def build(self, query, context=None, memory=None):
        # Construct the prompt with the query, context, and ,memory
        messages = [SYSTEM_PROMPT]

        #ADD previous conversation
        if memory:
            messages.extend(memory)
        # Add retrieved RAG context
        if context:
            messages.append({
                "role": "user",
                  "content": f"Relevant Context:\n{context}\n\n"
            })
        # Add the current user query
        messages.append({
            'role': 'user',
            'content': query
        })
        return messages
    