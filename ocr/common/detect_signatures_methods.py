import PIL.Image
from ultralytics import YOLO

this_file_path = __file__
print(this_file_path)
# models/linknet_models/segm/segm_model.ckpt
model = YOLO("common/signature_model/best.pt")


def detect_signatures(image: PIL.Image.Image):
    results = model(image)[0]
    bboxes = []
    for result in results:
        bbox = result.boxes.data.cpu().numpy().tolist()[0]
        if bbox[-1] == 1.0: # not stamp
            continue
        bbox = [int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])]
        bboxes.append(bbox)
    return bboxes


if __name__ == '__main__':
    results = detect_signatures(PIL.Image.open(r"C:\Users\zarina\PycharmProjects\t1-ocr-hack\ocr\data\images\0_kop_0.png"))
    print(results)