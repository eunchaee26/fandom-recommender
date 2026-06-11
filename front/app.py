import streamlit as st
import requests

st.title("🎤 나에게 맞는 덕질 유형 추천기")

st.write("질문에 답하면 당신에게 맞는 덕질 유형을 추천해드립니다!")

stage = st.slider(
    "무대를 보는 걸 얼마나 좋아하나요?",
    1, 5, 3
)

variety = st.slider(
    "예능 클립이나 비하인드 영상을 얼마나 좋아하나요?",
    1, 5, 3
)

acting = st.slider(
    "연기나 작품 감상을 얼마나 좋아하나요?",
    1, 5, 3
)

sns = st.slider(
    "떡밥(SNS, 라이브, 브이로그)을 얼마나 중요하게 생각하나요?",
    1, 5, 3
)

music = st.slider(
    "음악 자체의 완성도를 얼마나 중요하게 생각하나요?",
    1, 5, 3
)

voice = st.slider(
    "음색과 감성을 얼마나 중요하게 생각하나요?",
    1, 5, 3
)

concert = st.slider(
    "공연 영상 시청을 얼마나 좋아하나요?",
    1, 5, 3
)

if st.button("🎯 추천받기"):

    data = {
        "stage": stage,
        "acting": acting,
        "music": music,
        "voice": voice,
        "variety": variety,
        "sns": sns,
        "concert": concert
    }

    response = requests.post(
        "http://backend:8000/recommend",
        json=data
    )

    result = response.json()

    st.success(f"추천 결과: {result['result']}")
    st.write(result["description"])