import pyttsx3

print("WELLCOME TO KARTHIK TEXT TO SPEECH")
text = input("enter your text:")
engine = pyttsx3.init()
engine.setProperty('rate',130)
engine.say(text)
engine.runAndWait()


