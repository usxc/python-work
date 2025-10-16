from gtts import gTTS
from playsound3 import playsound

tts = gTTS(text="ハロー！ワールド！", lang="ja", slow=False)

tts.save("hello.mp3")
playsound("hello.mp3")