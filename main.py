from Whisper.whisper_audio import Audio_To_Text

att = Audio_To_Text()
while True:
    att.listen()
    print(att.transcribe())