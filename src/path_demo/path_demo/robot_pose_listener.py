import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose

class RobotPoseListener(Node):
    def __init__(self):
        super().__init__('robot_pose_listener')

        # Subscriber to /odom
        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        # Publisher for /actual_pose
        self.actual_pose_pub = self.create_publisher(Pose, '/actual_pose', 10)

        self.get_logger().info('Robot Pose Listener node initialized')

    def odom_callback(self, msg):
        """
        Callback to process the odometry message and republish the robot's pose.
        """
        # Create a Pose message
        pose_msg = Pose()

        # Extract position from the odometry message
        pose_msg.position = msg.pose.pose.position

        # Extract orientation from the odometry message
        pose_msg.orientation = msg.pose.pose.orientation

        # Publish the actual pose
        self.actual_pose_pub.publish(pose_msg)

def main(args=None):
    rclpy.init(args=args)
    robot_pose_listener = RobotPoseListener()
    rclpy.spin(robot_pose_listener)
    rclpy.shutdown()

if __name__ == '__main__':
    main()