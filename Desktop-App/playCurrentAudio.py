from audioplayer import AudioPlayer
from gtts import gTTS
import os
import sys

# time.sleep(5)
def func(data):
    speech = gTTS(text=(data), lang='en', slow=False)
    speech.save("current_audio.mp3")
    AudioPlayer("current_audio.mp3").play(block=True) # [BUG] blocks the thread
    os.remove("current_audio.mp3")

data = sys.argv[1]
func(data)