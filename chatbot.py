import nltk
import random
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure that necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('wordnet')

# Greeting responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "hello", "I am glad you're talking to me!", "Hello! How can I assist you today?"]

# Basic Questions

COMMON_QUESTIONS = {
    "how are you": ["I'm a chatbot, but I'm functioning as expected!", "I'm here to assist you!"],
    "what is your name": ["I am Chatbot, your virtual assistant.", "You can call me Chatbot."],
    "what can you do": ["I can have basic conversations with you, answer some questions, and more."],
    "who created you": ["I was created by an AI enthusiast!"],
    "what is the tallest mountain in the world": ["The tallest mountain in the world is Mount Everest."],
    "what is the smallest country in the world": ["The smallest country in the world by area is Vatican City."],
    "who discovered penicillin": ["Penicillin was discovered by Alexander Fleming."],
    "what is the boiling point of water": ["The boiling point of water is 100 degrees Celsius (212 degrees Fahrenheit) at standard atmospheric pressure."],
    "who painted the Mona Lisa": ["The Mona Lisa was painted by Leonardo da Vinci."],
    "what is the chemical symbol for gold": ["The chemical symbol for gold is Au."],
    "what is the longest river in the world": ["The longest river in the world is the Nile River."],
    "what is the currency of japan": ["The currency of Japan is the Japanese Yen (JPY)."],
    "who is the president of the united states": ["As of now, Joe Biden is the President of the United States."],
    "what is the capital of france": ["The capital of France is Paris."],
    "who wrote 'to kill a mockingbird'": ["'To Kill a Mockingbird' was written by Harper Lee."],
    "what is the largest planet in our solar system": ["The largest planet in our solar system is Jupiter."],
    "what is the speed of light": ["The speed of light in a vacuum is approximately 299,792 kilometers per second (km/s)."],
    "what is python": ["Python is a high-level, interpreted programming language known for its readability and versatility."],
    "what is machine learning": ["Machine learning is a subset of artificial intelligence that involves training algorithms to learn from data and make predictions."],
    "what is a variable": ["A variable is a named storage location in a program that holds a value which can be modified during program execution."],
    "what is a function": ["A function is a reusable block of code that performs a specific task and can be called with different inputs."],
    "what is object-oriented programming": ["Object-oriented programming (OOP) is a paradigm based on the concept of objects, which can contain data and methods."]
}

def greeting(sentence):
    """If the user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def common_response(sentence):
    """If the user's input matches a common question, return the corresponding response"""
    sentence = sentence.lower()  # Ensure lowercase for comparison
    sentence = remove_punctuation(sentence)
    tokens = word_tokenize(sentence)
    
    for question in COMMON_QUESTIONS:
        question_cleaned = remove_punctuation(question.lower())
        question_tokens = word_tokenize(question_cleaned)
        
        # Check if the user's input contains all tokens from the question
        if all(token in tokens for token in question_tokens):
            return random.choice(COMMON_QUESTIONS[question])
    
    return None

def remove_punctuation(text):
    """Remove punctuation from the text"""
    return text.translate(str.maketrans('', '', string.punctuation))

lemmatizer = WordNetLemmatizer()
def lemmatize_sentence(sentence):
    """Lemmatize the words in the sentence"""
    words = word_tokenize(sentence)
    lemmatized_sentence = ' '.join([lemmatizer.lemmatize(word) for word in words])
    return lemmatized_sentence

def chatbot_response(user_input):
    """Generate a response to the user's input"""
    user_input = remove_punctuation(user_input)
    user_input = lemmatize_sentence(user_input.lower())

    # Debugging output
    print(f"Processed user input: {user_input}")

    # Check for greetings
    response = greeting(user_input)
    if response is not None:
        return response

    # Check for common questions
    response = common_response(user_input)
    if response is not None:
        return response

    # Default response
    response = "I'm sorry, I don't understand that. Can you please rephrase?"
    return response

def display_menu():
    """Display the chatbot menu"""
    print("\nMenu:")
    print("1. Continue chatting")
    print("0. Exit")

def get_valid_menu_choice():
    """Get a valid menu choice from the user"""
    while True:
        choice = input("Enter your choice (0-1): ")
        if choice in ['0', '1']:
            return choice
        else:
            print("Invalid choice. Please enter 0 or 1.")

def chatbot():
    """Main chatbot function"""
    print("Chatbot: Hello! I am your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        display_menu()
        choice = get_valid_menu_choice()
        if choice == '0':
            print("Chatbot: Goodbye! Have a great day!")
            break

if __name__ == "__main__":
    chatbot()
