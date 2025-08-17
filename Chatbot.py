# Simple rule-based chatbot using dictionary

# Define questions and answers
qa_pairs = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm just a bot, but I'm doing fine. How about you?",
    "i am fine":"ohh great! so aks me something..",
    "what is your name": "I am a simple chatbot created in Python.",
    "bye": "Goodbye! Have a nice day!",
    "exit": "Exiting... Bye!"
}

def get_response(user_input):
    user_input = user_input.lower()
    return qa_pairs.get(user_input, "Sorry, I don't understand that.")

# Chat loop
print("ChatBot: Type something to start chatting (type 'exit' to stop)\n")
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("ChatBot:", response)
    if user_input.lower() == "exit":
        break
