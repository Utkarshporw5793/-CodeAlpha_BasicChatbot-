def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm running smoothly 😄"
    elif "your name" in user_input:
        return "I'm your smart Python chatbot!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "Utkarsh" in user_input:
        return "Utkarsh is awesome! 🌸"
    else:
        return "I'm not sure how to respond to that yet..."

# Simple command-line chat interface
print("🤖 SmartBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 SmartBot: Bye! Take care.")
        break

    response = get_response(user_input)
    print("🤖 SmartBot:", response)
