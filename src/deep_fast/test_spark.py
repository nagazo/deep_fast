import requests
from pyspark.sql import SparkSession

# Spark 세션 생성
spark = SparkSession.builder \
    .appName("Load JSON Data") \
    .getOrCreate()

# 로깅 레벨 설정
spark.sparkContext.setLogLevel("ERROR")

def load_data():
    url = 'http://43.200.252.241:8044/all'
    r = requests.get(url)  # 요청 메서드 확인
    if r.status_code == 200:
        d = r.json()  # JSON 데이터를 로드
        return d
    else:
        print(f"Error: {r.status_code} - {r.text}")
        return None

# 데이터 로드
data = load_data()
print(data)
#if data:
#    # JSON 데이터를 RDD로 변환하여 DataFrame으로 변환
#    rdd = spark.sparkContext.parallelize([data])
#    df = spark.read.json(rdd)
#
#    df.show()  # DataFrame 내용 출력
