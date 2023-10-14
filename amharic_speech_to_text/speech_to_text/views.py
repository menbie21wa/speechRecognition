from django.shortcuts import render
import speech_recognition as sr
import time
def recognize_speech(request):
    if request.method == 'POST':
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Function to perform speech recognition from microphone input
        def recognize_amharic_speech_from_microphone():
            with sr.Microphone() as source:
                print("Please start speaking...")
                try:
                    audio_data = recognizer.listen(source, timeout=10)  # Adjust the timeout as needed
                    print("Recognizing...")
                    # Recognize the speech using the Google Web Speech API
                    recognized_text = recognizer.recognize_google(audio_data, language="am-ET")
                    return recognized_text
                except sr.WaitTimeoutError:
                    return "Speech input timeout. No speech detected."
                except sr.UnknownValueError:
                    return "Could not understand the audio"
                except sr.RequestError as e:
                    return f"Could not request results; {e}"

        # Recognize speech from the microphone
        result = recognize_amharic_speech_from_microphone()

        return render(request, 'speech_recognition.html', {'result': result})
    return render(request, 'speech_recognition.html')

