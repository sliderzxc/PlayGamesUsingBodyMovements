from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
hand_detector = HandDetector(maxHands=1)
value = 8
coordinates = [0, 0, 0, 0]

while True:
    success, image = cap.read()
    hands, hand_image = hand_detector.findHands(image)

    if hands:
        hand = hands[0]

        if value == 20:
            new_coordinates = hand["bbox"]
            print()
            if coordinates[0] > new_coordinates[0] + 20:
                print("Right")
            elif coordinates[0] < new_coordinates[0] - 20:
                print("Left")
            if coordinates[1] > new_coordinates[1] + 20:
                print("Up")
            elif coordinates[1] < new_coordinates[1] - 20:
                print("Down")
            coordinates = new_coordinates
            value = 0
        else:
            value += 1

    cv2.imshow("Hand Detection", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
