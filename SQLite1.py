import streamlit as st
import sqlite3
import random
import os

# データベースの絶対パス
DB_PATH = os.path.expanduser("~/desktop/lesson/tech0/tgk/quiz.db")

def get_quiz_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT question, option1, option2, option3, answerIndex FROM quiz")
    data = cursor.fetchall()
    conn.close()
    return [
        {"question": row[0], "options": [row[1], row[2], row[3]], "answerIndex": row[4]} for row in data
    ]

# クイズデータを取得
quiz_data = get_quiz_data()

# 状態管理用セッション変数の初期化
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_order' not in st.session_state and quiz_data:
    st.session_state.quiz_order = random.sample(quiz_data, min(5, len(quiz_data)))
if 'answered' not in st.session_state:
    st.session_state.answered = False

# クイズの出題
def display_question():
    if not quiz_data:
        st.error("クイズデータがありません。データベースにクイズを追加してください。")
        return
    
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
        if st.session_state.current_question < len(st.session_state.quiz_order) - 1:
            if st.button("次の問題へ"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            st.write(f"### 終了！正解数は {st.session_state.score} / {len(st.session_state.quiz_order)} です。")
            if st.button("もう一度挑戦する"):
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.quiz_order = random.sample(quiz_data, min(5, len(quiz_data)))
                st.session_state.answered = False
                st.rerun()

# アプリのタイトル
st.title("TGKスキルアップクイズ")
display_question()