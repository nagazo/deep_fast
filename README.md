# 🐶 Dog Image Classification Project

## 📚 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [아키텍처 개요](#🏗️-아키텍처-개요)
3. [주요 기능](#🎯-주요-기능)
4. [시스템 구성 요소](#📋-시스템-구성-요소)
5. [기술 스택](#🛠️-기술-스택)
6. [설치 방법](#🚀-설치-방법)
7. [기여하기](#🤝-기여하기)
8. [라이센스](#📄-라이센스)

## 프로젝트 개요
이 프로젝트는 강아지 사진을 업로드하고, 머신러닝 모델을 통해 해당 강아지의 품종을 예측하는 시스템입니다. **Streamlit**, **FastAPI**, **Airflow**, **PySpark**를 사용하여 이미지 업로드부터 예측, 라벨링까지 자동화된 프로세스를 제공합니다. 관리자는 이미지를 직접 라벨링할 수 있으며, 이를 통해 모델의 성능을 개선할 수 있습니다.

---

## 🏗️ 아키텍처 개요
- "C:\Users\playdata2\Desktop\32기_김동욱\dog_classification 아키텍처.pptx"

## 🎯 주요 기능

1. **이미지 업로드 및 예측**
   - 사용자는 **Streamlit** 인터페이스를 통해 강아지 이미지를 업로드할 수 있습니다.
   - 업로드된 이미지는 **FastAPI**로 전송되어 데이터베이스에 저장됩니다.
   - 업로드된 이미지는 머신러닝 모델을 통해 강아지 품종을 예측합니다.
   - 예측 결과는 로그에 기록됩니다.

2. **관리자 페이지**
   - 관리자는 처리되지 않은 이미지를 확인하고 직접 라벨을 지정할 수 있습니다.
   - 각 이미지에 대한 라벨링 작업은 **Streamlit** 관리 페이지에서 수행됩니다.
   - 관리자는 라벨을 입력하고 제출하여 데이터베이스에 저장합니다.

3. **자동 예측 및 로그 기록**
   - **Airflow**를 사용하여 정해진 간격으로 머신러닝 모델이 실행됩니다.
   - 각 실행 결과는 로그에 기록되어 데이터 분석에 활용됩니다.

4. **데이터 집계 및 분석**
   - **PySpark**를 활용하여 예측된 데이터를 집계하고 분석합니다.
   - 분석 결과는 데이터 기반 의사결정에 사용될 수 있습니다.

5. **사용자 친화적인 인터페이스**
   - **Streamlit**을 이용한 직관적인 사용자 인터페이스로 쉽게 이미지 업로드 및 라벨링 가능.
   - 관리자는 처리할 데이터가 없는 경우에도 쉽게 상태를 확인할 수 있습니다.

## 📋 시스템 구성 요소

- **사용자 인터페이스**: Streamlit
- **API 서버**: FastAPI
- **데이터베이스**: MySQL
- **작업 스케줄러**: Apache Airflow
- **데이터 처리 및 분석**: PySpark

## 🛠️ 기술 스택

- **Python**: 3.8 이상
- **Streamlit**: 1.x
- **FastAPI**: 0.68.0
- **Apache Airflow**: 2.x
- **MySQL**: 5.x 이상
- **PySpark**: 3.x

## 🚀 설치 방법

1. 레포지토리 클론

## 🤝 기여하기

기여를 원하시는 분은 아래의 단계를 따라 주세요:

1. **레포지토리 포크**
   - 이 프로젝트의 레포지토리를 포크하여 개인 계정으로 복사합니다.

2. **새로운 브랜치 생성**
   ```bash
   git checkout -b feature/YourFeature

3. **변경 사항 커밋**
   - 변경 사항을 추가한 뒤 커밋합니다.
   ```bash
   git commit -m "Add your feature"
   
4. **브랜치 푸시**
   - 커밋한 내용을 원격 저장소에 푸시합니다.
   ```bash
   git push origin feature/YourFeature

5. **Pull Request 생성**
   - GitHub에서 포크한 레포지토리로 가서 새로운 Pull Request를 생성합니다.
   - 변경 사항에 대한 설명을 작성하고 리뷰를 요청합니다.


## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 이 라이센스는 소프트웨어의 사용, 복사, 수정, 병합, 출판 및 판매를 허가하며, 소프트웨어의 저작권 및 라이센스 고지를 포함해야 합니다.

자세한 내용은 LICENSE 파일을 참조해 주세요.


```
위의 마크다운 내용은 "변경 사항 커밋" 섹션을 포함한 전체적인 기여 방법을 올바르게 나타냅니다.   
필요에 따라 이 내용을 기존 리드미에 통합하시면 됩니다.
```
