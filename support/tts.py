import time
from gtts import gTTS
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

language = 'en-us'
count = 0


def speak(text):
    global count
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(f'speech{count % 3}.mp3')
    mixer.init()
    mixer.music.load(f'speech{count % 3}.mp3')
    mixer.music.play()
    # p = vlc.MediaPlayer(f"support/speech{count % 3}.mp3")
    # p.play()
    # # Wait while speaking
    time.sleep(1.5)
    # duration = p.get_length() / 1000
    # time.sleep(duration)
    count += 1


def main(arglist):
    text = 'TEST: Hello there'
    speak(text)


if __name__ == '__main__':
    main(sys.argv[1:])
