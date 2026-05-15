import cv2
import os
import time
import winsound  # Thư viện có sẵn trên Windows để phát tiếng Beep
from dotenv import load_dotenv
from detector import PoseDetector

load_dotenv()
CAMERA_URL = os.getenv("CAMERA_URL")

def main():
    cap = cv2.VideoCapture(CAMERA_URL)
    detector = PoseDetector()
    
    bad_posture_start = None
    ALERT_SECONDS = 2  # Giảm xuống 2 giây để cảnh báo nhạy hơn theo ý thầy

    print("He thong dang khoi dong...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: continue

        frame = cv2.resize(frame, (640, 480))
        results = detector.find_pose(frame)

        if results.pose_landmarks:
            detector.mp_draw.draw_landmarks(
                frame, results.pose_landmarks, detector.mp_pose.POSE_CONNECTIONS)

            landmarks = results.pose_landmarks.landmark
            
            # Lấy các điểm quan trọng: Tai (7), Vai (11), Mắt trái (3), Mắt phải (6)
            ear = landmarks[7]
            shoulder = landmarks[11]
            eye_l = landmarks[3]
            eye_r = landmarks[6]

            # 1. Check Cúi đầu/Vẹo người
            angle = detector.get_angle(ear, shoulder)
            
            # 2. Check Ngồi quá gần (Khoảng cách giữa 2 mắt càng lớn = càng gần cam)
            dist_eyes = detector.get_distance(eye_l, eye_r)

            # Thiết lập trạng thái mặc định
            status = "Trang thai: Tot"
            color = (0, 255, 0)
            is_alert = False

            # LOGIC CẢNH BÁO
            if angle > 35:
                status = "CANH BAO: CUI DAU / VEO NGUOI"
                is_alert = True
            elif dist_eyes > 0.25: # Ngưỡng 0.25 bạn có thể căn chỉnh lại
                status = "CANH BAO: MAT QUA GAN MAN HINH"
                is_alert = True

            if is_alert:
                color = (0, 0, 255)
                if bad_posture_start is None:
                    bad_posture_start = time.time()
                
                elapsed = time.time() - bad_posture_start
                if elapsed >= ALERT_SECONDS:
                    # Phát tiếng Beep: Tần số 1000Hz, thời gian 100ms
                    winsound.Beep(1000, 100) 
            else:
                bad_posture_start = None

            # Hiển thị thông báo
            cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.putText(frame, f"Goc: {int(angle)} | Mat: {round(dist_eyes, 2)}", 
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow("AIoT Pose Guard - PTIT", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()