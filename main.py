from ai_engine import ask_ai
from code_loader import load_code

print("Loading project code...")
code_context = load_code()
print("Code loaded successfully.\n")

while True:
    user_input = input("Ask something (or type exit): ")

    if user_input.lower() == "exit":
        break

    answer = ask_ai(user_input, code_context)
    print("\nAI:", answer)
    print("-" * 50)
