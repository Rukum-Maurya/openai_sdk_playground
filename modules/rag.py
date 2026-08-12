class RAG:
    def __init__(self, search, reranker, chat, memory, prompt_builder):
        self.search = search
        self.reranker = reranker
        self.chat = chat
        self.memory = memory
        self.prompt_builder = prompt_builder

    


    def generate_response(self, query, candidate_k=10,final_k=3):

        # Step 1: Retrieve candidate  documents
        search_results = self.search.search(
            query,
            candidate_k
        )
        
        # 2. Rerank Candidates
        reranked_result = self.reranker.rerank(
            query,
            search_results
        )

        # 3. Keep only the best documents
        final_results = reranked_result[:final_k]

        print("\n===== FINAL CONTEXT =====")

        for i, (doc, score) in enumerate(final_results, 1):
            print(f"\nDocument {i}")
            print(f"Reranker score: {score}")
            print(doc)

        print("\n=========================\n")

        # 4. Build RAG context
        context = "\n\n".join(
            f"Document: {doc}"
            for doc, _ in final_results
        )

        # 5. Get  conversation messages
        memory_messages = self.memory.get_messages()



        # 6. Build final LLM messages
        messages = self.prompt_builder.build(
            query=query,
            context=context,
            memory=memory_messages
        )

        print(f"Final Prompt : {messages}")

        # 7. Generate response from the LLM
        assistant_response = self.chat.generate(messages)

        # Step 6: Update memory with the new messages
        self.memory.add_user_message(query)
        self.memory.add_assistant_message(assistant_response)

        return assistant_response