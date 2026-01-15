#!/usr/bin/python3
import cv2
import numpy as np

CAM_INDEX = 0
FRAME_W, FRAME_H = 640, 480
AREA_MIN = 2000

BLUE_LOWER = np.array([95, 100, 80], dtype=np.uint8)
BLUE_UPPER = np.array([130, 255, 255], dtype=np.uint8)

GREEN_LOWER = np.array([40, 70, 70], dtype=np.uint8)
GREEN_UPPER = np.array([80, 255, 255], dtype=np.uint8)

RED_LOWER1 = np.array([0, 150, 100], dtype=np.uint8)
RED_UPPER1 = np.array([10, 255, 255], dtype=np.uint8)
RED_LOWER2 = np.array([170, 150, 100], dtype=np.uint8)
RED_UPPER2 = np.array([180, 255, 255], dtype=np.uint8)

# Kamera einmal oeffnen und behalten
cap = cv2.VideoCapture(CAM_INDEX)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)


def detect_and_draw(frame, mask, color_name, box_color):
    direction = "N"

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    for cnt in contours:
        if cv2.contourArea(cnt) < AREA_MIN:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        center_x = x + w // 2

        if color_name == "Gruen":
            third = FRAME_W // 3
            if center_x < third:
                direction = "L"
            elif center_x < 2 * third:
                direction = "Z"
            elif center_x > 2 * third:
                direction = "R"
            else:
                direction = "N"

        cv2.rectangle(frame, (x, y), (x + w, y + h), box_color, 2)
        cv2.putText(
            frame,
            color_name,
            (x, y - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            box_color,
            2,
            cv2.LINE_AA,
        )

    return direction


def get_direction_and_frame():
    ok, frame = cap.read()
    if not ok:
        return "N", None

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv, BLUE_LOWER, BLUE_UPPER)
    mask_green = cv2.inRange(hsv, GREEN_LOWER, GREEN_UPPER)
    mask_r1 = cv2.inRange(hsv, RED_LOWER1, RED_UPPER1)
    mask_r2 = cv2.inRange(hsv, RED_LOWER2, RED_UPPER2)
    mask_red = cv2.bitwise_or(mask_r1, mask_r2)

    detect_and_draw(frame, mask_blue, "Blau", (255, 0, 0))
    direction_green = detect_and_draw(frame, mask_green, "Gruen", (0, 255, 0))
    detect_and_draw(frame, mask_red, "Rot", (0, 0, 255))

    return direction_green, frame


def get_direction():
    direction, _ = get_direction_and_frame()
    return direction


def main():
    if not cap.isOpened():
        print("Kamera konnte nicht geoeffnet werden")
        return

    while True:
        direction, frame = get_direction_and_frame()
        if frame is None:
            continue

        third = FRAME_W // 3
        cv2.line(frame, (third, 0), (third, FRAME_H), (255, 255, 255), 1)
        cv2.line(frame, (2 * third, 0), (2 * third, FRAME_H), (255, 255, 255), 1)

        cv2.imshow("Farberkennung", frame)
        print(direction, flush=True)

        key = cv2.waitKey(1) & 0xFF
        if key in (27, ord("q")):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()