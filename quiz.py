import streamlit as st
import random

# クイズデータ
quiz_data = [
    {"question": "SSOT、なんの略？", "options": ["Simple Sign of Terms", "Secret Segment of transcend", "Single Source of Truth"], "answerIndex": 2},
    {"question": "Githubでローカルのファイルをリモートリポジトリにプッシュしたい。正しい手順は？", "options": ["add→commit→push", "commit→add→push", "push→add→commit"], "answerIndex": 0},
    {"question": "DONE、何と読む？", "options": ["ドーン", "ダーン", "ドゥーン"], "answerIndex": 1},
    {"question": "ユーザーが何らかの操作を行った時に画面上に表示され、数秒後に自動的に消える通知のこと、何と言う？", "options": ["トグル", "モーダル", "トースト"], "answerIndex": 2},
]

# セッション情報の初期化
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_data = random.sample(quiz_data, len(quiz_data))

# クイズの進行
def next_question():
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = None
    
    if st.session_state.selected_option is not None:
        correct_answer = st.session_state.quiz_data[st.session_state.current_question]["answerIndex"]
        if st.session_state.selected_option == correct_answer:
            st.session_state.score += 1

        st.session_state.current_question += 1
        st.session_state.selected_option = None

# クイズのリスタート
def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_data = random.sample(quiz_data, len(quiz_data))
    st.session_state.selected_option = None

# UI
st.title("内製開発クイズ")

if st.session_state.current_question < len(st.session_state.quiz_data):
    quiz_item = st.session_state.quiz_data[st.session_state.current_question]
    st.subheader(quiz_item["question"])

    options = quiz_item["options"]
    st.session_state.selected_option = st.radio("選択肢を選んでください", range(len(options)), format_func=lambda x: options[x])

    if st.button("回答する"):
        next_question()
else:
    st.success(f"クイズ終了！あなたのスコアは {st.session_state.score} / {len(st.session_state.quiz_data)} です。")
    if st.button("もう一度挑戦"):
        restart_quiz()