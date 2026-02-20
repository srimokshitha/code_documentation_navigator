Code Documentation Navigator



Overview

\- AI-powered tool that analyses and explains entire codebases.

\- Built using Streamlit for UI and Ollama (local LLM) for AI processing.

\- Designed to help developers and students understand unfamiliar projects quickly.



Problem

\- Understanding a new codebase takes time.

\- Reading multiple files manually is inefficient.

\- Beginners struggle to interpret complex functions and project structure.



Solution

\- Load any local project folder.

\- Automatically summarise the entire project.

\- Ask questions about the codebase in natural language.

\- Choose explanation modes based on user needs:

&nbsp; - Normal

&nbsp; - Explain Like I'm 5

&nbsp; - Technical Deep Dive



How It Works

\- The application reads all Python files from the selected folder.

\- The combined codebase is sent to a local LLM via Ollama.

\- The model generates summaries and answers user questions.

\- Streamlit provides an interactive interface for user interaction.



Tech Stack

\- Python

\- Streamlit

\- Ollama

\- LLaMA / Mistral model

\- Git



Project Structure

\- app.py: Streamlit UI logic.

\- ai\_engine.py: Handles communication with Ollama API.

\- code\_loader.py: Loads and combines project files.

\- main.py: Entry-level logic for execution.

\- sample\_code/: Example project for testing.

\- requirements.txt: Project dependencies.



How to Run

1\. Clone the repository:

&nbsp;  git clone https://github.com/srimokshitha/code\_documentation\_navigator.git

&nbsp;  cd code\_documentation\_navigator



2\. Create and activate virtual environment:

&nbsp;  python -m venv venv

&nbsp;  venv\\Scripts\\activate



3\. Install dependencies:

&nbsp;  pip install -r requirements.txt



4\. Ensure Ollama is running:

&nbsp;  ollama run llama3



5\. Start the application:

&nbsp;  streamlit run app.py



Use Cases

\- Understanding open-source repositories.

\- Academic project documentation.

\- Developer onboarding.

\- Code review assistance.



Future Enhancements

\- Automatic README generation.

\- Code dependency visualization.

\- Architecture summary generation.

\- Deployment-ready hosted version.



Author

Sri Mokshitha Barli

GitHub: https://github.com/srimokshitha



