import pyaudio
import speech_recognition as sr
#Microphone(device_index: Union[int, None] = None, sample_rate: int = 16000, chunk_size: int = 1024) -> Microphone

#index = pyaudio.get_device_count() - 1
#index = pyaudio.PyAudio().get_device_count() - 1
'''m = None
for i, microphone_name in enumerate(Microphone.list_microphone_names()):
    if microphone_name == "HDA Intel HDMI: 0 (hw:0,3)":
        m = Microphone(device_index=i)
print (i)
print (m)'''

r = sr.Recognizer()

with sr.Microphone(device_index = 1, sample_rate = 48000) as source: 
    audio = r.listen(source) 
    print("Could notdjgh")
try:
    print("You said " + r.recognize(audio))   
except LookupError:                           
    print("Could not understand audio")
    
