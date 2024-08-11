import speech_recognition as sr

def process_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            # Here you would add code to handle the text as a calculator input
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio")
        except sr.RequestError as e:
            print("Sorry, there was an error with the request: {0}".format(e))
