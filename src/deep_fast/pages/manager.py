import streamlit as st
import pymysql
import requests
from PIL import Image
import io

# DB 연결 함수
def get_conn():
    return pymysql.connect(
        host='13.125.248.110',  # 데이터베이스 서버 주소
        user='nagazo',          # 데이터베이스 사용자 이름
        password='4444',        # 데이터베이스 비밀번호
        database='nagazodb'     # 데이터베이스 이름
    )

# 이미지 가져오기 함수
def fetch_image():
    url='http://13.125.248.110:8044/uploadfile/'
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        st.error("Failed to fetch image from URL")
        return None

# 메인 애플리케이션
st.title("Image Processing Manager Page")

# DB에서 이미지 목록 가져오기
conn = get_conn()
with conn:
    with conn.cursor() as cursor:
        sql = "SELECT num, file_path FROM dog_class WHERE label IS NULL ORDER BY num"
        cursor.execute(sql)
        results = cursor.fetchall()

# 결과를 기반으로 이미지 표시 및 라벨 추가
for num, image_url in results:
    st.write(f"Image Number: {num}")
    image = fetch_image(file_path)
    if image:
        st.image(image, caption=f"Image {num}", use_column_width=True)
        
        # 라벨 입력 필드
        label = st.text_input(f"Enter label for image {num}")

        if st.button(f"Submit Label for Image {num}"):
            # 라벨 업데이트 SQL 실행
            with conn.cursor() as cursor:
                update_sql = "UPDATE dog_class SET label = %s WHERE num = %s"
                cursor.execute(update_sql, (label, num))
                conn.commit()
                st.success(f"Label for image {num} updated successfully.")

