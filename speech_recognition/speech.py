import speech_recognition as sr

r = sr.Recognizer()

# with sr.Microphone() as source:
#     print('Speak something : ')
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print('You said : {}'.format(text))
#     except:
#         print('Sorry, Could not recognize your voice...')

file = sr.AudioFile('sample1.wav')
with file as source:
    audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('Sorry, Could not recognize your voice...')