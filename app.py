
import streamlit as st
import datetime
from collections import Counter

def reduce_number(n):
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(d) for d in str(n))
    return n

def char_to_num(c):
    table = {
        'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
        'J':1,'K':2,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,
        'S':1,'T':2,'U':3,'V':4,'W':5,'X':6,'Y':7,'Z':8
    }
    return table.get(c.upper(), 0)

def calculate_life_path_number(birthdate):
    return reduce_number(sum(int(d) for d in birthdate.strftime('%Y%m%d')))

def calculate_birth_day_number(day):
    return reduce_number(day)

def calculate_expression_number(name):
    return reduce_number(sum(char_to_num(c) for c in name if c.isalpha()))

def calculate_soul_urge_number(name):
    return reduce_number(sum(char_to_num(c) for c in name if c.upper() in "AEIOU"))

def get_number_meaning(position, n):
    meanings = {
        "life_path": {
            1: "自立とリーダーシップ。",
            2: "協調と調和。",
            3: "表現力と創造性。",
            4: "安定と努力。",
            5: "自由と変化。",
            6: "愛と責任。",
            7: "探求と精神性。",
            8: "達成と現実性。",
            9: "博愛と奉仕。",
            11: "直感と霊性。",
            22: "理想の具現化。",
            33: "無条件の愛。"
        }
    }
    return meanings.get(position, {}).get(n, "解釈は準備中です。")

# アプリ本体
st.title("🔢 数秘術診断アプリ")

tab1, tab2 = st.tabs(["🧑‍💼 自己診断", "💑 相性診断"])

with tab1:
    name = st.text_input("名前（ローマ字）")
    birthdate = st.date_input("生年月日を選択", min_value=datetime.date(1925, 1, 1), max_value=datetime.date(2025, 12, 31))

    if st.button("診断する"):
        if name:
            lp = calculate_life_path_number(birthdate)
            bd = calculate_birth_day_number(birthdate.day)
            ex = calculate_expression_number(name)
            su = calculate_soul_urge_number(name)

            st.subheader("🔮 診断結果")
            st.write(f"運命数：{lp} → {get_number_meaning('life_path', lp)}")
            st.write(f"誕生数：{bd}")
            st.write(f"表現数：{ex}")
            st.write(f"魂の欲求数：{su}")

            nums = [lp, bd, ex, su]
            for n, c in Counter(nums).items():
                if c > 1:
                    st.info(f"{n} が複数登場 → 影響が強い数字です")
        else:
            st.warning("名前を入力してください。")

with tab2:
    st.write("💑 相性診断は今後追加予定です。")
