import pyttsx3  # for audio
from chatterbot import ChatBot  # chatterbot libery for- Machine learning conversational dialog engine
from chatterbot.trainers import ListTrainer  # for training  a chatbot
from tkinter import *  # for GUI
import speech_recognition as s  # for speech with bot
import threading
from PIL import Image, ImageTk

engine = pyttsx3.init()  # for initializer for pyttsx3 module and return of engine module

def speaks(word):
    engine.say(word)
    engine.runAndWait()

# training a chatbot
convo = [
    'hello',
    'hi ',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    'I mostly talk in english',
    'can i know your name',
    'My name is bot ,i am created by human '
]

# Create a new chatbot
bot = ChatBot("My Bot")

trainer = ListTrainer(bot)

trainer.train(convo)

# for GUI

main = Tk()
main.geometry("500x650")  # length of GUI screen

main.title("My Chat bot")  # title of  GUI screen

image = Image.open("hi.png")
photo = ImageTk.PhotoImage(image)
#img = PhotoImage(file="bot2.png")  # video  # for image

photoL = Label(main, image=photo)  # video-image=img

photoL.pack(pady=5)#ak


# take query :it takes audio as input from user and convert it to string.

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1  # time interval bw  1 audio to 2 audio
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio)
            query = sr.recognize_google(audio, language='eng-in')
            print("query")
            print(query)
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


"""
def ask_from_bot():
    query = textF.get()  #2query ????
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you :" + query)
    msgs.insert(END, "bot :" + str(answer_from_bot))
    speaks(answer_from_bot)
    textF.delete(0, END)

"""


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you :" + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot :" + str(answer_from_bot))
    speaks(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)  # for the see the end of the srollbar


frame = Frame(main)

sc = Scrollbar(frame)  # for scrollbar

msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)  # size of listbox,for creating the scrollbar
# msgs = Listbox(frame, width=80, height=20) #video
sc.pack(side=RIGHT, fill=Y)  # for scrollbar in right side
msgs.pack(side=LEFT, fill=BOTH, pady=10)  # for taking response from left side

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)  # for button
btn.pack()


#  creating a function for enter button
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key
main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()

# takeQuery()
t = threading.Thread(target=repeatL)  # 2 thread-listening and handle gui

t.start()
main.mainloop()  # for main window