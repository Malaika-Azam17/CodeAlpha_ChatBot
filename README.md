Chatbot Project Description

This chatbot project is a simple, rule-based system designed to handle basic greetings and common questions. The following is an overview of the different components and functionalities of the chatbot.

Components
Greeting Responses:

The chatbot can recognize and respond to common greetings such as "hello", "hi", "greetings", "sup", "what's up", and "hey".
Responses are chosen randomly from a predefined list to make interactions feel more dynamic.

Common Questions and Answers:

The chatbot has a predefined set of questions and answers. These cover a range of topics, including personal inquiries about the chatbot, general knowledge questions, and common programming-related queries.

Text Processing:

The chatbot uses the Natural Language Toolkit (nltk) to tokenize and lemmatize user input. This ensures that the input is normalized for better matching with predefined responses.
Punctuation is removed from user input to facilitate more accurate matching with the predefined questions.

Response Generation:

The chatbot first checks if the user input is a greeting and responds appropriately if it is.
If the input is not a greeting, the chatbot checks if it matches any of the predefined common questions. If a match is found, it responds with the corresponding answer.
If the input doesn't match any of the predefined questions, the chatbot responds with a default message indicating that it doesn't understand the input.

Menu System:

After each response, the chatbot displays a menu allowing the user to continue chatting or exit the conversation.
The menu ensures that the user can gracefully end the conversation if desired.

Usage

To start a conversation with the chatbot, run the script. The chatbot will greet you and prompt you to enter your message. You can continue chatting by selecting the appropriate option from the menu or exit the conversation by typing 'exit', 'quit', or 'bye'.
This chatbot project demonstrates basic natural language processing and rule-based response generation, making it a simple yet effective virtual assistant for answering predefined questions.
