from gtts import gTTS
import os

#fh = open("text.txt","r")
#myText = fh.read().replace("\n","")


myText = "ตู้เย็นอัจฉริยะ ยินดีต้อนรับค่ะ, กดที่นี่เพื่อดำเนินการต่อไป"

language = 'th'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")

# https://www.youtube.com/watch?v=_Q8wtPCyMdo&ab_channel=ProgrammingKnowledge