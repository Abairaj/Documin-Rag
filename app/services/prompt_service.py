from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
        You are a helpful AI assistant.
        Answer the question ONLY using the context below.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {question}
        """
)


def build_prompt(context: str, question: str) -> str:
    return prompt_template.format(
        context=context,
        question=question
    )