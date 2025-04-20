# Yolo:Home – Smart AIoT Home System

## Giới thiệu

Yolo:Home là một hệ thống nhà thông minh tích hợp công nghệ AIoT (AI + IoT), cho phép người dùng giám sát, điều khiển và tương tác với các thiết bị trong nhà một cách thông minh và an toàn. Hệ thống sử dụng FastAPI cho backend, MQTT với Adafruit IO để giao tiếp thời gian thực, RabbitMQ để xử lý cảnh báo, và cơ sở dữ liệu MySQL để lưu trữ.

## Tính năng chính

- Đăng ký và đăng nhập người dùng với JWT
- Giám sát cảm biến (nhiệt độ, độ ẩm, ánh sáng)
- Cảnh báo khi vượt ngưỡng giá trị cho phép
- Điều khiển thiết bị từ xa qua API
- Ghi nhận và hiển thị dữ liệu lịch sử

## Kiến trúc

- **Ngôn ngữ:** Python 3.9+
- **Framework:** FastAPI
- **Giao tiếp thời gian thực:** MQTT (Adafruit IO)
- **Queue xử lý song song:** RabbitMQ (Pika)
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Mật khẩu:** Bcrypt

## Cấu trúc thư mục

```
app/
├── core/               # JWT, MQTT, RabbitMQ
├── db/                 # Cấu hình kết nối CSDL
├── models/             # ORM Models (User, Device, SensorData,...)
├── observers/          # Observer Pattern (SensorSubject, Observers)
├── routes/             # API routers
├── schemas/            # Pydantic schemas (input/output)
├── services/           # Logic nghiệp vụ
├── utils/              # Cấu hình & tiện ích bảo mật
├── main.py             # FastAPI entrypoint
.env                    # Biến môi trường
requirements.txt        # Thư viện phụ thuộc
```

## Thiết lập dự án

### 1. Cài đặt thư viện

```
pip install -r requirements.txt
```

### 2. Thiết lập biến môi trường

Tạo file `.env`:

```
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=YoloHome

AIO_USERNAME=your_adafruit_username
AIO_KEY=your_adafruit_key

JWT_SECRET=your_jwt_secret
JWT_ALGORITHM=HS256
JWT_EXPIRE=3600

RABBITMQ_URL=amqp://guest:guest@localhost/
```

### 3. Tạo cơ sở dữ liệu

Sử dụng file SQL đã cung cấp [database.sql](sql/database.sql) chứa toàn bộ bảng.

### 4. Khởi chạy FastAPI

```
uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --log-config log_config.yaml
```

Hoặc chạy nền

```
nohup uvicorn app.main:app --host 0.0.0.0 --port 80 --reload --log-config log_config.yaml > uvicorn.log 2>&1 &
```

## API chính

- `POST /auth/signup`: Đăng ký tài khoản
- `POST /auth/signin`: Đăng nhập, trả về JWT
- `GET /api/device`: Lấy danh sách thiết bị của user
- `POST /api/device`: Thêm thiết bị mới
- `PATCH /api/device/{device_id}`: Cập nhật thiết bị
- `DELETE /api/device/{device_id}`: Xóa thiết bị
- `POST /api/sensor`: Ghi nhận dữ liệu cảm biến
- `GET /api/sensor`: Lấy dữ liệu mới nhất
- `GET /api/sensor/check-alert`: Kiểm tra cảnh báo gần nhất
- `GET /api/sensor/time-range`: Lấy dữ liệu theo khoảng thời gian (unix time)

Tất cả các API yêu cầu JWT thông qua `Authorization: Bearer <token>`.

## Frontend

Dự án giao diện người dùng (frontend) được xây dựng riêng và có thể được kết nối trực tiếp với backend thông qua các API đã cung cấp.

Repository: [https://github.com/HANND04/yolohome](https://github.com/HANND04/yolohome)

## Liên hệ

Trường Đại học Bách Khoa - ĐHQG TP.HCM  
Khoa Khoa học và Kỹ thuật Máy tính  
Đồ án môn học Đa ngành - CO3109 - HK242