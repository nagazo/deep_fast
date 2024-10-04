from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
from deep_fast.util_esther import get_max_label
import io
from fastapi import Request
from typing import Union

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    img = await file.read()
    model=pipeline("image-classification", model="roschmid/dog-races")

    from PIL import Image
    img = Image.open(io.BytesIO(img))
    prediction = model(img)

    label = get_max_label(prediction)

    score = prediction[0]['score']

#    if score > 0.8:
#        response_image_path = ""
#    else:
#        response_image_path = "핫도그 아님"

    return {
            "label":label,
            "prediction":prediction
            }

