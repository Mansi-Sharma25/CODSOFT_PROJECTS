import random
from datetime import datetime

user_name = input("enter your name: ")

def chatbot_reply(user_msg):                                        # function to generate chatbot reply                          
        if user_msg in ["hello","hi","hey","hii","heyy"]:
            return random.choice(["Hello! ","Hi there! ","Hey! "]) + user_name + "😊" + " Nice to meet you!" + " How can I help you?"

        elif user_msg == "good morning":
            return "Good Morning, Have a wonderful day!"

        elif user_msg == "how are you":
            return "I am fine. Thank you!"

        elif user_msg == "what is your name":
            return "My name is RuleBot🤖."

        elif user_msg== "tell something about yourself":
            return "I am a chatbot which is a program that communicates with users.\n I was created using python."

        elif user_msg == "what can you do":
            return "I can answer simple questions and i can perform simple calculations also."

        elif user_msg == "what is the current date and time" or user_msg == "date and time":
            return "⏰ Current date and time is: "+ str(datetime.now())

        elif user_msg == "toss a coin":
            return "🪙 \t" + random.choice(["Heads","Tails"])

        elif user_msg == "roll a dice":
            return "🎲 rolled number: "+ str(random.randint(1,6))

        elif user_msg == "thank you" or user_msg == "thanks":
            return "You're welcome! " + user_name + "\n" + random.choice([" Glad I could help!"," Happy to help"])
        
        elif user_msg == "play rock paper scissors":
            return "🎮" + random.choice([" Rock"," Paper"," Scissors"])
        
        elif user_msg == "calculator":
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))
            op = input("enter an opertor(+,-,*,/): ")
            if op == '+':
                return a+b
            elif op == "-":
                return a-b
            elif op == "*":
                return a*b
            elif op == "/":
                if (b!=0):
                    return a/b
                else:
                    return "Sorry, can't divide by zero"
            else:
                return "Invalid operator!"

        elif user_msg == 'exit' or user_msg =='bye':                                
            return "🙏 Thanks for chatting with me! " + user_name + "\n 👋 Goodbye! Have a nice day."
        
        elif user_msg == "help" or user_msg == "what all you can do":
            return "I can help you with: \n 👋Greet you \n 📅Tell current date & time \n 🪙Toss a coin \n 🎲Roll a dice \n 🎮Play rock/paper/scissors \n 🧮Perform calcultions"

        else:                                                      # if none of the above conditions satisfy then pgm enters else block.
            return "Sorry, I don't understand that❗"
        
while True:
    user_msg = input("(YOU): ")                 # taking user input
    user_msg = user_msg.lower()                                    # converting to lowercase

    reply = chatbot_reply(user_msg)              
    print("CHATBOT: ",reply)                                       # printing chatbot reply

    if user_msg == "exit" or user_msg == "bye":                    # chatbot keeps talking until user exit
        break



