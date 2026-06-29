def get_retriever(vectorestore):
    retriever = vectorestore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return retriever