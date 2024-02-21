import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['hi|hey|hello', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you!', 'I\'m good, how about you?']],
    ['what is your name?', ['I am a chatbot.', 'You can call me a chatbot.']],
    ['what can you do?', ['I can assist you with various tasks, ask me anything!']],
    ['tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 'What do you get when you cross a snowman and a vampire? Frostbite!']],
    ['quit', ['Bye, take care!', 'Goodbye!']]
]

# Create chatbot
def chatbot():
    print("Hi, I'm a chatbot! How can I help you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye, take care!")
            break
        else:
            response = chat.respond(user_input)
            print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()

