# PoseAlert - AIoT Posture Guard 🤖🛡️

Hệ thống giám sát tư thế ngồi học thông minh sử dụng trí tuệ nhân tạo (MediaPipe) để bảo vệ sức khỏe người dùng. Dự án được phát triển nhằm cảnh báo các tư thế sai có thể gây hại cho cột sống và thị lực.

## ✨ Tính năng chính
* **Cảnh báo tư thế:** Tự động nhận diện khi người dùng cúi đầu quá thấp hoặc vẹo người.
* **Bảo vệ thị lực:** Cảnh báo khi khoảng cách từ mắt đến màn hình quá gần.
* **Cảnh báo âm thanh:** Phát tiếng Beep sau 2 giây duy trì tư thế sai.
* **Kết nối linh hoạt:** Hỗ trợ lấy dữ liệu camera từ Smartphone thông qua IP Webcam.

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.11
* **Thư viện AI:** MediaPipe (Pose Estimation)
* **Xử lý hình ảnh:** OpenCV
* **Phần cứng thử nghiệm:** Laptop NVIDIA RTX 3050 & Smartphone Camera

## 🚀 Hướng dẫn cài đặt
1. **Clone dự án:**
   ```bash
   git clone [https://github.com/tuong-38/PoseAlert.git](https://github.com/tuong-38/PoseAlert.git)
   cd PoseAlert
