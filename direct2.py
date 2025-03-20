import streamlit as st
import random

# クイズデータ
quiz_data = [
    {"question": "天然ガスは、何度まで冷やすと液体に変化する？", "options": ["マイナス342度", "マイナス115度", "マイナス162度"], "answerIndex": 2},
    {"question": "アジャイル（agile）、どういう意味？", "options": ["臨機応変な", "柔軟な", "俊敏な・機敏な"], "answerIndex": 2},
    {"question": "PHPのフレームワークではないものはどれ？", "options": ["Laravel", "Django", "Symfony"], "answerIndex": 1},
    {"question": "「ナクストジェイエス」はどれ？", "options": ["Next.js", "Nuxt.js", "Nest.js"], "answerIndex": 1},
    {"question": "Pythonでリストの要素数を取得する関数は？", "options": ["size()", "length()", "len()"], "answerIndex": 2},
]

# 状態管理用セッション変数の初期化
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_order' not in st.session_state:
    st.session_state.quiz_order = random.sample(quiz_data, 5)
if 'answered' not in st.session_state:
    st.session_state.answered = False

# クイズの出題
def display_question():
    current_quiz = st.session_state.quiz_order[st.session_state.current_question]
    st.write(f"### {current_quiz['question']}")

    # 選択肢表示
    selected_option = st.radio("選択肢", current_quiz['options'], index=None)

    if st.button("回答する") and not st.session_state.answered:
        st.session_state.answered = True
        if selected_option == current_quiz['options'][current_quiz['answerIndex']]:
            st.success("正解！")
            st.session_state.score += 1
        else:
            st.error(f"不正解。正解は「{current_quiz['options'][current_quiz['answerIndex']]}」です。")

    if st.session_state.answered:
        if st.session_state.current_question < 4:
            if st.button("次の問題へ"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            st.write(f"### 終了！正解数は {st.session_state.score} / 5 です。")

# アプリのタイトル
st.title("TGKスキルアップクイズ")
display_question()
