import rclpy
import math
from rclpy.node import Node

from tf2_ros import Buffer, TransformListener

class TFListener(Node):
    def __init__(self):
        super().__init__("tf_listener")

        self.tf_buffer = Buffer()

        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.timer = self.create_timer(0.5, self.lookup_transform)

    def lookup_transform(self):
        try:
            transform = self.tf_buffer.lookup_transform(
                "chassis",
                "object_frame",
                rclpy.time.Time()
            )

            t = transform.transform.translation

        
            self.get_logger().info(
                f"x={t.x:.2f}, y={t.y:.2f}, z={t.z:.2f}"
            )

            t2 = transform.transform.translation

        
            self.get_logger().info(
                f"x={t2.x:.2f}, y={t2.y:.2f}, z={t2.z:.2f}"
            )

            distance = math.sqrt(t.x**2 + t.y**2 + t.z**2)

            self.get_logger().info(
                f"Distance from base to object: {distance:.2f} m"
            )

            if distance < 2.7:
                self.get_logger().warn("STOP - obstacle too close")
            elif distance < 3.0:
                self.get_logger().info("Slow down")
            else:
                self.get_logger().info("Path clear")

        except Exception as e:
            self.get_logger().warn("Waiting for TF...")


def main():
    rclpy.init()
    node = TFListener()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()