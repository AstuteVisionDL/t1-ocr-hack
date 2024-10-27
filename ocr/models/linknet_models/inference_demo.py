import os

import cv2
from matplotlib import pyplot as plt

from predictor import PipelinePredictor
from utils import get_image_visualization
from linefinder import get_structured_text

for img_path in os.listdir('/workdir/scripts/images'):
    IMG_PATH = f'/workdir/scripts/images/{img_path}'

    PIPELINE_CONFIG_PATH = '/workdir/scripts/pipeline_config.json'

    predictor = PipelinePredictor(pipeline_config_path=PIPELINE_CONFIG_PATH)
    image = cv2.imread(IMG_PATH)

    rotated_image, pred_data = predictor(image)

    image = cv2.imread(IMG_PATH)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    vis = get_image_visualization(
        img=image,
        pred_data=pred_data,
        draw_contours_classes=['shrinked_text'],
        draw_text_classes=['shrinked_text']
    )
    print(pred_data)
    plt.figure(figsize=(40, 40))
    plt.imshow(vis)
    os.makedirs('out', exist_ok=True)
    plt.savefig(f'out/{img_path}.png')

    structured_text = get_structured_text(pred_data, ['shrinked_text'])
    print(structured_text)
    for page_text in structured_text:
        for line_text in page_text:
            if line_text:
                print(' '.join(line_text))
        print('\n')
