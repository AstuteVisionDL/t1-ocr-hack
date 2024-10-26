def signature_classification_accuracy(gt_signatures, pred_signatures):
    correct = sum(1 for gt_sig, pred_sig in zip(gt_signatures, pred_signatures) if gt_sig == pred_sig)
    total = len(gt_signatures)
    return correct / total if total > 0 else 0


def object_detection_metrics(matches, total_gt, total_pred, iou_threshold=0.5):
    true_positives = sum(1 for match in matches if match['iou'] >= iou_threshold)
    false_positives = total_pred - true_positives
    false_negatives = total_gt - true_positives

    precision = true_positives / (true_positives + false_positives) if total_pred > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if total_gt > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1_score


def calculate_iou(boxA, boxB):
    xA = max(boxA[0][0], boxB[0][0])
    yA = max(boxA[0][1], boxB[0][1])
    xB = min(boxA[1][0], boxB[1][0])
    yB = min(boxA[1][1], boxB[1][1])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[1][0] - boxA[0][0]) * (boxA[1][1] - boxA[0][1])
    boxBArea = (boxB[1][0] - boxB[0][0]) * (boxB[1][1] - boxB[0][1])

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou


def word_level_accuracy(gt_text, pred_text):
    return 1.0 if gt_text == pred_text else 0.0


def character_level_accuracy(gt_text, pred_text):
    correct_chars = sum(1 for gt_char, pred_char in zip(gt_text, pred_text) if gt_char == pred_char)
    total_chars = len(gt_text)
    return correct_chars / total_chars if total_chars > 0 else 0
