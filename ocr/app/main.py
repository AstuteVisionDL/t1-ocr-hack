from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


class DocumentResponse:
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
