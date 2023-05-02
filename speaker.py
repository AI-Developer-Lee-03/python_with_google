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
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요, 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 서울 기온은 20도입니다. 맑은 하늘이 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '원 달러 환율은 1200원입니다.'
    elif '고마워' in input_text:
        answer_text = '별말씀을요.'
    elif '휴학' in input_text:
        answer_text = '힘든 순간은 성장의 자양분이 되어줄 거랍니다. 조금만 더 힘내요!'   
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요.'
        stop_listening(wait_for_stop = False)
    elif '홍대입구' in input_text:
        answer_text = '뉴진스의 하입보이요'
    elif '별로네' in input_text:
        answer_text = '어디서 평가질이야? 니가 나 개발했잖아 이진우. 욕해도 소용없어'
    else:
        answer_text = '죄송해요. 진우 개발자님이 실력이 부족해서 제가 답변을 못드리겠어요'
    speak(answer_text)
    
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