from transformers import pipeline
from PIL import Image

ocr_pipeline = pipeline("image-to-text", model="raxtemur/trocr-base-ru", device=0)


def run_recognition_tr_ocr(image: Image) -> list[dict]:
    return ocr_pipeline(image)
