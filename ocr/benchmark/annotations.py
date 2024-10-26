import json


def load_annotation(annotations_path):
    with open(annotations_path, 'r') as f:
        annotation = json.load(f)
    return annotation
