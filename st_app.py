# 설치 필요
# pip install langchain
import streamlit as st
from langchain_community.llms import OpenAI
# import speech_recognition as sr

st.title('🍎🍐🍊 나의 AI Chat 🥝🍅🍆')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')
openai_api_key = st.secrets["openai"]["api_key"]

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
  submitted = st.form_submit_button('Submit')
  # if not openai_api_key.startswith('sk-'):
  #   st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)




# HTML 및 JavaScript 코드  
st.markdown("""  
    <script>  
        // 음성 인식 API를 사용하여 음성을 텍스트로 변환  
        function startDictation() {  
            var recognition = new webkitSpeechRecognition();  
            recognition.continuous = false;  
            recognition.interimResults = false;  

            recognition.lang = 'ko-KR'; // 한국어 설정  
            recognition.start();  

            recognition.onresult = function(event) {  
                var transcript = event.results[0][0].transcript;  
                document.getElementById("speech_input").value = transcript;  
                recognition.stop();  
            };  

            recognition.onerror = function(event) {  
                console.error(event.error);  
                recognition.stop();  
            };  
        }  
    </script>  
""", unsafe_allow_html=True)  

# 음성 입력 버튼  
if st.button("음성 입력 시작"):  
    st.markdown("<button onclick='startDictation()'>음성 입력</button>", unsafe_allow_html=True)  

# 텍스트 입력 필드  
speech_input = st.text_input("음성으로 입력된 텍스트", "", key="speech_input")  

# 결과 출력  
if speech_input:  
    st.write("입력된 텍스트:", speech_input)
else:
    st.write("입력된 텍스트가 없습니다.")





# # 마이크에서 음성 입력을 받아오는 함수
# def get_audio():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)

#     # 음성을 텍스트로 변환
#     text = r.recognize_google(audio)

#     return text

# st.title("음성 인식 예제")
# st.write("아래 버튼을 클릭하면 음성을 입력할 수 있습니다.")
# if st.button("음성 입력"):
#     # 음성 입력 받아오기
#     text = get_audio()
#     st.write("음성 입력 결과 : ", text)