import paho.mqtt.client as mqtt
import time

import os
from gtts import *


 #The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    a=msg.payload
    print ("a")
    if a=="0":
        print (str(msg.payload))
        tts=gTTS(text="hey, its raining",lang='en')
        tts.save("proj.mp3")
        os.system("mpg321 proj.mp3")
        os.remove("proj.mp3")
        
    elif a=="1":
        print (str(msg.payload))
        tts=gTTS(text="Warning: Gas is leaking. switching the exhaust on",lang='en')
        tts.save("proj.mp3")
        os.system("mpg321 proj.mp3")
        os.remove("proj.mp3")
        
 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.115", 1883, 60)

client.loop_forever()





