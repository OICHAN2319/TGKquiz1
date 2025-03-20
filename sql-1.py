import streamlit as st
import sqlite3
import random

# データベース接続とクイズデータの取得
def get_quiz_data():
    connection = sqlite3.connect("quiz_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT question, option1, option2, option3, option4, answer FROM quiz")
    data = cursor.fetchall()
    connection.close()
    return data

# クイズデータの読み込み
data = get_quiz_data()

# セッションステートの初期化
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'selected_quizzes' not in st.session_state:
    st.session_state.selected_quizzes = random.sample(data, 5)

# クイズの進行
quiz = st.session_state.selected_quizzes[st.session_state.quiz_index]
question, *options, correct_answer = quiz

st.header("TGKスキルアップクイズ")
st.subheader(f"問題 {st.session_state.quiz_index + 1} / 5")
st.write(question)

# 回答選択
given_answer = st.radio("選択肢を選んでください", options)

if st.button("回答する"):
    if given_answer == correct_answer:
        st.success("正解です！")
        st.session_state.score += 1
    else:
        st.error(f"不正解です。正解は「{correct_answer}」です。")

    # 次のクイズに進む
    st.session_state.quiz_index += 1

# クイズ終了時の結果表示
if st.session_state.quiz_index >= 5:
    st.write("---")
    st.subheader("クイズ終了！")
    st.write(f"あなたの正解数は {st.session_state.score} / 5 でした。")
    st.button("もう一度挑戦する", on_click=lambda: st.session_state.update(quiz_index=0, score=0, selected_quizzes=random.sample(data, 5)))