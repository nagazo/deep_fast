import pymysql.cursors

def get_conn():
    conn=pymysql.connect(host=os.getenv("DB_IP", "localhost"), port=os.getenv("MY_PORT", "53306"), user='nagazo', password='4444', database='nagazodb', cursorclass=pymysql.cursors.DictCursor)
    return conn

def get_label(query: str, size=-1):
    conn=get_conn()
    query="select label from dog_class where label is not NULL"
    label=pd.read_sql(query, conn)
    conn.close
    return label


import sys
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

load_dt=sys.argv[1]

spark=SparkSession.builder.appName("aggregation").getOrCreate()

label=get_label()

label_spark=spark.createDataFrame(label)

result_path="/home/esthercho/code/pro_3/deep_fast/result.csv"
result=spark.read.csv(result_path, header=True, inferSchema=True)

combined_df=result.join(label_spark, result_df["result"]==labels_spark["label"], "inner").select(result["*"], label_spark["label"])

accuracy_df = combined_df.withColumn("is_correct", when(col("result") == col("label"), 1).otherwise(0))

total_count = accuracy_df.count()
correct_count = accuracy_df.agg({"is_correct": "sum"}).collect()[0][0]
accuracy = correct_count / total_count if total_count > 0 else 0.0

# 9. accuracy를 DataFrame에 추가
accuracy_df = accuracy_df.withColumn("accuracy", when(col("is_correct").isNotNull(), accuracy))

# 10. 결과를 aggregation 테이블에 삽입
aggregation_df = accuracy_df.select("result", "label", "accuracy")

# MariaDB에 데이터 저장
def insert_aggregation(dataframe):
    conn = get_conn()  # MariaDB 연결
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO aggregation (result, label, accuracy)
    VALUES (%s, %s, %s)
    """

    for row in dataframe.collect():
        cursor.execute(insert_query, (row['result'], row['label'], row['accuracy']))

    conn.commit()  # 변경 사항 저장
    conn.close()  # 연결 종료

# 11. aggregation 데이터 삽입
insert_aggregation(aggregation_df)

# 12. Spark 세션 종료
spark.stop()
