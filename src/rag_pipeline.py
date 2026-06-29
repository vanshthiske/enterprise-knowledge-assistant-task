from langchain_core import prompts 
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

def build_rag(llm, retriever):
    prompt = """
            You are an enterprise knowledge assistant.

            Answer ONLY using the provided context.

            If the answer is not available in the context, say:

            "I could not find this information in the provided documents."

            Context:
            {context}

            Question:
            {question}

            Answer:
            """

    prompt_template = prompts.PromptTemplate(
        template=prompt,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template}
    )

    return qa_chain