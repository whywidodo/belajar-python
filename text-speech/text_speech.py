from gtts import gTTS
import os


fh = open("test.txt", "r")
contohText = fh.read().replace("\n", "  ")

bahasa = 'id'

hasil = gTTS(text=contohText, lang=bahasa, slow=False)

hasil.save("output.mp3")

fh.close()

os.system("start output.mp3")
