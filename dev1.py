import streamlit as st
import random

# クイズデータ（テスト用にコード内に直接記述）
quiz_data = [
    ("東京の都庁がある区は？", "新宿区", "渋谷区", "千代田区", "新宿区"),
    ("富士山の標高は？", "3776m", "4000m", "3500m", "3776m"),
    ("日本で一番広い都道府県は？", "北海道", "青森県", "岩手県", "北海道"),
    ("お寿司のネタで「たまご」と呼ばれるものは？", "たまご焼き", "数の子", "いくら", "たまご焼き"),
    ("日本の首都は？", "東京", "大阪", "京都", "東京")
]
random.shuffle(quiz_data)

# セッションステートの初期化
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0
    st.session_state['score'] = 0
    st.session_state['selected_answer'] = None
    st.session_state['answered'] = False

# クイズの出題
def show_quiz():
    current_index = st.session_state['current_question']
    if current_index < 5:
        question, opt1, opt2, opt3, answer = quiz_data[current_index]
        st.write(f"**Q{current_index + 1}. {question}**")
        selected_answer = st.radio("選択してください:", [opt1, opt2, opt3], index=None, key=f"answer_{current_index}")

        if st.button("回答する") and not st.session_state['answered']:
            st.session_state['answered'] = True
            if selected_answer == answer:
                st.success("正解！")
                st.session_state['score'] += 1
            else:
                st.error(f"不正解。正解は: {answer}")

        if st.session_state['answered'] and st.button("次の問題へ"):
            st.session_state['current_question'] += 1
            st.session_state['answered'] = False
            st.rerun()
    else:
        st.write(f"### クイズ終了！あなたの正解数は {st.session_state['score']} / 5 です。")
        if st.button("もう一度挑戦する"):
            st.session_state['current_question'] = 0
            st.session_state['score'] = 0
            st.session_state['answered'] = False
            random.shuffle(quiz_data)
            st.rerun()

# アプリケーション本体
st.title("TGKスキルアップクイズ")
show_quiz()
