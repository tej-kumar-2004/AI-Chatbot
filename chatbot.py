# Task - 01: AI Chatbot

print("================================")
print("       AI CHATBOT")
print("================================")
print("Hello! I am your AI Chatbot.")
print("Type 'bye' to exit.\n")

def chatbot_response(user_message):
    message = user_message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii"]:
        return "Hello! How can I help you?"

    # Name
    elif "your name" in message or "who are you" in message:
        return "I am a simple AI chatbot created using Python."

    # How are you
    elif "how are you" in message:
        return "I am doing great! Thanks for asking."

    # Python
    elif "python" in message:
        return "Python is a popular programming language used in AI, ML and web development."

    # AI
    elif "what is ai" in message or "artificial intelligence" in message:
        return "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence."

    # NLP
    elif "nlp" in message or "natural language processing" in message:
        return "NLP stands for Natural Language Processing. It helps computers understand and process human language."

    # Help
    elif "help" in message:
        return "Sure! You can ask me about AI, Python, NLP, or general questions."

    # Thanks
    elif "thank you" in message or "thanks" in message:
        return "You're welcome!"

    # Exit
    elif message in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day!"

    # Unknown question
    else:
        return "Sorry, I don't understand that question. Please try another question."


# Chat loop
while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        break