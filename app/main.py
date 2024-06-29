import cv2
import time
import os
from datetime import datetime
from detector import load_yolo, detect_objects
from database import init_db, save_detection

def draw_labels(frame, boxes, confidences, class_ids, indexes, classes):
    labels = []
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            if class_ids[i] == 18:
                label = "goodboi?"
                color = (0, 255, 255)  # Yellow for dog
            elif class_ids[i] == 8:
                label = "Bubba Delivery?"
                color = (0, 0, 255)  # Red for truck
            else:
                label = str(classes[class_ids[i]])
                color = (0, 255, 0) if class_ids[i] == 0 else (255, 0, 0)  # Green for person, Blue for bicycle
            labels.append(label)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    return frame, labels

def save_image(detection_label, frame):
    os.makedirs('images', exist_ok=True)
    image_file_path = f"images/{detection_label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    cv2.imwrite(image_file_path, frame)
    save_detection(detection_label, image_file_path)
    print(f"Saved image: {detection_label}, {image_file_path}")

def main():
    net, output_layers, classes = load_yolo()
    class_ids_of_interest = [0, 1, 8, 18]  # person, bicycle, truck, dog
    init_db()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    last_detection_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        current_time = time.time()

        if current_time - last_detection_time >= 3:  # Capture image every 3 seconds
            boxes, confidences, class_ids, indexes = detect_objects(net, output_layers, frame, class_ids_of_interest)
            frame, labels = draw_labels(frame, boxes, confidences, class_ids, indexes, classes)
            
            if labels:
                detection_label = labels[0]  # Assuming only one detection for simplicity
                save_image(detection_label, frame)
                last_detection_time = current_time

        cv2.imshow('Camera Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()