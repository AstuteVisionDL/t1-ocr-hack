import cv2
from collections import Counter

import numpy as np
import pytesseract


def jaccard_similarity(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    # Создаем счетчики для каждого слова
    counter1 = Counter(word1)
    counter2 = Counter(word2)

    # Получаем множество уникальных символов
    unique_chars = set(counter1.keys()).union(set(counter2.keys()))

    # Считаем количество совпадений
    intersection = sum((min(counter1[char], counter2[char]) for char in unique_chars))

    # Считаем общее количество символов в объединении
    union = sum((max(counter1[char], counter2[char]) for char in unique_chars))

    # Рассчитываем и возвращаем Jaccard Similarity
    return intersection / union if union > 0 else 0

def is_handwritten(image, true_text: str):
    """
    Determine if the text in an image is handwritten or printed.

    Parameters:
    - image: The image containing text to be classified.
    - threshold: The threshold to distinguish handwritten vs printed based on stroke variability.

    Returns:
    - bool: True if the text is handwritten, False if printed.
    """
    # Convert image to grayscale
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, lang='rus', config=custom_config)

    return jaccard_similarity(text, true_text) < 0.4
    #
    # # Apply edge detection
    # edges = cv2.Canny(gray, 100, 200)
    #
    # # Measure contour characteristics
    # contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #
    # # Calculate variability in stroke width
    # stroke_widths = []
    # for cnt in contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     aspect_ratio = w / float(h)
    #     stroke_widths.append(aspect_ratio)
    #
    # # Calculate standard deviation of stroke width
    # if len(stroke_widths) == 0:
    #     return False  # Assume printed if no contours found
    # std_dev = np.std(stroke_widths)
    #
    # # Return True if variability suggests handwriting
    # return std_dev > threshold

