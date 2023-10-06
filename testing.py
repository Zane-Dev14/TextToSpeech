# '''	
# import pyttsx3
# voiceEngine = pyttsx3.init()
# rate = voiceEngine.getProperty('rate')
# volume = voiceEngine.getProperty('volume')
# voice = voiceEngine.getProperty('voice')
 
# print (rate)
# print (volume)
# print (voice)
# newVoiceRate = 50
# while newVoiceRate <= 300:
#     voiceEngine.setProperty('rate', newVoiceRate)
#     voiceEngine.say('Testing different voice rates.')
#     voiceEngine.runAndWait()
#     print(newVoiceRate)
#     newVoiceRate = newVoiceRate+50'''

# '''
# working rate changer
# def values():
#     vals=request.values.get("ValueInput","0")
#     x=vals.split()
#     print(x)
#     newVoiceRate = int(x[0])
#     while newVoiceRate <= int(x[0]):
#         voiceEngine.setProperty('rate', newVoiceRate)
#         print(newVoiceRate)
#         newVoiceRate = newVoiceRate+50
#     return render_template("values.html")

# # '''
import pyttsx3 as p
eng=p.init()

voices = eng.getProperty('voices')
# # eng.setProperty("rate",10)
# # x=eng.getProperty("rate")
# # print(x)
# with open("UserData.txt","r") as ofile:
#     red=ofile.read()
#     y=red.split("\n")
#     lens=len(y)
#     print(y)
#     x=2-4
#     print(y[-2])

# x=-5
# for i in range(1,6):

#     print(i,x)
#     x+=1

for i in voices:
    print(i.id)
eng.setProperty("voice",voices[-3].id)
new=eng.getProperty("voice")
eng.say('Testing different voice rates.')
eng.runAndWait()
x=[0,12,13,14,15,16,17]
for i in x:
    eng.setProperty("voice",voices[i].id)
    eng.say('Testing different voice rates.')
    print(new,i)
    eng.runAndWait()