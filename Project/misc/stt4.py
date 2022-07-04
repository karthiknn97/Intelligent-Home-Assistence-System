import speech_recognition as sr
r=sr.Recognizer()
with sr.AudioFile("/home/pi/file.wav") as source:
    print("convert")
    BING_KEY = "36fd56ca622648b2bdc19dfbfb923ef6"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        print("I think you said " + r.recognize_bing("/home/pi/file.wav", key=BING_KEY))
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

