import os
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from surya.ocr import run_ocr
from surya.schema import OCRResult

printed_words_filter = ["Краткое наименование организации", "ИНН", "КПП", "ОГРН", "ОКПО", "ОКАТО", "ОКТМО",]


def process_single_image(image_path: str) -> list[OCRResult]:
    """
    Main function of OCR application
    :param image: image with sheet of paper
    :return: text on the image
    """
    image = Image.open(image_path)

    langs = ["ru"]
    det_processor, det_model = load_det_processor(), load_det_model()
    rec_model, rec_processor = load_rec_model(), load_rec_processor()
    predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)
    return predictions


def visualize_predictions(image_path: str, predictions: list[OCRResult], save_path: Path | None = None):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for prediction in predictions:
        for text_line in prediction.text_lines:
            polygon = text_line.polygon
            x_coords, y_coords = zip(*polygon)
            points = list(zip(x_coords, y_coords))
            image = cv2.polylines(image, [np.array(points, dtype=np.int32)], isClosed=True, color=(255, 0, 0), thickness=2)
    if save_path:
        cv2.imwrite(str(save_path) + ".png", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


def save_cropped_words(predictions: list[OCRResult], image_path: str, save_path: Path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for idx, prediction in enumerate(predictions):
        for idx_1, text_line in enumerate(prediction.text_lines):
            polygon = text_line.polygon
            x_coords, y_coords = zip(*polygon)
            min_x, min_y = min(x_coords), min(y_coords)
            max_x, max_y = max(x_coords), max(y_coords)
            min_x = int(min_x)
            min_y = int(min_y)
            max_x = int(max_x)
            max_y = int(max_y)
            cropped_word = image[min_y:max_y, min_x:max_x]
            cv2.imwrite(str(save_path) + f"_word_{idx}_{idx_1}.png", cv2.cvtColor(cropped_word, cv2.COLOR_RGB2BGR))



if __name__ == '__main__':
    os.makedirs("results", exist_ok=True)
    os.makedirs("words", exist_ok=True)
    for image_path in os.listdir("ocr/data"):
        image_path = os.path.join("ocr/data", image_path)
        results = process_single_image(image_path)
        visualize_predictions(image_path, results, save_path=Path("results") / Path(image_path).stem)
        save_cropped_words(results, image_path, save_path=Path("words") / Path(image_path).stem)
