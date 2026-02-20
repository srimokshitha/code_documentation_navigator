import os

def load_code_from_folder(folder_path):
    all_code = ""

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        all_code += f"\n\n# File: {file}\n"
                        all_code += f.read()
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    return all_code
