from benchmark.metrics import calculate_iou


def match_predictions_to_ground_truth(ground_truth, predictions, iou_threshold=0.1):
    matches = []
    unmatched_gt = ground_truth.copy()
    unmatched_pred = predictions.copy()

    for pred in predictions:
        best_iou = 0
        best_match = None
        for gt in unmatched_gt:
            iou = calculate_iou(pred['coordinates'], gt['coordinates'])
            if iou > best_iou:
                best_iou = iou
                best_match = gt

        if best_iou >= iou_threshold and best_match:
            matches.append({
                'gt': best_match,
                'pred': pred,
                'iou': best_iou
            })
            unmatched_gt.remove(best_match)
            unmatched_pred.remove(pred)

    return matches, unmatched_gt, unmatched_pred
