echo "Recording your Speech (Ctrl+C to Transcribe)"
arecord -D sysdefault:CARD=1 -q -f cd -t wav -d 0 -r 16000 rec.wav
 
echo "Converting Speech to Text..."
wget -q -U "Mozilla/5.0" --post-file rec.wav --header "Content-Type: audio/x-flac; rate=16000" -O - "https://api.cognitive.microsoft.com/sts/v1.0/recognize?lang=en-us&client=chromium && key=36fd56ca622648b2bdc19dfbfb923ef6" | cut -d\" -f12  > stt.txt
 
echo "You Said:"
value=`cat stt.txt`
echo "$value"
