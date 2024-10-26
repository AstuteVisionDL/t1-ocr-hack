from PIL import Image
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor
from surya.ocr import run_ocr
from surya.schema import OCRResult


def run_ocr_pipeline_on_image(image) -> list[dict]:
    surya_preds = process_single_image(image)
    return [{'signature': False, 'content': text_line.text,
             'coordinates': [[text_line.bbox[0], text_line.bbox[1]], [text_line.bbox[2], text_line.bbox[3]]]} for
            prediction in surya_preds for text_line in prediction.text_lines]


def process_single_image(image: Image) -> list[OCRResult]:
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
