import speech_recognition as sr

def get_script(filename):
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        r = sr.Recognizer()
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.