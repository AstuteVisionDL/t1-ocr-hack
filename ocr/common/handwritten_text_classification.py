import cv2
import numpy as np


def is_handwritten(image, threshold=0.5):
    """
    Determine if the text in an image is handwritten or printed.

    Parameters:
    - image: The image containing text to be classified.
    - threshold: The threshold to distinguish handwritten vs printed based on stroke variability.

    Returns:
    - bool: True if the text is handwritten, False if printed.
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Measure contour characteristics
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate variability in stroke width
    stroke_widths = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        stroke_widths.append(aspect_ratio)

    # Calculate standard deviation of stroke width
    if len(stroke_widths) == 0:
        return False  # Assume printed if no contours found
    std_dev = np.std(stroke_widths)

    # Return True if variability suggests handwriting
    return std_dev > threshold

