import rclpy
from rclpy.serialization import deserialize_message
from sensor_msgs.msg import CameraInfo
import paho.mqtt.client as mqtt
import json

# MQTT 브로커 정보
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "camera/info"

# ROS2 메시지 역직렬화 함수
def decode_camera_info(payload):
    try:
        # ROS2 메시지 역직렬화
        camera_info = deserialize_message(payload, CameraInfo)

        # 디코딩된 데이터를 JSON 형태로 변환
        camera_info_dict = {
            "header": {
                "stamp": {
                    "sec": camera_info.header.stamp.sec,
                    "nanosec": camera_info.header.stamp.nanosec
                },
                "frame_id": camera_info.header.frame_id
            },
            "height": camera_info.height,
            "width": camera_info.width,
            "distortion_model": camera_info.distortion_model,
            "D": list(camera_info.d),
            "K": list(camera_info.k),
            "R": list(camera_info.r),
            "P": list(camera_info.p),
            "binning_x": camera_info.binning_x,
            "binning_y": camera_info.binning_y,
            "roi": {
                "x_offset": camera_info.roi.x_offset,
                "y_offset": camera_info.roi.y_offset,
                "height": camera_info.roi.height,
                "width": camera_info.roi.width,
                "do_rectify": camera_info.roi.do_rectify
            }
        }
        return camera_info_dict
    except Exception as e:
        print(f"Failed to decode CameraInfo: {e}")
        return None

# MQTT 메시지 처리 함수
def on_message(client, userdata, message):
    try:
        payload = message.payload
        print(f"Received raw binary message (length {len(payload)}): {payload[:20]}...")

        # CameraInfo 메시지 디코딩
        camera_info = decode_camera_info(payload)

        if camera_info:
            print("Decoded CameraInfo message:")
            print(json.dumps(camera_info, indent=2))
        else:
            print("Failed to decode CameraInfo message.")

    except Exception as e:
        print(f"Error processing message: {e}")

# MQTT 클라이언트 설정
client = mqtt.Client()
client.on_message = on_message

# ROS2 초기화
rclpy.init()

# 브로커 연결 및 토픽 구독
client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
client.subscribe(TOPIC)

print(f"Subscribed to topic: {TOPIC}")
client.loop_forever()
