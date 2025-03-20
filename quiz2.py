import streamlit as st
import random

quiz_data = [
    {"question": "SSOT、なんの略？", "options": ["Simple Sign of Terms", "Secret Segment of transcend", "Single Source of Truth"], "answer_index": 2},
    {"question": "Githubでローカルのファイルをリモートリポジトリにプッシュしたい。正しい手順は？", "options": ["add→commit→push", "commit→add→push", "push→add→commit"], "answer_index": 0},
    {"question": "DONE、何と読む？", "options": ["ドーン", "ダーン", "ドゥーン"], "answer_index": 1},
    {"question": "ユーザーが何らかの操作を行った時に画面上に表示され、数秒後に自動的に消える通知のこと、何と言う？", "options": ["トグル", "モーダル", "トースト"], "answer_index": 2}
]

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.score = 0
    random.shuffle(quiz_data)

st.title("内製開発クイズ")

if st.session_state.quiz_index < len(quiz_data):
    current_quiz = quiz_data[st.session_state.quiz_index]
    st.subheader(current_quiz["question"])

    selected_option = st.radio("選択肢", current_quiz["options"], index=None)

    if st.button("回答する"):
        if selected_option is None:
            st.warning("選択肢を選んでください。")
        elif selected_option == current_quiz["options"][current_quiz["answer_index"]]:
            st.session_state.score += 1
            st.success("正解です！")
        else:
            st.error("不正解です...")

        st.session_state.quiz_index += 1
        st.experimental_rerun()

else:
    st.write(f"全問終了！スコア: {st.session_state.score}/{len(quiz_data)}")
    if st.button("再挑戦"):
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        random.shuffle(quiz_data)
        st.experimental_rerun()