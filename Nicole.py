from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

nicole_chatbot = ChatBot(
    name='Nicole',
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation"
    ]
)

nicole_chatbot.set_trainer(ChatterBotCorpusTrainer)

nicole_chatbot.train(
   "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)


#method trainer
#Allows a chat bot to be trained using a list of strings
#where the list represents a conversation.
#nicole face
file = open('nicoleface.txt','r')
if file.mode == 'r':
    contents = file.read()
    print(contents)

file.close()

print('Hi dear, i´m alive...')
# The following loop will execute each time the user enters input
while True:
    try:
        nicole_response = nicole_chatbot.get_response(input())
        print(nicole_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break