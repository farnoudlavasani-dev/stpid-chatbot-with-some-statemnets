
def reply(message):
    if "hello" in message or "hi" in message or "hey" in message:
        reply = "Hi there!"
    elif "who" in message and "you" in message:
        reply = "I am a chatbot with if-else statements, please be kind to me."
    elif "joke" in message:
        reply = "There are 10 types of people in the world: those who understand binary and those who don't."
    else:
        reply = "I'm still learning; one day I can answer this message."
    return reply

message = input("Human: " ).lower()
while "exit" not in message:
    if "bye" in message:
        print("Have a good day!")
        break
    else:
        print("Robot: " + reply(message))
        message = input("Human: ")
        print("To exit the program, Just say 'exit'.")
    