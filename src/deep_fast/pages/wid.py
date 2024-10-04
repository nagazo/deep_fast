import streamlit as st
import requests

# 새 페이지: 이미지 업로드 및 분류
def image_classification_page():
    st.title("이 강아지는 어떤 품종인가요? 🐶")  # 페이지 제목 설정

    # 파일 업로드 컴포넌트
    uploaded_file = st.file_uploader("강아지 이미지를 업로드하세요", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # 업로드한 이미지 표시
        st.image(uploaded_file, caption="업로드한 이미지", use_column_width=True)

        # 이미지를 FastAPI 서버로 전송
        files = {"file": uploaded_file.getvalue()}

        try:
            # FastAPI 서버 URL로 POST 요청 (정확한 서버 주소 입력)
            response = requests.post("http://13.125.248.110:8044/uploadfile/", files=files)

            if response.status_code == 200:
                # FastAPI로부터 받은 응답 출력
                result = response.json()
                # 품종 정보를 제외한 나머지 응답 결과 출력
                st.json({
                    "filename": result.get("filename"),
                    "content_type": result.get("content_type"),
                    "file_full_path": result.get("file_full_path"),
                    "request_time": result.get("request_time"),
                })
            else:
                st.error(f"오류: {response.status_code} - {response.text}")
        
        except Exception as e:
            st.error(f"서버에 연결 실패: {str(e)}")

# Streamlit 앱 실행
if __name__ == "__main__":
    image_classification_page()

