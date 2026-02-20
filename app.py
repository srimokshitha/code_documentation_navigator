import streamlit as st
from code_loader import load_code_from_folder
from ai_engine import ask_question, summarize_project

st.set_page_config(page_title="Code Documentation Navigator", page_icon="🚀")

st.title("🚀 Code Documentation Navigator")
st.markdown("### Understand Your Codebase Using AI")
st.markdown("---")

st.info("💡 Ask questions about your project in natural language.")

folder_path = st.text_input("Enter your project folder path:", value="sample_code")

if folder_path:
    with st.spinner("Loading codebase..."):
        codebase = load_code_from_folder(folder_path)

    st.success("Codebase Loaded Successfully!")

    if st.button("📊 Summarize Entire Project"):
        with st.spinner("Generating summary..."):
            summary = summarize_project(codebase)
        st.success(summary)

    st.markdown("---")

    mode = st.radio(
        "Choose explanation mode:",
        ["Normal", "Explain Like I'm 5", "Technical Deep Dive"]
    )

    question = st.text_input("Ask a question about your code:")

    if st.button("Get Answer"):
        if question:
            with st.spinner("Analyzing code..."):
                answer = ask_question(codebase, question, mode)
            st.markdown("### 🤖 AI Response")
            st.write(answer)
        else:
            st.warning("Please enter a question.")
