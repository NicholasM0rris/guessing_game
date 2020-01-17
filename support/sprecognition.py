import speech_recognition as sr
import sys


# print(sr.Microphone.list_microphone_names()[1])

def recognise_audio():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    try:
        with mic as source:
            r.energy_threshold = 0
            r.adjust_for_ambient_noise(source)
            # r.energy_threshold = 700
            audio = r.listen(source)
        dialogue = r.recognize_google(audio)
        return dialogue
    except sr.UnknownValueError:
        return False


def main():
    r = sr.Recognizer()

    mic = sr.Microphone(device_index=1)
    while True:
        try:
            with mic as source:
                r.energy_threshold = 0
                print('checking for ambient noise')
                # r.adjust_for_ambient_noise(source)
                r.energy_threshold = 700
                print('listening')
                audio = r.listen(source)
            print('recognising')
            dialogue = r.recognize_google(audio)
            print(dialogue)
        except sr.UnknownValueError:
            print('No idea what you said')


if __name__ == '__main__':
    main(sys.argv[1:])
