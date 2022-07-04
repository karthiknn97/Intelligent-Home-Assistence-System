import cv2
import os
import pytesseract
from PIL import Image
from gtts import *

a=cv2.imread("a4.png",0) #load image in gray 

# apply thresholding to preprocess the image
b= cv2.threshold(a, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]    #not effective in tested cases

#median blurring should be done to remove noise
med= cv2.medianBlur(b,5)
#cv2.imshow("image",b)

text=pytesseract.image_to_string(med,lang='eng')

print(text)
fil=open("ocrdata.txt","w")   #open a file in write mode
fil.writelines(text)

#text to speech of ocr
tts=gTTS(text,lang='en')
tts.save("proj.mp3")
os.system("omxplayer proj.mp3")
os.remove("proj.mp3")

cv2.imshow("a1",med)
cv2.waitKey(0)
cv2.destroyAllWindows()
fil.close()

