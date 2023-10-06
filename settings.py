import pyttsx3 as p
engine = p.init()
voiceEngine=p.init()

def setVolume(volumeLevel):
    newVolume = float(volumeLevel)
    while newVolume <= float(volumeLevel):
        voiceEngine.setProperty('volume', newVolume)
        newVolume = newVolume+0.3

def rateOfSpeed(speed):
    voiceEngine.setProperty('rate', speed)            
    speed +=1

def chooseVoice(voiceNumber):
    voices=engine.getProperty("voices")
    print("ok")
    engine.setProperty("voice",voices[voiceNumber].id)
    n=engine.getProperty("voice")
    print(n)