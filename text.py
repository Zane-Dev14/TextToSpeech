import pyttsx3 as p
from app import *
from var import voices,engine
voic=[]
for v in voices:
    voic.append(v.id)
length=len(voic)
def Text(data):
    engine.say(data)
    try:
        engine.runAndWait()
    except:
        engine.endLoop()