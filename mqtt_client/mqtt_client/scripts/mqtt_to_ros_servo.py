# import paho.mqtt.client as mqtt
# import json
# import time

# # MQTT 브로커 설정
# BROKER_ADDRESS = "localhost"
# BROKER_PORT = 1883
# TOPIC = "/robot/servostream"

# client = mqtt.Client()
# client.connect(BROKER_ADDRESS, BROKER_PORT, 60)

# servostream_data = {
#     "pos": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#     "vel": [0.01, 0.02, 0.03, 0.04, 0.05, 0.06],
#     "acc": [0.001, 0.002, 0.003, 0.004, 0.005, 0.006],
#     "time": 1.5
# }

# try:
#     while True:
#         message = json.dumps(servostream_data)
#         client.publish(TOPIC, message)
#         print(f"Published: {message}")
#         time.sleep(5)  # 1초 간격으로 전송
# except KeyboardInterrupt:
#     print("MQTT Publisher stopped.")

#############################################################################

import paho.mqtt.client as mqtt
from rclpy.serialization import serialize_message
from dsr_msgs2.msg import ServojStream

# MQTT 브로커 설정
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "/robot/servostream"

# MQTT 클라이언트 설정
client = mqtt.Client()
client.connect(BROKER_ADDRESS, BROKER_PORT, 60)

# ROS 2 메시지 생성
ros_msg = ServojStream()
ros_msg.pos = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
ros_msg.vel = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
ros_msg.acc = [0.001, 0.002, 0.003, 0.004, 0.005, 0.006]
ros_msg.time = 1.5

try:
    while True:
        # 메시지 직렬화
        serialized_msg = serialize_message(ros_msg)

        # MQTT로 퍼블리시
        client.publish(TOPIC, serialized_msg)
        print(f"Published serialized message: {serialized_msg}")

except KeyboardInterrupt:
    print("MQTT Publisher stopped.")
