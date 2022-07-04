arecord -D hw:1,0 -r 48000 -f S16_LE file.flac
echo "Converting Speech to Text..."
wget -q -U "Mozilla/5.0" --post-file file.flac --header "Content-Type: audio/x-flac; rate=48000" -O - "https://api.cognitive.microsoft.com/sts/v1.0/recognize?lang=en-us&client=chromium&key=36fd56ca622648b2bdc19dfbfb923ef6” |cut -d\" -f8 >stt.txt
echo "extract recognized text"
cat stt.txt
echo "You Said:"
value=`cat stt.txt`
echo "$value"
