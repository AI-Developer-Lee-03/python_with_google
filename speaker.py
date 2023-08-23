import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#음성 인식부(STT구현)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = 'ko')
        print(f'회원님: {text}')
        answer(text)
    
    except sr.UnknownValueError:
        print('JinwooBOT: 죄송해요. 무슨 말씀인지 모르겠어요.')
    
    except sr.RequestError as e:
        print(f'요청 실패: {e}') #API키 오류, 네트워크 문제

#대답부
def answer(input_text):
    pass #구현 나중에

    
# TTS기능 구현
def speak(text):
    print(f'JinwooBOT: {text}')
    file_name = 'voice.mp3'
    tts = gTTS(text = text, lang = 'ko')
    tts.save(file_name)
    playsound(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen) #인풋 들어올 때마다 listen내장함수 호출
# stop_listening(wait_for_stop = False)

while True:
    time.sleep(0.1)
