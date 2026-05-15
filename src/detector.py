import cv2
import mediapipe as mp
import math

class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.mp_draw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(
            model_complexity=1, 
            min_detection_confidence=0.5, 
            min_tracking_confidence=0.5
        )

    def find_pose(self, frame):
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(img_rgb)
        return results

    def get_angle(self, p1, p2):
        """Tính góc chúi của đoạn thẳng nối 2 điểm so với trục thẳng đứng"""
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        angle = math.degrees(math.atan2(abs(dx), abs(dy)))
        return angle

    def get_distance(self, p1, p2):
        """Tính khoảng cách Euclid giữa 2 điểm (dùng cho nhận diện ngồi gần)"""
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)