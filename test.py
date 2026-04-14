import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math, time

class JointCommandPublisher(Node):
    def __init__(self):
        super().__init__('joint_command_publisher')
        self.pub = self.create_publisher(JointState, '/joint_command', 10)
        self.timer = self.create_timer(0.02, self.publish)  # 50Hz
        self.t = 0.0

    def publish(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        
        msg.name = ['revolute_1'] 
        
        msg.position = [0.5 * math.sin(self.t)]
        msg.velocity = []
        msg.effort = []
        
        self.pub.publish(msg)
        self.t += 0.02

def main():
    rclpy.init()
    node = JointCommandPublisher()
    rclpy.spin(node)

if __name__ == '__main__':
    main()