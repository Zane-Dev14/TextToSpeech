#Importing Modules
import pyttsx3 as p
from flask import Flask, render_template, request
from text import *
from var import voices
from settings import chooseVoice,rateOfSpeed,setVolume
import os
#Initializing Engine, using ESpeak as default engine
voiceEngine = p.init()
engine = p.init()

#setting the flask app to app.py

app = Flask(__name__)

#Flask Routes Start Here 
#<----------------------------------------------------------------------->

#default home page
@app.route('/home', methods =["GET","POST"])
def home():
    return render_template("home.html")

#About Page, More info
@app.route('/about', methods =["GET","POST"])
def about():
    return render_template("about.html")

#Page to select which voice to be used
@app.route('/voice', methods =["GET","POST"])
def voice():
    if request.method== "POST":
        for i in range (len(voices)):
            if request.form.get("submit%s"%i)==int(i):
                print("Selecting Voice Number %s"%i)
                chooseVoice(i)                
    return render_template("voices.html",listOfVoices=voic,len=length)

#Page to type the text to be converted to speech
@app.route('/texting', methods =["GET","POST"])
def texting():
    default_value = '0'
    data=request.form.get('boxInput',default_value)
    if data!=default_value:
        Text(data)
        saveData(data)
    return render_template("texting.html")

#Page to get values of rate and Volume
@app.route('/values', methods =["GET","POST"])
def values():
    rateInputted=request.values.get("RateInput","0")
    VolumeInputted=request.values.get("VolumeInput","0")
    newVoiceRate = int(rateInputted)
    while newVoiceRate <= int(rateInputted):
        if int(rateInputted)!=0:
            voiceEngine.setProperty('rate', newVoiceRate)            
        newVoiceRate = newVoiceRate+50
            
    if VolumeInputted!="0":
        setVolume(VolumeInputted)
             
    return render_template("values.html")

#Page to get userdata

@app.route("/getdata",methods=["GET","POST"])
def fetchdata():
    got =getData("UserData.txt")
    default_value = '0'
    number=request.form.get('deleteNumber',default_value)
    if number!=default_value:
        deleteNewData(int(number))
    return render_template("readData.html",DataSent=got)
#Flask ends here
#<-------------------------------------------------------------------------__>

#Saving Userdata to a TextFile named "Userdata"
def saveData(inputtedData):
    with open("UserData.txt","a") as ifile:
        ifile.write("\n"+inputtedData)

#Getting the data from the file
def getData(fileName):
    with open("%s"%fileName,"r") as ofile:
        red=ofile.read()
        y=red.split("\n")
        lens=len(y)
        last5=y[-6:lens-1]
        return last5

def deleteNewData(numberDeleting):
    x=-5
    with open("UserData.txt","r") as o1file:
        readss=o1file.read()
        spi=readss.split("\n")
        for i in range(1,6):
            if i==numberDeleting:
                for j in spi:
                    if spi[x]!=j:
                        with open("UserData1.txt","a") as o2file:
                            o2file.write(j+"\n")
            x+=1
    os.remove("UserData.txt")
    os.rename("UserData1.txt","UserData.txt")
        
if __name__ == '__main__':
   app.run(debug=True)
