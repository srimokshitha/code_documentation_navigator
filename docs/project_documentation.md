Project Documentation – Code Documentation Navigator



1\. System Architecture



The system consists of three main components:



\- User Interface Layer (Streamlit)

\- Code Processing Layer (code\_loader.py)

\- AI Processing Layer (ai\_engine.py using Ollama)



Workflow:

User selects a folder → 

Code files are loaded and combined → 

Prompt is generated → 

Local LLM processes request → 

Response displayed in UI.



2\. Module Description



app.py

\- Handles Streamlit UI

\- Manages user inputs

\- Controls explanation mode selection

\- Displays summaries and responses



code\_loader.py

\- Traverses selected directory

\- Reads Python files

\- Combines them into a single string

\- Prepares codebase for AI processing



ai\_engine.py

\- Sends prompt to Ollama local API

\- Controls explanation style

\- Handles response formatting



main.py

\- Entry point support file



3\. Explanation Modes



Normal Mode:

\- Balanced explanation.



Explain Like I’m 5:

\- Simplified language.

\- Beginner-friendly explanation.



Technical Deep Dive:

\- Detailed breakdown of functions and logic.

\- More technical vocabulary.



4\. Model Interaction



\- Uses Ollama running locally.

\- Sends prompt using HTTP POST request.

\- Receives response in JSON format.

\- Displays output in Streamlit interface.



5\. Limitations



\- Large projects may take longer to summarize.

\- Performance depends on local hardware.

\- Currently optimized for Python projects.



6\. Future Scope



\- Multi-language support.

\- Automatic documentation generation.

\- Graph-based architecture visualization.

\- Performance optimization for large repositories.



