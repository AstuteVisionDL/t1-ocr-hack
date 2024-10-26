from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

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
async def upload_document(file: UploadFile = File(...)):
    response_data = [
        {
            "coordinates": [[0, 0], [10, 10]],
            "content": "text",
            "language": "rus",
            "signature": False,
        },
        {
            "coordinates": [[10, 10], [20, 20]],
            "content": "",
            "language": "",
            "signature": True,
        },
    ]
    return JSONResponse(content=response_data)
