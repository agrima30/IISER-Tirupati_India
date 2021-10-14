from audioplayer import AudioPlayer
from gtts import gTTS
import os
import sys

'''
Converts text to speech
'''

def func(data):
    try:
        print('playing')
        speech = gTTS(text=(data), lang='en', slow=False)
        speech.save("current_audio.mp3")
        AudioPlayer("current_audio.mp3").play(block=True)
        print("Just played")
        os.remove("current_audio.mp3")
    except:
        pass

data = sys.argv[1]
func(data)