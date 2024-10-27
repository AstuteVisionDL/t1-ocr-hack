import json


def load_annotation(annotations_path):
    with open(annotations_path, 'r', encoding="utf-8") as f:
        annotation = json.load(f)
    return annotation
