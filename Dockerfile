# Sử dụng Python 3.11 bản nhẹ để giảm dung lượng image
FROM python:3.11-slim

# Cài đặt các thư viện hệ thống cần thiết cho OpenCV và MediaPipe trên Linux
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy và cài đặt thư viện trước để tận dụng Docker Cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code vào container
COPY . .

# Chạy ứng dụng (Lưu ý: Docker sẽ cần biến môi trường CAMERA_URL)
CMD ["python", "src/main.py"]