import  speech_recognition as sr
af=("sahil.wav")
r = sr.Recognizer()
with sr.AudioFile(af) as source:

    audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print('you said: {}'.format(text))
    except sr.UnknownValueError:
        print('sorry couldnt hear you')
    except sr.RequestError:
        print("sorry")