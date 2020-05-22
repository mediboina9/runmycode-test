import gtts
import os
text="My Siva I am from Navara"
language="en"
speech=gtts.lang(text=text, lang=language, slow=false)
speech.save("text.mp3")#c:text.mp3
os.system("start text.mp3")
