import speech_recognition as sr

def transformar_audio_en_texto():
    # Crear un reconocedor de voz
    reconocedor = sr.Recognizer()

    try:
        # Utilizar el micrófono como fuente de audio
        with sr.Microphone() as origen:
            print("Habla algo...")
            # Escuchar el audio del micrófono
            audio = reconocedor.listen(origen)

        # Utilizar el servicio de reconocimiento de voz de Google para convertir el audio en texto
        texto = reconocedor.recognize_google(audio, language='es-PE')

        # Mostrar el texto reconocido
        print("Texto reconocido:", texto)

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print("Error al solicitar resultados del servicio de reconocimiento de voz:", e)

transformar_audio_en_texto()
