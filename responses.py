def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "your name" in user_input:
        return "I'm ChatBuddy, your friendly assistant!"
    elif "how are you" in user_input:
        return "I'm doing well, thank you! How can I help you?"
    elif "what can you do" in user_input:
        return "I can answer basic questions and keep you company!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! You can ask me about my name, how I'm doing, or just chat casually!"
    elif "bca" in user_input:
        return "The BCA program is great! Want info about courses or career options?"
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"
    else:
        return "Hmm, I didn’t get that. Try asking something else?"
