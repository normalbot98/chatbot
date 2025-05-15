def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you?"
    elif "your name" in user_input:
        return "I'm your friendly chatbot."
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great!"
    else:
        return "Sorry, I didn't understand that."