# Define the FAQ data
faq_data = {
    "What are your hours of operation?": "Our hours of operation are Monday to Friday, 9 AM to 5 PM.",
    "Where are you located?": "We are located at 123 Main Street, Springfield.",
    "How can I contact support?": "You can contact support via email at support@example.com or call us at (555) 123-4567.",
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase with a receipt.",
    "Do you offer international shipping?": "Yes, we offer international shipping. Please check our shipping policy for more details."
}

def get_faq_response(question):
    """
    Function to get a response from the FAQ data.
    """
    return faq_data.get(question, "Sorry, I don't have an answer for that question.")

def chatbot():
    """
    Simple chatbot function that runs in a loop to interact with the user.
    """
    print("Hello! I'm your FAQ chatbot. How can I assist you today? (Type 'exit' to end the chat)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = get_faq_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()
