import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import numpy as np
from scipy.spatial.transform import Rotation as R

def bezier_curve(P0, P1, P2, P3, t):
    return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

def bezier_curve_derivative(P0, P1, P2, P3, t):
    return 3 * (1 - t)**2 * (P1 - P0) + 6 * (1 - t) * t * (P2 - P1) + 3 * t**2 * (P3 - P2)

def generate_random_path(start, end, num_points=500):
    P0 = np.array(start)
    P3 = np.array(end)
    P1 = P0 + np.random.rand(2) * (P3 - P0)
    P2 = P3 - np.random.rand(2) * (P3 - P0)

    t = np.linspace(0, 1, num_points)
    path = np.array([bezier_curve(P0, P1, P2, P3, ti) for ti in t])
    derivatives = np.array([bezier_curve_derivative(P0, P1, P2, P3, ti) for ti in t])

    xRef = path[:, 0]
    yRef = path[:, 1]
    thetaRef = np.arctan2(derivatives[:, 1], derivatives[:, 0])

    return xRef, yRef, thetaRef

class PathPublisherNode(Node):
    def __init__(self):
        super().__init__('path_publisher_node')

        # Crear el publicador de la trayectoria
        self.path_pub = self.create_publisher(Path, '/path_reference', 10)

        # Generar la trayectoria aleatoria
        start_point = (0, 0)
        end_point = (8, 8)
        self.xRef, self.yRef, self.thetaRef = generate_random_path(start_point, end_point)

        # Crear el mensaje Path una vez
        self.path_msg = Path()
        self.path_msg.header.frame_id = "world"  # Ajusta el frame_id según tu configuración
        self.path_msg.header.stamp = self.get_clock().now().to_msg()

        for x, y, theta in zip(self.xRef, self.yRef, self.thetaRef):
            pose_stamped = PoseStamped()
            pose_stamped.header.frame_id = "world"  # Ajusta el frame_id según tu configuración
            pose_stamped.header.stamp = self.get_clock().now().to_msg()
            pose_stamped.pose.position.x = x
            pose_stamped.pose.position.y = y
            pose_stamped.pose.position.z = 0.0 

            # Convertir el ángulo de Euler (theta) a un cuaternión
            quat = R.from_euler('z', theta).as_quat() 
            pose_stamped.pose.orientation.x = quat[0]
            pose_stamped.pose.orientation.y = quat[1]
            pose_stamped.pose.orientation.z = quat[2]
            pose_stamped.pose.orientation.w = quat[3]

            self.path_msg.poses.append(pose_stamped)

        self.publish_rate = 1.0  # 1 publicación por segundo
        self.timer = self.create_timer(60, self.publish_path)
        #self.timer = self.create_timer(1/self.publish_rate, self.publish_path)

        self.get_logger().info('Path publisher node initialized')

    def publish_path(self):
        """
        Publica la misma trayectoria pre-generada cada vez que se llama.
        """
        # Actualizar el timestamp del mensaje
        self.path_msg.header.stamp = self.get_clock().now().to_msg()

        # Publicar la trayectoria
        self.path_pub.publish(self.path_msg)
        #self.get_logger().info('Path published!')

def main(args=None):
    rclpy.init(args=args)

    path_publisher_node = PathPublisherNode()

    rclpy.spin(path_publisher_node)

    path_publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
