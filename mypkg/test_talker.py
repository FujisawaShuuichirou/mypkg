import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(String, "translation", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)
        #msg = String()
        #msg.data = input("ローマ字を入力して下し:")
        #self.pub.publish(msg)

    def cb(self):
        msg = String()
        msg.data = input()
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("test_talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
