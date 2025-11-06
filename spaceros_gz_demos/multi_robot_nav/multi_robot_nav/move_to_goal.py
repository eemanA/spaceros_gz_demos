#!/usr/bin/env python3

import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist

import time
 
# Only the robots you actually spawned

ROBOTS = ['X2_a', 'X2_b', 'X2_c']
 
class MoveToGoal(Node):

    def __init__(self, ns):

        super().__init__(f'move_to_goal_{ns}')

        self.ns = ns

        self.pub = self.create_publisher(Twist, f'/{ns}/cmd_vel', 10)

        self.start_time = time.time()

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.get_logger().info(f"[{ns}] Motion controller active.")
 
    def timer_callback(self):

        msg = Twist()

        elapsed = time.time() - self.start_time
 
        if elapsed < 4.0:

            msg.linear.x = 8.0      # strong forward motion

            msg.angular.z = 0.0

        elif elapsed < 6.0:

            msg.linear.x = 0.0

            msg.angular.z = 1.2     # visible rotation

        else:

            msg.linear.x = 0.0

            msg.angular.z = 0.0

            self.timer.cancel()

            self.get_logger().info(f"[{self.ns}] Finished movement.")

        self.pub.publish(msg)
 
def main(args=None):

    rclpy.init(args=args)

    executor = rclpy.executors.MultiThreadedExecutor()

    nodes = [MoveToGoal(ns) for ns in ROBOTS]

    for node in nodes:

        executor.add_node(node)

    try:

        executor.spin()

    finally:

        for node in nodes:

            node.destroy_node()

        rclpy.shutdown()
 
if __name__ == '__main__':

    main()

 
 


