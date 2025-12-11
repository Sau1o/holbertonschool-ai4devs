import sys
import os
import argparse

def generate_docs(file_path, extension):
    print(f"Generating docs for: {file_path}")
    if extension == ".java":
        comment = "/**\n * [AI GENERATED JAVADOC]\n * @author Copilot\n */"
    elif extension == ".py":
        comment = '"""\n[AI GENERATED DOCSTRING]\n"""'
    else:
        return

    with open(file_path, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(comment + '\n' + content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--language', required=True)
    args = parser.parse_args()
    generate_docs(args.file, args.language)
