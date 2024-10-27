import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import io
from PIL import Image
from models.linknet_trocr_version import run_ocr_pipeline_on_image


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)


class DocumentResponse(BaseModel):
    coordinates: list[list[int]]
    content: str
    language: str
    signature: bool


@app.post("/upload-document/", response_model=list[DocumentResponse])
async def upload_document(file: UploadFile = File(...),
                          all: bool = Query(False)):
    response_data = []
    contents = await file.read()

    image = Image.open(io.BytesIO(contents))
    result = run_ocr_pipeline_on_image(image, all)
    return JSONResponse(content=result)


if __name__=='__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
