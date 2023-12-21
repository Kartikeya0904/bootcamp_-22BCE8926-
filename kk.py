import random

def chatbot():
    print("Hello! I'm your personalized chatbot. What's your name?")
    name = input()
    print(f"Glad to meet you, {name}!")
    
    while True:
        print("How can I help you?")
        user_input = input().lower()

        if "climate" in user_input:
            print("It's cloudy today!")
        elif "score" in user_input:
            print("India 300 for 3 wickets loss")
        elif "jokes" in user_input:
            jokes = ["Always borrow money from pessimist.They'll never except it back"]
            print(random.choice(jokes))
        elif "thankyou" in user_input:
            print("Goodbye!")
            break
        else:
            print("I'm sorry, I didn't understand what you said.")


chatbot()
