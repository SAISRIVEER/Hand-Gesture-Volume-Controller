import mediapipe as mp
import cv2
import time

class handDetector():
    def __init__(self, mode = False,maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mphands = mp.solutions.hands
        # self.hands = self.mphands.Hands(self.mode, self.maxHands, self.trackCon, self.detectionCon)
        self.hands = self.mphands.Hands(self.mode, self.maxHands, min_detection_confidence=self.detectionCon, 
                                min_tracking_confidence=self.trackCon)

        self.mpdraw = mp.solutions.drawing_utils


    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw: 
                    self.mpdraw.draw_landmarks(img, handlms,self.mphands.HAND_CONNECTIONS)

        return img
    
    def findPosition(self, img, handNo = 0, draw = True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate (myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                # if id == 0:
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255,0,0), cv2.FILLED)
                
        return lmList
    
def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f"FPS {str(int(fps))}", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 3)

        cv2.imshow("IMAGE",img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
