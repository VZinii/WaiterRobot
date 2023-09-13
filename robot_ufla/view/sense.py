import speech_recognition as sr

def speech_to_text():
  # Initialize the recognizer
  recognizer = sr.Recognizer()

  # Capture audio from the microphone
  with sr.Microphone() as source:
    # print(sr.Microphone.list_microphone_names())
    print("Fale algo...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
    audio = recognizer.listen(source)

  try:
    # Recognize the speech using Google Web Speech API
    text = recognizer.recognize_google(audio, language='pt-BR')
    text = text.lower()
    stt = text.split(' ')
    return stt
    # print("Você falou:", stt)
  except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
  except sr.RequestError as e:
    print("Sorry, an error occurred. Could not request results; {0}".format(e))
