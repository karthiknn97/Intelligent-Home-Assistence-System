import os
from gtts import *
say="hello attige rohan calling "
tts=gTTS(text=say,lang='en')
tts.save("proj.mp3")
os.system("omxplayer proj.mp3")
os.remove("proj.mp3")

