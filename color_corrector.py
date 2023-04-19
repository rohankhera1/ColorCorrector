import cv2
import numpy as np

color_correction_matrix = np.array([
    [0.567, 0.433, 0],
    [0.558, 0.442, 0],
    [0, 0.242, 0.758]
])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: failed to capture image")
        break

    corrected_frame = cv2.transform(frame, color_correction_matrix)

    cv2.imshow("Original", frame)
    cv2.imshow("Corrected", corrected_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
