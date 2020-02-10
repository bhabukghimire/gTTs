from gtts import gTTS
import os
from playsound import playsound
word = "my name is bhabuk and i am "
language = 'en'

output = gTTS(text=word, lang=language, slow=False)

output.save("hellos.mp3")
playsound("hello.mp3")