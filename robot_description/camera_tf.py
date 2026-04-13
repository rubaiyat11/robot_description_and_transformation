import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster
import math

class CameraTf(Node):
    def __init__(self):
        super().__init__("camera_tf_broadcaster")

        self.br = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_tf)

        self.angle = 0.0

    def broadcast_tf(self):
        t = TransformStamped()
        t2 = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "wrist"
        t.child_frame_id = "camera_frame"
        
        t2.header.stamp = self.get_clock().now().to_msg()
        t2.header.frame_id = "camera_frame"
        t2.child_frame_id = "object_frame"

        self.angle += 0.05
        x = math.cos(self.angle)
        y = math.sin(self.angle)

        t2.transform.translation.x = x
        t2.transform.translation.y = y
        t2.transform.translation.z = 0.0
        
        t2.transform.rotation.x = 0.0
        t2.transform.rotation.y = 0.0
        t2.transform.rotation.z = 0.0
        t2.transform.rotation.w = 1.0

        t.transform.translation.x = 0.5
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.5

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.br.sendTransform(t)
        self.br.sendTransform(t2)


def main():
    rclpy.init()
    node= CameraTf()
    rclpy.spin(node)
    rclpy.shutdown()

    