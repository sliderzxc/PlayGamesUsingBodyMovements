from cvzone.HandTrackingModule import HandDetector
from src.hands.domain.manage_hand_movements import ManageHandSwipes
import cv2

cap = cv2.VideoCapture(0)
hand_detector = HandDetector(maxHands=1)
manage_hand_movements = ManageHandSwipes()
value = 0
coordinates = [0, 0, 0, 0]

while True:
    success, image = cap.read()
    hands, hand_image = hand_detector.findHands(image)

    if hands:
        if value == 5:
            hand = hands[0]
            new_coordinates = hand["bbox"]
            coordinates = manage_hand_movements.handle(coordinates, new_coordinates)
            value = 0
        else:
            value += 1

    cv2.imshow("Hand Detection", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
