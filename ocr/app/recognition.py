from transformers import pipeline
from PIL import Image
import os

ocr_pipeline = pipeline("image-to-text", model="raxtemur/trocr-base-ru", device=0)

folder_path = 'words'


def run_recognition(image: Image) -> list[dict]:
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # filter for image files
            image_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(image_path).convert("RGB")  # Ensure image is in RGB mode
                result = ocr_pipeline(img)  # Perform OCR
                print(image_path)
                print(result[0]['generated_text'])  # Access the text result
                print()
            except Exception as e:
                print(f"Error opening {filename}: {e}")
