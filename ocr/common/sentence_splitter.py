import os

import cv2
import numpy as np
from PIL import Image


def split_sentence_image_into_text(image: Image.Image):
    """
    Split sentence image into words using Projection Profiles

    Do it by calculate the space between the words by
    :param sentence_image:
    :return:
    """

    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    vertical_projection = np.sum(binary, axis=0)

    threshold = np.max(vertical_projection) * 0.05  # Adjust as needed

    space_indices = np.where(vertical_projection < threshold)[0]

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

    # filter empty words
    word_images = [word for word in word_images if word.shape[1] > 0]
    # convert to PIL images
    word_images = [Image.fromarray(word) for word in word_images]
    return word_images


if __name__ == '__main__':
    print(os.getcwd())
    image = Image.open("ocr/common/0_kop_0_word_0_0.png")
    split_sentence_image_into_text(image)
