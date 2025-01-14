# import rclpy
# from rclpy.node import Node
# from dsr_msgs2.msg import ServojStream
# import json
# from rclpy.serialization import deserialize_message
# from std_msgs.msg import String
# class ServojStreamSubscriber(Node):
#     def __init__(self):
#         super().__init__('servoj_stream_subscriber')
#         self.subscription = self.create_subscription(
#             String,
#             '/servoj_stream',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning

#     def listener_callback(self, msg):
#         try:
#             data = json.loads(msg.data)

#             ros_msg = ServojStream()
#             ros_msg.pos = data['pos']
#             ros_msg.vel = data['vel']
#             ros_msg.acc = data['acc']
#             ros_msg.time = data['time']

#             # ROS 2 메시지를 퍼블리시
#             self.get_logger().info(f"Published ROS 2 message: {ros_msg}")

#         except json.JSONDecodeError as e:
#             self.get_logger().error(f"JSON Decode Error: {e}")
#         except KeyError as e:
#             self.get_logger().error(f"Key Error: {e}")
#         except Exception as e:
#             self.get_logger().error(f"Unexpected Error: {e}")

# def main(args=None):
#     rclpy.init(args=args)
#     node = ServojStreamSubscriber()
#     try:
#         rclpy.spin(node)
#     except KeyboardInterrupt:
#         pass
#     finally:
#         node.destroy_node()
#         rclpy.shutdown()

# if __name__ == '__main__':
#     main()
##std_msgs/msg/String

################################################################

import rclpy
from rclpy.node import Node
from dsr_msgs2.msg import ServojStream

class ServojStreamSubscriber(Node):
    def __init__(self):
        super().__init__('servoj_stream_subscriber')

        # ROS 2 토픽 구독
        self.subscription = self.create_subscription(
            ServojStream,  
            '/servoj_stream',  
            self.listener_callback,  
            10
        )
        self.subscription 

    def listener_callback(self, msg):
        try:
            self.get_logger().info(f"Received message: pos={msg.pos}, vel={msg.vel}, acc={msg.acc}, time={msg.time}")
        except Exception as e:
            self.get_logger().error(f"Unexpected Error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = ServojStreamSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
