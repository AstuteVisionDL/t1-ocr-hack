import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import os
import io
import cv2
import numpy as np
from PIL import Image
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from surya.ocr import run_ocr
from surya.schema import OCRResult

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

def process_single_image(image) -> list[OCRResult]:
    """
    Main function of OCR application
    :param image: image with sheet of paper
    :return: text on the image
    """


    langs = ["ru"]
    det_processor, det_model = load_det_processor(), load_det_model()
    rec_model, rec_processor = load_rec_model(), load_rec_processor()
    predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)
    return predictions

class DocumentResponse(BaseModel):
    coordinates: list[list[int]]
    content: str
    language: str
    signature: bool


@app.post("/upload-document/", response_model=list[OCRResult])
async def upload_document(file: UploadFile = File(...)):
    response_data = []
    contents = await file.read()

    # Open the image using PIL from the bytes
    image = Image.open(io.BytesIO(contents))
    result = process_single_image(image)
    return JSONResponse(content=result)

if __name__=='__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
