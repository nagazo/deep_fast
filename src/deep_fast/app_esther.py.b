import streamlit as st
import requests

st.title("# Dog Classifier 🐶 ")


def upload_file():
    url='http://127.0.0.1:8777/uploadfile/'
    file=st.file_uploader('궁금한 강아지 사진을 업로드', type=['png', 'jpg', 'jpeg', 'webp'])
    if file is not None:
        files={"file": (file.name, file.getvalue(), file.type)}
        response=requests.post(url, files=files)
        if response.status_code==200:
            st.success("이미지 업로드 성공!")
            st.write(response.json())
        else:
            st.error(f"이미지 업로드 실패... {response.status_code}")
            st.write(response.text)
    else:
        st.warning("파일을 업로드 해라")

upload_file()
