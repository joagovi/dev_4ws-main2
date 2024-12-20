import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
from nav_msgs.msg import Path
import numpy as np
from scipy.spatial.transform import Rotation as R

def kinematics_controller(controllerGain, actualPose, referencePose, maxSpeed, desSpeed, current_index):
    """
    Lyapunov-based nonlinear kinematics controller for a robot.

    Args:
        controllerGain: A list or numpy array containing the controller gains [k1, k2, k3].
        actualPose: A list or numpy array representing the current pose of the robot [x, y, theta].
        referencePose: A numpy array representing the reference poses (waypoints) for the robot.
        maxSpeed: A list or numpy array specifying the maximum linear and angular velocities [max_v, max_w].
        desSpeed: A list or numpy array specifying the desired linear and angular velocities [des_v, des_w].
        i: The index of the current reference pose (waypoint).

    Returns:
        v: The calculated linear velocity for the robot.
        w: The calculated angular velocity for the robot.
        i: The updated index of the reference pose.
        xn: ... (unclear from the provided code, likely an intermediate calculation)
        ye: The lateral error in the robot's frame.
        thetae: The orientation error in the robot's frame.
    """
    i= current_index
    # Numerical Singularity tolerance
    numsingTolerance = 1e-3

    # Maximum velocity and omega
    maximumVelocity = maxSpeed[0]
    maximumOmega = maxSpeed[1]

    # Desired velocity and omega
    desiredVelocity = desSpeed[0]
    desiredOmega = desSpeed[1]

    # Extracting x, y, theta from actualPose
    xAct, yAct, thetaAct = actualPose

    # Extracting x, y, theta from referencePose
    xRef = referencePose[:, 0]
    yRef = referencePose[:, 1]
    thetaRef = referencePose[:, 2]

    # Controller Gain
    k1, k2, k3 = controllerGain

    # Reset index if it reaches the end
    if i == len(xRef):
        i = 1

    # Waypoints setup (calculate xn)
    if i == 1 or i == len(xRef):
        xn = (xAct - xRef[i]) * np.cos(thetaRef[i]) + (yAct - yRef[i]) * np.sin(thetaRef[i])
    else:
        xn = (xAct - xRef[i]) * np.cos((thetaRef[i] + thetaRef[i - 1]) / 2) + (yAct - yRef[i]) * np.sin((thetaRef[i] + thetaRef[i - 1]) / 2)

    # Error Calculation
    if xn < 0:
        xe = (xRef[i] - xAct) * np.cos(thetaAct) + (yRef[i] - yAct) * np.sin(thetaAct)
        ye = -(xRef[i] - xAct) * np.sin(thetaAct) + (yRef[i] - yAct) * np.cos(thetaAct)
        thetae = thetaRef[i] - thetaAct
    else:
        if i < len(xRef)-1:
            i += 1
        else:
            i = len(xRef)-1
        xe = (xRef[i] - xAct) * np.cos(thetaAct) + (yRef[i] - yAct) * np.sin(thetaAct)
        ye = -(xRef[i] - xAct) * np.sin(thetaAct) + (yRef[i] - yAct) * np.cos(thetaAct)
        thetae = thetaRef[i] - thetaAct

    # Lyapunov Controller Output (calculate v)
    v = k1 * xe + desiredVelocity * np.cos(thetae)
    v = np.clip(v, -maximumVelocity, maximumVelocity)  # Limit v within max bounds

    # Calculate w
    w = (1 / k2) * ye * desiredVelocity + k3 * np.sin(thetae) + desiredOmega
    w = np.clip(w, -maximumOmega, maximumOmega)  # Limit w within max bounds

    # Global Frame Error (calculate xE) - This part seems incomplete in the MATLAB code
    if i == 1 or i == 2:  # Assuming you meant 2 here, as `length(xRef)` wouldn't make sense in this context
        xE = xRef[i] - xAct
    else:
        xE = xRef[i - 2] - xAct

    return v, w, i, xn, ye, thetae

class KinematicsControllerNode(Node):

    def __init__(self):
        super().__init__('kinematics_controller_node')

        # Parámetros del controlador
        self.controller_gain = np.array([0.1*15, 0.2*15, 0.6*15])
        self.max_speed = np.array([15, 2])  # m/s, rad/s
        self.des_speed = np.array([10, 0.0])  # m/s, rad/s

        # Suscriptor a la trayectoria de referencia
        self.path_sub = self.create_subscription(
            Path,
            '/path_reference',
            self.path_callback,
            10
        )

        # Suscriptor para la pose actual del robot
        self.actual_pose_sub = self.create_subscription(
            Pose,
            '/actual_pose',
            self.actual_pose_callback,
            10 
        )

        # Publicadores para las velocidades de control
        self.linear_vel_pub = self.create_publisher(Float32, '/cmd_vel/linear', 10)
        self.angular_vel_pub = self.create_publisher(Float32, '/cmd_vel/angular', 10)

        # Variable para almacenar la pose de referencia
        self.reference_pose = None

        # Índice de la pose de referencia actual
        self.current_index = 0

        self.get_logger().info('Kinematics controller node initialized')

    def path_callback(self, msg):
        """
        Callback para procesar la trayectoria recibida.
        """
        #print('hola')
        self.reference_pose = np.array([[
             pose.pose.position.x,
             pose.pose.position.y,
             R.from_quat([
                 pose.pose.orientation.x, 
                 pose.pose.orientation.y, 
                 pose.pose.orientation.z, 
                 pose.pose.orientation.w
             ]).as_euler('zyx')[0]  # Extraer el ángulo de yaw del cuaternión
         ] for pose in msg.poses])

    def actual_pose_callback(self, msg):
        """
        Callback para procesar la pose actual del robot.
        """
        #print(self.reference_pose)
        if self.reference_pose is not None:
            actual_pose = np.array([
                 msg.position.x, 
                 msg.position.y, 
                 R.from_quat([
                     msg.orientation.x, 
                     msg.orientation.y, 
                     msg.orientation.z, 
                     msg.orientation.w
                 ]).as_euler('zyx')[0]
             ]) 
            v, w, self.current_index, _, _, _ = kinematics_controller(
                self.controller_gain, actual_pose, self.reference_pose, self.max_speed, self.des_speed, self.current_index
            )

            # Publicar las velocidades de control
            linear_vel_msg = Float32()
            linear_vel_msg.data = v
            self.linear_vel_pub.publish(linear_vel_msg)

            angular_vel_msg = Float32()
            angular_vel_msg.data = w
            self.angular_vel_pub.publish(angular_vel_msg)

def main(args=None):
    rclpy.init(args=args)

    kinematics_controller_node = KinematicsControllerNode()

    rclpy.spin(kinematics_controller_node)

    kinematics_controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()