import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/IzAAkoS.jpeg");
             background-attachment: fixed;
             background-size: cover
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.title('WHAT IS THIS DOG?')

name = st.text_input("강아지 주인의 이름을 입력하세요:") # 사용자 입력받기

# 사이드바 추가
st.sidebar.title("사이드바")
option = st.sidebar.selectbox("메뉴 선택", ["홈", "주의사항", "정보"])

# 이름 입력
if st.button("제출"):
    st.write(f"안녕하세요, {name}님!")


# 데이터 시각화
# 랜덤 데이터 생성
data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['x', 'y']
)

if option == "데이터 시각화":
    st.write("데이터 시각화")
    
    # 선 그래프
    st.line_chart(data)

    # Matplotlib 사용
    st.write("산점도 그래프")
    fig, ax = plt.subplots()
    ax.scatter(data['x'], data['y'], color='purple')
    st.pyplot(fig)
    
#page_bg_img = '''
#<style>
#body {
#background-image: url("https://previews.123rf.com/images/tankist276/tankist2761506/tankist276150600031/40963827-%EC%8A%AC%ED%94%88-%EC%88%9C%EC%88%98-%ED%95%98%EC%B0%AE%EC%9D%80-%EA%B0%9C-%EA%B0%95%EC%95%84%EC%A7%80-%EB%AC%B4%EC%8B%AC-%ED%95%9C-%ED%82%B9-%EC%B0%B0%EC%8A%A4-%EB%B0%9C-%EB%B0%94%EB%A6%AC-%EA%B1%B0%EC%A7%93%EB%A7%90-%EC%B4%9D%EA%B5%AC%EB%A5%BC.jpg");
#background-size: cover;
#}
#</style>
#'''
#
#st.markdown(page_bg_img, unsafe_allow_html=True)

#def load_data():
#    url = 'http://127.0.0.1/all'
#    r = requests.get(url)
#    d = r.json()
#    return d

#data = load_data()
#df = pd.DataFrame(data)
#df['request_time'] = pd.to_datetime(df['request_time'])


#st.line_chart(data)
