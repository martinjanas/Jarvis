import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening for keyword...")

        # Run a loop to continuously listen to the microphone
        while True:
            try:
                print("Listening for 'Jarvisi'...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)  # No timeout or time limit
                
                # Recognizing speech in Czech
                print("Recognizing...")
                text = recognizer.recognize_google(audio, language="cs-CZ")  # Use Google's web speech API
                
                # Check if the keyword "Jarvisi" is in the recognized text
                if "jarvisi" in text.lower():
                    print("Keyword 'Jarvisi' detected. Listening for commands...")
                    
                    # Start processing further commands after "Jarvisi"
                    while True:
                        try:
                            audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)  # Keep listening for commands
                            print("Recognizing...")
                            command = recognizer.recognize_google(audio, language="cs-CZ")  # Recognize the command
                            print(f"Command: {command}")
                            
                            # Check for a stop command (to exit the loop)
                            if "stop" in command.lower():
                                print("Stopping the recognition.")
                                return  # Stop the loop and the function
                        
                        except sr.UnknownValueError:
                            print("Could not understand the audio.")
                        except sr.RequestError:
                            print("Could not request results from Google Speech Recognition service.")
                
                else:
                    print("Did not detect 'Jarvisi', continuing to listen...")
            
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")

# Call the function to start continuous speech recognition
recognize_speech()
