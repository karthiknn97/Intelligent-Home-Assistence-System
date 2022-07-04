import speech_recognition as sr
#import urllib2

r=sr.Recognizer()
with sr.Microphone(device_index = 4, sample_rate = 48000) as source:
    while True:
        print("say")
        audio=r.listen(source, duration = 5)
        print("Could notdjgh")

        BING_KEY = "36fd56ca622648b2bdc19dfbfb923ef6"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
        try:
            print("I think you said " + r.recognize_bing(audio, key=BING_KEY))
        except sr.UnknownValueError:
            print("I could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))



""" if r.recognize_bing(audio, key=BING_KEY) == 'turn on the light':
            response = urllib2.urlopen('http://192.168.0.114/LED=ON')
            html = response.read()
        if r.recognize_bing(audio, key=BING_KEY) == 'turn off the light':
            response = urllib2.urlopen('http://192.168.0.114/LED=OFF')
            html = response.read()
"""



    
