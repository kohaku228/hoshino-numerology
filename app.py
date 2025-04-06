import streamlit as st
import datetime
from collections import Counter

# --- 数値処理ヘルパー関数 ---
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

def evaluate_compatibility(n1, n2):
    distance = abs(n1 - n2)
    if n1 == n2:
        return "似すぎて衝突も／深い理解"
    elif distance == 1:
        return "バランスが良い／補い合える関係"
    elif distance in [2, 3]:
        return "やや違いがあり刺激的な関係"
    else:
        return "理解に時間がかかるが学びが大きい"

def get_relationship_theme(n):
    themes = {
        1: "自立とチャレンジの関係",
        2: "共感と寄り添いの関係",
        3: "楽しさと遊び心の関係",
        4: "安定と現実的なパートナーシップ",
        5: "変化と刺激を求める関係",
        6: "愛と家庭的な関係",
        7: "精神性と心の距離感を学ぶ関係",
        8: "成功と目標達成の協働関係",
        9: "奉仕・学び・運命的な縁",
        11: "霊的な成長・インスピレーションの関係",
        22: "理想実現と共同創造の関係",
        33: "無条件の愛を学び合う魂のパートナー"
    }
    return themes.get(n, "未知の関係")

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
        },
        "birth_day": {
            1: "積極的で行動的な面が強調される人です。",
            2: "協調性があり、人との関係を大切にします。",
            3: "明るくユーモアにあふれ、周囲を楽しませます。",
            4: "安定志向で堅実、努力家タイプです。",
            5: "変化を好み、フットワークが軽い人です。",
            6: "思いやりがあり、家族や仲間に尽くします。",
            7: "内省的で深く物事を考える知性派です。",
            8: "目標達成意欲が高く、実務能力に長けます。",
            9: "人のために動ける、奉仕精神の強い人です。",
            11: "感受性が高く、インスピレーションで動く人です。",
            22: "理想を形にする力を持ち、スケールの大きな思考をします。",
            33: "愛情深く、人々の癒しとなる存在です。"
        },
        "expression": {
            1: "周囲からはリーダー的存在と見られがちです。",
            2: "聞き上手で、サポート役にまわることが多いです。",
            3: "おしゃべり好きで華やかな印象を与えます。",
            4: "まじめで信頼される性格に見られます。",
            5: "自由人で枠にとらわれない雰囲気です。",
            6: "人当たりが良く、安心感を与える人です。",
            7: "ちょっとミステリアスで知的な印象です。",
            8: "しっかり者で現実的な印象を持たれます。",
            9: "優しく博愛的な空気をまとっています。",
            11: "直感的で不思議な雰囲気があります。",
            22: "堂々としてスケールの大きさを感じさせます。",
            33: "優しさに満ち、みんなの母のような存在です。"
        },
        "soul": {
            1: "自分の力で道を切り開きたいという意志があります。",
            2: "人とつながり、支え合いたいという願いがあります。",
            3: "自分を表現して、楽しみたいという想いがあります。",
            4: "堅実に基盤を築きたいという願いがあります。",
            5: "自由に動き、刺激を求めたいという想いがあります。",
            6: "家族や仲間を大切にし、守りたいという気持ちがあります。",
            7: "本質や真実を深く知りたいという欲求があります。",
            8: "目標を達成し、現実的な成果を得たい想いがあります。",
            9: "人や社会に貢献したいという奉仕の精神があります。",
            11: "直感やひらめきを大切にしたいと感じています。",
            22: "理想の世界を実現したいという大きな意志があります。",
            33: "無償の愛を広げたいという魂の願いがあります。"
        }
    }
    return meanings.get(position, {}).get(n, "意味が未設定です。")

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
            st.write(f"誕生数：{bd} → {get_number_meaning('birth_day', bd)}")
            st.write(f"表現数：{ex} → {get_number_meaning('expression', ex)}")
            st.write(f"魂の欲求数：{su} → {get_number_meaning('soul', su)}")

            nums = [lp, bd, ex, su]
            for n, c in Counter(nums).items():
                if c > 1:
                    st.info(f"{n} が複数登場 → 影響が強い数字です")
        else:
            st.warning("名前を入力してください。")

with tab2:
    st.subheader("💑 相性診断")
    col1, col2 = st.columns(2)
    with col1:
        your_name = st.text_input("あなたの名前（ローマ字）", key="your_name")
        your_birth = st.date_input("あなたの生年月日", min_value=datetime.date(1925, 1, 1), max_value=datetime.date(2025, 12, 31), key="your_birth")
    with col2:
        partner_name = st.text_input("相手の名前（ローマ字）", key="partner_name")
        partner_birth = st.date_input("相手の生年月日", min_value=datetime.date(1925, 1, 1), max_value=datetime.date(2025, 12, 31), key="partner_birth")

    if st.button("相性を診断"):
        you = calculate_life_path_number(your_birth)
        partner = calculate_life_path_number(partner_birth)
        total = reduce_number(you + partner)
        relation = evaluate_compatibility(you, partner)
        theme = get_relationship_theme(total)

        st.subheader("🔗 相性診断結果")
        st.write(f"あなたの運命数：{you}")
        st.write(f"相手の運命数：{partner}")
        st.write(f"相性タイプ：{relation}")
        st.write(f"ふたりの関係性テーマ（合計数 {total}）：{theme}")
