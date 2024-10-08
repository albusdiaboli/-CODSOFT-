def chatbot_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    
    elif "help" in user_input or "what can you do" in user_input:
        return "I can chat with you, tell the weather, or do simple math operations!"
    
   
    elif "weather" in user_input:
        return "I'm not connected to the internet, so I can't tell the weather right now!"
    
    
    elif "add" in user_input:
        try:
           
            numbers = [int(word) for word in user_input.split() if word.isdigit()]
            return f"The result is {sum(numbers)}"
        except:
            return "I couldn't understand the numbers. Please try again!"
    
  
    else:
        return "I'm sorry, I don't understand that yet. Can you ask something else?"


user_input = input("You: ")
print("Bot:", chatbot_response(user_input))