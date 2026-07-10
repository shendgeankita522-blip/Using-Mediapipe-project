# ------------------------- IMPORT LIBRARIES -------------------------
# -------------->  IMPORT LIBRARY
import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

# MediaPipe modules
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils


# Load local image
def image_to_array(path):
    img = cv2.imread(path)

    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")

    return img


# Give your image path here
mug_path = r"C:\Users\Dell\Downloads\ChatGPT Image Jul 10, 2026, 12_35_42 PM.png"

# Read image
mug = image_to_array(mug_path)


# Initialize Objectron
with mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.5,
    model_name="Cup"
) as objectron:

    # Process image
    results = objectron.process(mug)


# Check detection
if not results.detected_objects:
    print("No box landmarks detected.")
else:
    print("Object detected!")


# Draw results
annotated_image = mug.copy()

if results.detected_objects:
    for detected_object in results.detected_objects:

        # Draw 2D landmarks
        mp_drawing.draw_landmarks(
            annotated_image,
            detected_object.landmarks_2d,
            mp_objectron.BOX_CONNECTIONS
        )

        # Draw 3D axis
        mp_drawing.draw_axis(
            annotated_image,
            detected_object.rotation,
            detected_object.translation
        )


# Convert BGR to RGB for matplotlib
annotated_image = cv2.cvtColor(
    annotated_image,
    cv2.COLOR_BGR2RGB
)


# Display result
plt.figure(figsize=(10, 10))
plt.imshow(annotated_image)
plt.axis("off")
plt.show()
