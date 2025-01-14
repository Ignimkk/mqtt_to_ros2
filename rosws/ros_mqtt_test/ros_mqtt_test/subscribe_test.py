
import rclpy
from rclpy.node import Node
import json
from std_msgs.msg import String

class JsonSubscriber(Node):
    def __init__(self):
        super().__init__('json_subscriber')
        self.subscription = self.create_subscription(
            String,
            '/pong/primitive',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        try:
            # JSON 문자열을 파싱
            data = json.loads(msg.data)
            self.get_logger().info(f"Received JSON: {data}")
        except json.JSONDecodeError as e:
            self.get_logger().error(f"Failed to parse JSON: {e}")

def main(args=None):
    rclpy.init(args=args)
    json_subscriber = JsonSubscriber()
    rclpy.spin(json_subscriber)
    json_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
