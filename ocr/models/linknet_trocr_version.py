import PIL.Image
import numpy as np
from PIL import Image

from ocr.common.handwritten_text_classification import is_handwritten
from ocr.models.linknet_models.predictor import PipelinePredictor, get_upscaled_bbox
from ocr.models.recognition_models.tr_ocr_recognition import run_recognition_tr_ocr


PIPELINE_CONFIG_PATH = "models/linknet_models/pipeline_config.json"
predictor = PipelinePredictor(pipeline_config_path=PIPELINE_CONFIG_PATH)


def run_ocr_pipeline_on_image(image: Image.Image) -> list[dict]:
    word_images, bboxes = detect_with_linknet(image)
    recognition = run_recognition_tr_ocr(word_images)
    result_list = []

    i = 0
    for recognition_result, bbox in zip(recognition, bboxes):
        content = recognition_result[0]["generated_text"]
        word_crop = word_images[i]
        i += 1
        #if not is_handwritten(word_crop, content):
        #     continue
        if len(content.split()) > 1:
            content = max(content.split(), key=len)
        result_list.append({
            "signature": False,
            "content": content,
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
