from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
from deep_fast.util_esther import get_max_label
import io
from fastapi import Request
from typing import Union

from datetime import datetime
from pytz import timezone
import pymysql.cursors

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    ts = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
    # 이미지 파일 서버에 저장
    img = await file.read()
    file_name = file.filename
    file_label = file_name.split('.')[0].split('_')[0]
    file_ext = file.content_type.split('/')[-1] # content_type = image/png 형식으로 출력됨

    upload_dir = os.getenv('UPLOAD_DIR', "./photo")
    file_full_path = os.path.join(upload_dir, f'{uuid.uuid4()}.{file_ext}')
    os.makedirs(os.path.dirname(file_full_path), exist_ok = True)

    with open(file_full_path, 'wb') as f:
        f.write(img)
    # 연결 DB 수정해야함
    connection = get_conn()
    # insert 양식 손봐야함
    sql = "INSERT INTO `image_processing`(file_name, label, file_path, request_time, request_user) VALUES (%s, %s, %s, %s, %s)"
    with connection:
        with connection.cursor() as cursor:
            # insert 들어갈 value들 수정해야함
            cursor.execute(sql,(file_name, file_label, file_full_path, ts, "n18"))
        connection.commit()
#    img = await file.read()
#    model=pipeline("image-classification", model="roschmid/dog-races")
#
#    from PIL import Image
#    img = Image.open(io.BytesIO(img))
#    prediction = model(img)
#
#    label = get_max_label(prediction)
#
#    score = prediction[0]['score']
    # return 값 뭐 다르게 하고 싶으면 수정해야함
    return {
            "filename": file_name,
            "filelabel" : file_label,
            "content_type" : file.content_type,
            "file_full_path" : file_full_path,
            "request_time" : ts
            }
