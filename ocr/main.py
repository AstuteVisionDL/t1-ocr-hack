import os
from pathlib import Path

import cv2

from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from surya.schema import OCRResult
import numpy as np
import matplotlib.pyplot as plt


def process_single_image(image_path: str) -> list[OCRResult]:
    """
    Main function of OCR application
    :param image: image with sheet of paper
    :return: text on the image
    """
    image = Image.open(image_path)
    langs = ["ru"]  # Replace with your languages - optional but recommended
    det_processor, det_model = load_det_processor(), load_det_model()
    rec_model, rec_processor = load_rec_model(), load_rec_processor()
    predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)
    return predictions


def visualize_predictions(image_path: str, predictions: list[OCRResult], save_path: Path | None = None):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 8))
    plt.imshow(image)

    for prediction in predictions:
        for text_line in prediction.text_lines:
            x_coords = text_line.bbox[0::2]  # x coordinates
            y_coords = text_line.bbox[1::2]  # y coordinates
            points = list(zip(x_coords, y_coords))
            cv2.polylines(image, [np.array(points, dtype=np.int32)], isClosed=True, color=(255, 0, 0), thickness=2)

            text_display = f"{text_line.text} ({text_line.confidence:.2f})" if text_line.confidence else text_line.text
            plt.text(x_coords[0], y_coords[0] - 10, text_display, color='blue', fontsize=12, weight='bold')

    plt.axis('off')
    plt.title('OCR Predictions', fontsize=16)

    if save_path:
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0.1)
    else:
        plt.show()


if __name__ == '__main__':
    os.makedirs("results", exist_ok=True)
    for image_path in os.listdir("ocr/data"):
        image_path = os.path.join("ocr/data", image_path)
        results = process_single_image(image_path)
        visualize_predictions(image_path, results, save_path=Path("results") / Path(image_path).stem)
