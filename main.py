import speech_recognition as sr

def wav_to_txt(wav_file, txt_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)  # ler o áudio
            text = recognizer.recognize_google(audio_data, language='pt-BR')  # especificar o idioma
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(text)  # escrever texto em um arquivo
            print(f"Transcrição concluída! O texto foi salvo em '{txt_file}'.")
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Usar a função
wav_file = 'C:/Users/nome/Downloads/audio.wav'  # insira o caminho do seu arquivo WAV
txt_file = 'C:/Users/nome/Downloads/audio.txt'  # nome do arquivo de saída
wav_to_txt(wav_file, txt_file)
