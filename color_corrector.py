import cv2
import numpy as np

color_correction_matrix = np.array([
    [0.617, 0.320, 0.063],
    [0.188, 0.802, 0.010],
    [0.000, 0.251, 0.749]
])

deuteranopia_correction_matrix = np.array([
    [0.625, 0.375, 0],
    [0.7, 0.3, 0],
    [0, 0.3, 0.7]
])

tritanopia_correction_matrix = np.array([
    [0.967, 0.033, 0],
    [0, 0.733, 0.267],
    [0, 0.183, 0.817]
])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: failed to capture image")
        break

    corrected_frame = cv2.transform(frame, color_correction_matrix)
    deuteranopia_frame = cv2.transform(frame, deuteranopia_correction_matrix)
    tritanopia_frame = cv2.transform(frame, tritanopia_correction_matrix)

    cv2.imshow("Original", frame)
    cv2.imshow("Protanopia", corrected_frame)
    cv2.imshow("Deuteranopia", deuteranopia_frame)
    cv2.imshow("Tritanopia", tritanopia_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
