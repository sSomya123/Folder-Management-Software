from nltk.chat.util import Chat, reflections
from Methods import create_folder, delete_folder, copy_folder, move_folder

# Predefined folder shortcuts
folders = {
    "doc": "C:/Users/techn/Documents",
    "desktop": "C:/Users/techn/Desktop",
    "video": "C:/Users/techn/Videos",
    "pic": "C:/Users/techn/Pictures",
    "music": "C:/Users/techn/Music"
}

def resolve_path(path):
    """Resolve shortcut names to actual paths, if applicable."""
    return folders.get(path.lower(), path)

# Define chatbot command patterns
pairs = [
    [r"create folder (.+) in (.+)", lambda matches: create_folder(matches[1], matches[0])],
    [r"delete folder (.+)", lambda matches: delete_folder(matches[0])],
    [r"copy folder (.+) to (.+)", lambda matches: copy_folder(matches[0], matches[1])],
    [r"move folder (.+) to (.+)", lambda matches: move_folder(matches[0], matches[1])],
    [r"quit", ["Goodbye! Have a great day!"]],
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I am your folder management chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
