# SPDX-FileCopyrightText: 2022 Shuichiro Fujisawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    #global doub
    node.get_logger().info("Listen: %d" % msg.data)
    #doub += msg.data
    #print(doub)

#doub = 0
rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
