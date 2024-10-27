import PIL.Image
import numpy as np
from PIL import Image

from common.handwritten_text_classification import is_handwritten
from models.linknet_models.predictor import PipelinePredictor, get_upscaled_bbox
from models.recognition_models.tr_ocr_recognition import run_recognition_tr_ocr
from common.detect_signatures_methods import detect_signatures


PIPELINE_CONFIG_PATH = "models/linknet_models/pipeline_config.json"
predictor = PipelinePredictor(pipeline_config_path=PIPELINE_CONFIG_PATH)


def calculate_iou_yolo_format(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou


def match_signatures_with_predictions(signature_boxes, predictions, iou_threshold=0.1):
    matches = []
    unmatched_gt = signature_boxes.copy()
    unmatched_pred = predictions.copy()

    for pred in predictions:
        best_iou = 0
        best_match = None
        for gt in unmatched_gt:
            iou = calculate_iou_yolo_format(pred, gt)
            if iou > best_iou:
                best_iou = iou
                best_match = gt

        if best_iou >= iou_threshold and best_match:
            matches.append(pred)
            unmatched_gt.remove(best_match)
            unmatched_pred.remove(pred)

    return matches, unmatched_gt, unmatched_pred


def run_ocr_pipeline_on_image(image: Image.Image) -> list[dict]:
    word_images, bboxes = detect_with_linknet(image)
    signature_bboxes = detect_signatures(image)
    matches, unmatched_signatures, _ = match_signatures_with_predictions(signature_bboxes, bboxes)

    recognition = run_recognition_tr_ocr(word_images)
    result_list = []

    i = 0
    for recognition_result, bbox in zip(recognition, bboxes):
        content = recognition_result[0]["generated_text"]
        word_crop = word_images[i]
        i += 1
        try:
            if not is_handwritten(word_crop, content):
                continue
        except Exception as e:
            print("Exception during handwriting detection", e.with_traceback(e.__traceback__))
        if len(content.split()) > 1:
            content = max(content.split(), key=len)
        signature = False
        if bbox in matches:
            signature = True
            content = "."
            matches.pop(matches.index(bbox))

        result_list.append({
            "signature": signature,
            "content": content,
            "coordinates": [[bbox[0], bbox[1]], [bbox[2], bbox[3]]]
        })
    for signature in unmatched_signatures:
        bbox = signature
        result_list.append({
            "signature": True,
            "content": ".",
            "coordinates": [[bbox[0], bbox[1]], [bbox[2], bbox[3]]]
        })
    return result_list


def detect_with_linknet(image: Image.Image):
    """
    Detection function, return slices with words and bboxes
    """
    words = []
    # leave only 3 channels
    pil_image = image.convert("RGB")
    image = np.array(pil_image)

    rotated_image, pred_data = predictor(image)
    bboxes = []
    for p in pred_data['predictions']:
        if 'crop' not in p or p['crop'] is None:
            continue
        words.append(PIL.Image.fromarray(p['crop']))
        bbox = get_upscaled_bbox(p['bbox'], 1.1, 2.3)
        bboxes.append(bbox)
    return words, bboxes


if __name__ == '__main__':
    image = Image.open(r"C:\Users\zarina\PycharmProjects\t1-ocr-hack\ocr\data\images\0_kop_0.png")
    result = run_ocr_pipeline_on_image(image)
    print("result", result)
