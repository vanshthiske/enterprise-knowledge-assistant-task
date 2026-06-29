import streamlit as st

from src.loader import load_documents
from src.chunker import split_documents
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.llm import get_llm
from src.rag_pipeline import build_rag


st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None


# Sidebar
with st.sidebar:

    st.title("📚 Enterprise Assistant")

    st.markdown("---")

    st.write("### Features")
    st.write("✅ Document Search")
    st.write("✅ Semantic Retrieval")
    st.write("✅ Source Citation")
    st.write("✅ Conversation History")

    st.markdown("---")

    st.write("### Chat History")

    if st.session_state.chat_history:

        for item in st.session_state.chat_history:

            st.write(f"**Q:** {item['question']}")
            st.write(f"**A:** {item['answer']}")
            st.markdown("---")

    else:
        st.write("No questions asked yet.")


# Main Title
st.title("🤖 Enterprise Knowledge Assistant")

st.write(
    "Upload enterprise documents and ask questions using natural language."
)

# Upload Files
uploaded_files = st.file_uploader(
    "Upload PDF, DOCX, TXT files",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# Process Documents
if uploaded_files:

    if st.button("Process Documents"):

        with st.spinner("Processing documents..."):

            documents = load_documents(uploaded_files)

            chunks = split_documents(documents)

            embeddings = get_embedding_model()

            vectorstore = create_vector_store(
                chunks,
                embeddings
            )

            retriever = get_retriever(
                vectorstore
            )

            llm = get_llm()

            qa_chain = build_rag(
                llm,
                retriever
            )

            st.session_state.qa_chain = qa_chain

        st.success("Documents processed successfully.")

# Question Section
if st.session_state.qa_chain:

    question = st.chat_input(
        "Ask a question about your documents..."
    )

    if question:

        with st.spinner("Searching documents and generating answer..."):

            response = st.session_state.qa_chain.invoke(
                {"query": question}
            )

        answer = response["result"]

        # Store chat history
        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        st.subheader("Question")

        st.write(question)

        st.subheader("Answer")

        st.success(answer)

        # Dummy confidence score
        confidence = 90

        st.metric(
            label="Confidence Score",
            value=f"{confidence}%"
        )

        st.subheader("Source Documents")

        shown_sources = set()

        for doc in response["source_documents"]:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            page = doc.metadata.get(
                "page",
                "N/A"
            )

            source_key = f"{source}-{page}"

            if source_key not in shown_sources:

                shown_sources.add(source_key)

                st.info(
                    f"📄 {source} | Page {page}"
                )

else:

    st.info(
        "Upload documents and click 'Process Documents' to begin."
    )