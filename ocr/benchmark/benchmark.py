import os

from ocr.benchmark.annotations import load_annotation
from ocr.benchmark.matching import match_predictions_to_ground_truth
from ocr.benchmark.metrics import character_level_accuracy, word_level_accuracy, calculate_iou, \
    object_detection_metrics, signature_classification_accuracy
from ocr.models.pipeline import run_ocr_pipeline_on_image


def run_benchmark(ground_truth, predictions):
    # Perform matching
    matches, unmatched_gt, unmatched_pred = match_predictions_to_ground_truth(ground_truth, predictions)

    # Initialize accumulators
    char_accuracies = []
    word_accuracies = []
    ious = []
    gt_signatures = []
    pred_signatures = []

    for match in matches:
        gt_item = match['gt']
        pred_item = match['pred']
        iou = match['iou']

        # Text Recognition Metrics
        gt_text = gt_item['content']
        pred_text = pred_item['content']
        char_acc = character_level_accuracy(gt_text, pred_text)
        word_acc = word_level_accuracy(gt_text, pred_text)
        char_accuracies.append(char_acc)
        word_accuracies.append(word_acc)
        ious.append(iou)

        # Signature Classification Accuracy
        gt_signatures.append(gt_item['signature'])
        pred_signatures.append(pred_item['signature'])

    # Compute overall metrics for this image
    total_gt = len(ground_truth)
    total_pred = len(predictions)

    precision, recall, f1_score = object_detection_metrics(matches, total_gt, total_pred)
    average_char_accuracy = sum(char_accuracies) / len(char_accuracies) if char_accuracies else 0
    average_word_accuracy = sum(word_accuracies) / len(word_accuracies) if word_accuracies else 0
    signature_accuracy = signature_classification_accuracy(gt_signatures, pred_signatures)

    # Output the results for this image
    print(f"Character-level Accuracy: {average_char_accuracy:.2f}")
    print(f"Word-level Accuracy: {average_word_accuracy:.2f}")
    print(f"Object Detection - Precision: {precision:.2f}, Recall: {recall:.2f}, F1-Score: {f1_score:.2f}")
    print(f"Signature Classification Accuracy: {signature_accuracy:.2f}")
    print("-" * 50)
    print("\n")

    return average_char_accuracy, average_word_accuracy, precision, recall, f1_score, signature_accuracy


def run_benchmark_for_full_dataset(dataset_path: str):
    annotations = os.path.join(dataset_path, "annotations")
    images = os.path.join(dataset_path, "images")

    # Initialize accumulators for overall metrics
    total_char_accuracy = 0
    total_word_accuracy = 0
    total_precision = 0
    total_recall = 0
    total_f1_score = 0
    total_signature_accuracy = 0
    num_images = 0

    for image_filename in os.listdir(images):
        image_path = os.path.join(images, image_filename)
        annotation_path = os.path.join(annotations, image_filename.replace(".jpg", ".json").replace(".png", ".json"))
        ground_truth = load_annotation(annotation_path)
        predictions = run_ocr_pipeline_on_image(image_path)
        avg_char_acc, avg_word_acc, precision, recall, f1_score, signature_acc = run_benchmark(ground_truth, predictions)

        # Accumulate metrics
        total_char_accuracy += avg_char_acc
        total_word_accuracy += avg_word_acc
        total_precision += precision
        total_recall += recall
        total_f1_score += f1_score
        total_signature_accuracy += signature_acc
        num_images += 1

    # Compute overall average metrics
    if num_images > 0:
        overall_char_accuracy = total_char_accuracy / num_images
        overall_word_accuracy = total_word_accuracy / num_images
        overall_precision = total_precision / num_images
        overall_recall = total_recall / num_images
        overall_f1_score = total_f1_score / num_images
        overall_signature_accuracy = total_signature_accuracy / num_images
    else:
        overall_char_accuracy = 0
        overall_word_accuracy = 0
        overall_precision = 0
        overall_recall = 0
        overall_f1_score = 0
        overall_signature_accuracy = 0

    # Output overall metrics
    print("Overall Metrics:")
    print(f"Average Character-level Accuracy: {overall_char_accuracy:.2f}")
    print(f"Average Word-level Accuracy: {overall_word_accuracy:.2f}")
    print(f"Average Precision: {overall_precision:.2f}")
    print(f"Average Recall: {overall_recall:.2f}")
    print(f"Average F1-Score: {overall_f1_score:.2f}")
    print(f"Average Signature Classification Accuracy: {overall_signature_accuracy:.2f}")


if __name__ == '__main__':
    run_benchmark_for_full_dataset("ocr/data")