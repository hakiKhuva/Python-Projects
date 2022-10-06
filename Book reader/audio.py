import pyttsx3
book = open("(1) The Hunger Games.txt")
book_text = book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()