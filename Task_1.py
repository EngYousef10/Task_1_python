def chat_bot():
    user_name = None
    knowledge_base = {
        "hello": "Hello! How can I help you?",
        "hi": "Hi there!",
        "how are you": "I'm just a program, but thanks for asking!",
        "what's your name": "I'm a simple chat bot.",
        "goodbye": "Goodbye! Have a great day!",
        "bye": "See you later!"
    }
    
    math_operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    
    print("Welcome to the Chat Bot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'exit':
            print("Chat Bot: Goodbye!")
            break
        
        # Save name if this is the first time
        if user_name is None and ("my name is" in user_input or "i am" in user_input):
            if "my name is" in user_input:
                user_name = user_input.split("my name is")[1].strip()
            else:
                user_name = user_input.split("i am")[1].strip()
            print(f"Chat Bot: Nice to meet you, {user_name}!")
            continue
        
        # Check for mathematical operations
        math_found = False
        for op in math_operations:
            if op in user_input:
                try:
                    # Extract numbers from input
                    numbers = [int(s) for s in user_input.split() if s.isdigit()]
                    if len(numbers) >= 2:
                        result = math_operations[op](numbers[0], numbers[1])
                        print(f"Chat Bot: The result is {result}")
                        math_found = True
                        break
                except:
                    print("Chat Bot: I couldn't understand that math operation.")
                    math_found = True
                    break
        
        if math_found:
            continue
        
        # Check knowledge base
        response_found = False
        for question in knowledge_base:
            if question in user_input:
                print(f"Chat Bot: {knowledge_base[question]}")
                response_found = True
                break
        
        if not response_found:
            print("Chat Bot: I'm not sure how to respond to that. Can you ask something else?")

# Run the chat bot
chat_bot()