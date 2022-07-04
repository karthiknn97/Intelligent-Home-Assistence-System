import RPi.GPIO as GPIO
import time
import os
import speech_recognition as sr

from gtts import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#os.system("python3 /home/pi/Nandas/gr.py")

def tts(thistext=""):
    tts=gTTS(text=thistext,lang='en')
    tts.save("proj.mp3")
    os.system("mpg321 proj.mp3")
    os.remove("proj.mp3")

print("Press the button   \n Try saying....\n Help or what can you do")
tts("Press the button and Try saying.... Help ")



while True:
    input_state = GPIO.input(40)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)

        print("recording...")
        os.system("arecord -D hw:1,0 -d 4 -r 48000 -f S16_LE file.wav")
        print("processing...")
        r = sr.Recognizer()
        with sr.AudioFile("file.wav") as source:
            audio = r.listen(source)
            a=r.recognize_google(audio)
            print("you said: ")
            print(a)

        with open("speech.txt", "w") as f:  #, encoding="utf-8" if we want to choose encoding
            f.write(a)
        os.remove("file.wav")       
        os.system("python2 /home/pi/Nandas/command.py")
