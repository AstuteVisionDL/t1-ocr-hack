from PIL import Image
from surya.detection import batch_text_detection
from surya.input.processing import convert_if_not_rgb, slice_polys_from_image
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor

from models.recognition_models.tr_ocr_recognition import run_recognition_tr_ocr


def run_ocr_pipeline_on_image(image: Image.Image) -> list[dict]:
    word_images, detections = detect_with_surya(image)
    recognition = run_recognition_tr_ocr(word_images)
    result_list = []

    for recognition_result, detection_result in zip(recognition, detections[0].bboxes):
        content = recognition_result[0]["generated_text"]
        if content.isupper():
            continue
        bbox = detection_result.bbox
        result_list.append({
            "signature": False,
            "content": content,
            "coordinates": [[bbox[0], bbox[1]], [bbox[2], bbox[3]]]
        })
    return result_list


def detect_with_surya(image: Image.Image):
    """
    Main function of OCR application
    :param image: image with sheet of paper
    :return: text on the image
    """
    det_processor, det_model = load_det_processor(), load_det_model()

    images = convert_if_not_rgb([image])
    det_predictions = batch_text_detection(images, det_model, det_processor)

    all_slices = []

    for idx, (det_pred, image) in enumerate(zip(det_predictions, images)):
        polygons = [p.polygon for p in det_pred.bboxes]
        slices = slice_polys_from_image(image, polygons)
        all_slices.extend(slices)

    return all_slices, det_predictions


if __name__ == '__main__':
    image = Image.open("/home/ark/PycharmProjects/t1hackaton/ocr/data/images/0_kop_0.png")
    result = run_ocr_pipeline_on_image(image)
    print("result",result)
