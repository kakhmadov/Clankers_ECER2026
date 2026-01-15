import cv2
import numpy as np

CAM_INDEX = 1
FRAME_W, FRAME_H = 640, 480
AREA_MIN = 600

BLUE_LOWER = np.array([95, 100, 80], dtype=np.uint8)
BLUE_UPPER = np.array([130, 255, 255], dtype=np.uint8)

GREEN_LOWER = np.array([40, 70, 70], dtype=np.uint8)
GREEN_UPPER = np.array([80, 255, 255], dtype=np.uint8)

RED_LOWER1 = np.array([0, 150, 100], dtype=np.uint8)
RED_UPPER1 = np.array([10, 255, 255], dtype=np.uint8)
RED_LOWER2 = np.array([170, 150, 100], dtype=np.uint8)
RED_UPPER2 = np.array([180, 255, 255], dtype=np.uint8)

cap = cv2.VideoCapture(CAM_INDEX, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)

while True:
    ok, frame = cap.read()
    if not ok:
        continue

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv, BLUE_LOWER, BLUE_UPPER)
    mask_green = cv2.inRange(hsv, GREEN_LOWER, GREEN_UPPER)
    mask_r1 = cv2.inRange(hsv, RED_LOWER1, RED_UPPER1)
    mask_r2 = cv2.inRange(hsv, RED_LOWER2, RED_UPPER2)
    mask_red = cv2.bitwise_or(mask_r1, mask_r2)

    def detect_and_draw(mask, color_name, box_color):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) < AREA_MIN:
                continue
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)
            cv2.putText(frame, color_name, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, box_color, 2, cv2.LINE_AA)

    detect_and_draw(mask_blue, "Blau", (255, 0, 0))
    detect_and_draw(mask_green, "Gruen", (0, 255, 0))
    detect_and_draw(mask_red, "Rot", (0, 0, 255))

    cv2.imshow("Farberkennung", frame)

    key = cv2.waitKey(1) & 0xFF
    if key in (27, ord('q')):
        break

cap.release()
cv2.destroyAllWindows()