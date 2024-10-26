import os

import numpy as np
import cv2
import numpy as np


def split_sentence_image_into_text(image_path: str):
    """
    Split sentence image into words using Projection Profiles

    Do it by calculate the space between the words by
    :param sentence_image:
    :return:
    """


    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    vertical_projection = np.sum(binary, axis=0)

    threshold = np.max(vertical_projection) * 0.005  # Adjust as needed

    # Find indices where projection is below the threshold
    space_indices = np.where(vertical_projection < threshold)[0]

    # Find continuous space regions
    spaces = []
    start = None
    for i in range(len(space_indices)):
        if start is None:
            start = space_indices[i]
        if i == len(space_indices) - 1 or space_indices[i + 1] != space_indices[i] + 1:
            end = space_indices[i]
            spaces.append((start, end))
            start = None

    # Split the image into words based on detected spaces
    prev_end = 0
    word_images = []
    for space in spaces:
        end = space[0]
        word = image[:, prev_end:end]
        word_images.append(word)
        prev_end = space[1]

    # Add the last word
    word = image[:, prev_end:]
    word_images.append(word)

    os.makedirs('ocr/data/debug_splitter', exist_ok=True)
    # Save or process word_images as needed
    for idx, word_img in enumerate(word_images):
        if word_img.shape[1] > 0:
            cv2.imwrite(f'ocr/data/debug_splitter/word_{idx}.png', word_img)


if __name__ == '__main__':
    print(os.getcwd())
    split_sentence_image_into_text("ocr/common/0_kop_0_word_0_0.png")
