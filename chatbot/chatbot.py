print("====================================")
print("       PLAIN CHATBOT")
print("====================================")

print()
print("This chatbot does not have access to")
print("the student's private study data.")
print()

question = input("You: ")

print()
print("Chatbot:")

if "study" in question.lower() or "next" in question.lower():
    print("I can give general study advice, but I cannot")
    print("directly access your private study data.")
    print("Please provide your study information if you")
    print("want a personalized recommendation.")
else:
    print("I can provide general study-related information.")
