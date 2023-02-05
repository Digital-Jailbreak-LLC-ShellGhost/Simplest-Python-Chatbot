# Import necessary libraries
import re

# Define a default greeting
greeting = "Hello! How can I help you today?"

# Define responses
responses = {
    "hi": "Hi there!",
    "how are you": "I'm doing well, thanks for asking!",
    "bye": "Goodbye!",
    "default": "I'm sorry, I don't understand."
}

# Define a function to handle user input and generate a response
def chatbot_response(message):
    # Pre-process the message to remove any special characters
    message = re.sub(r'[^\w\s]', '', message).lower()
    
    # Check if the message matches any of the defined responses
    if message in responses:
        return responses[message]
    else:
        # Return the default response if no match is found
        return responses["default"]

# Start the conversation
print(greeting)

# Loop to continue the conversation
while True:
    # Get user input
    message = input("You: ")
    
    # Exit the loop if the user says "bye"
    if message == "bye":
        print("Chatbot: Goodbye!")
        break
    
    # Generate a response and print it
    response = chatbot_response(message)
    print("Chatbot: " + response)
