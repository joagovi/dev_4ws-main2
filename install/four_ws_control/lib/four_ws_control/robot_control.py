#!/usr/bin/python3
import math
import threading
import rclpy
import numpy as np
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

vel_msg = Twist()  # robot velosity
mode_selection = 0 # 1:opposite phase, 2:in-phase, 3:pivot turn 4: none
valor = 0.1  # Puedes cambiar este valor al que desees
vel_msg.linear.x = valor
vel_msg.angular.z = valor

class Commander(Node):

    def __init__(self):
        super().__init__('commander')
        timer_period = 0.02
        self.wheel_seperation = 0.122
        self.wheel_base = 0.156
        self.wheel_radius = 0.026
        self.wheel_steering_y_offset = 0.03
        self.steering_track = self.wheel_seperation - 2*self.wheel_steering_y_offset

        self.pos = np.array([0,0,0,0], float)
        self.vel = np.array([0,0,0,0], float) #left_front, right_front, left_rear, right_rear

        self.pub_pos = self.create_publisher(Float64MultiArray, '/forward_position_controller/commands', 10)
        self.pub_vel = self.create_publisher(Float64MultiArray, '/forward_velocity_controller/commands', 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        global vel_msg

        V = vel_msg.linear.x #vel_msg.linear.y
        #self.get_logger().info(f"Valor de V: {V}")

        frontSteerAngle = math.atan(vel_msg.angular.z* self.wheel_base / V)#vel_msg.angular.z* self.wheel_base / V)
        

        if frontSteerAngle > math.radians(60):
            frontSteerAngle = math.radians(60)
        elif frontSteerAngle < math.radians(-60):
            frontSteerAngle = math.radians(-60)

        rearSteerAngle = -frontSteerAngle

        epsilon = 1e-6
        #print( abs(frontSteerAngle) > epsilon )

        # Instantaneous Center of Rotation (ICR)
        R = (self.wheel_base) / (2 * math.tan(frontSteerAngle)) if abs(frontSteerAngle) > epsilon else float('inf')
        #print(2 * math.tan(frontSteerAngle))
        Ri = R - self.wheel_base/2
        Ro = R + self.wheel_base/2

        # Individual wheel steering angle
        self.pos[0]  = math.atan((self.wheel_base) / (2 * Ri))  # front wheel 1
        self.pos[1]  = math.atan((self.wheel_base) / (2 * Ro))  # front wheel 2
        self.pos[2]  = -self.pos[0]   # front wheel 3
        self.pos[3]  = -self.pos[1] # front wheel 4

        # Calculate wheel velocities
        if R == float('inf'):
            self.vel[0] = V / math.cos(self.pos[0] )
            self.vel[1]  = V / math.cos(self.pos[1] )
        else:
            self.vel[0]  = V * Ri / (R * math.cos(self.pos[0]))
            self.vel[1] = V * Ro / (R * math.cos(self.pos[1]))

        self.vel[2] = self.vel[0] 
        self.vel[3] = self.vel[1]
        #self.get_logger().info(f"Publicado: {self.vel}")
        #print('aqui')

        pos_array = Float64MultiArray(data=self.pos) 
        vel_array = Float64MultiArray(data=self.vel) 
        self.pub_pos.publish(pos_array)
        self.pub_vel.publish(vel_array)
        self.pos[:] = 0
        self.vel[:] = 0

class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('velocity_subscriber')

        # Suscribirse a los tópicos de velocidad lineal y angular, que publican un solo valor (tipo Float64)
        self.linear_subscription = self.create_subscription(
            Float32,
            '/cmd_vel/linear',
            self.linear_velocity_callback,
            10)

        self.angular_subscription = self.create_subscription(
            Float32,
            '/cmd_vel/angular',
            self.angular_velocity_callback,
            10)
        

    def linear_velocity_callback(self, msg):
        global vel_msg
        if(msg.data ==0):
            msg.data = 0.01
        self.get_logger().info(f"Valor de msg.data1 : {msg.data }")

        vel_msg.linear.x = msg.data  # Actualiza la velocidad lineal con el valor recibido

    def angular_velocity_callback(self, msg):
        global vel_msg
        if(msg.data ==0):
            msg.data = 0.01
        self.get_logger().info(f"Valor de msg.data2 : {msg.data }")
        vel_msg.angular.z = msg.data  # Actualiza la velocidad angular con el valor recibido
        

if __name__ == '__main__':
    rclpy.init(args=None)
    
    commander = Commander()
    velocity_subscriber = VelocitySubscriber()

    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(commander)
    executor.add_node(velocity_subscriber)

    executor_thread = threading.Thread(target=executor.spin, daemon=True)
    executor_thread.start()
    rate = commander.create_rate(2)
    try:
        while rclpy.ok():
            rate.sleep()
    except KeyboardInterrupt:
        pass
    
    rclpy.shutdown()
    executor_thread.join()


# #!/usr/bin/python3
# import math
# import threading
# import rclpy
# import numpy as np
# from rclpy.node import Node
# from std_msgs.msg import Float64MultiArray
# from geometry_msgs.msg import Twist
# from sensor_msgs.msg import Joy

# vel_msg = Twist()  # robot velosity
# mode_selection = 0 # 1:opposite phase, 2:in-phase, 3:pivot turn 4: none

# class Commander(Node):

#     def __init__(self):
#         super().__init__('commander')
#         timer_period = 0.02
#         self.wheel_seperation = 0.122
#         self.wheel_base = 0.156
#         self.wheel_radius = 0.026
#         self.wheel_steering_y_offset = 0.03
#         self.steering_track = self.wheel_seperation - 2*self.wheel_steering_y_offset

#         self.pos = np.array([0,0,0,0], float)
#         self.vel = np.array([0,0,0,0], float) #left_front, right_front, left_rear, right_rear

#         self.pub_pos = self.create_publisher(Float64MultiArray, '/forward_position_controller/commands', 10)
#         self.pub_vel = self.create_publisher(Float64MultiArray, '/forward_velocity_controller/commands', 10)
#         self.timer = self.create_timer(timer_period, self.timer_callback)

#     def timer_callback(self):
#         global vel_msg, mode_selection

#         # opposite phase
#         if(mode_selection == 1):
                  
#             # vel_steerring_offset = vel_msg.angular.z * self.wheel_steering_y_offset
#             # sign = np.sign(vel_msg.linear.x)

#             # self.vel[0] = sign*math.hypot(vel_msg.linear.x - vel_msg.angular.z*self.steering_track/2, vel_msg.angular.z*self.wheel_base/2) - vel_steerring_offset
#             # self.vel[1] = sign*math.hypot(vel_msg.linear.x + vel_msg.angular.z*self.steering_track/2, vel_msg.angular.z*self.wheel_base/2) + vel_steerring_offset
#             # self.vel[2] = sign*math.hypot(vel_msg.linear.x - vel_msg.angular.z*self.steering_track/2, vel_msg.angular.z*self.wheel_base/2) - vel_steerring_offset
#             # self.vel[3] = sign*math.hypot(vel_msg.linear.x + vel_msg.angular.z*self.steering_track/2, vel_msg.angular.z*self.wheel_base/2) + vel_steerring_offset

#             # self.pos[0] = math.atan(vel_msg.angular.z*self.wheel_base/(2*vel_msg.linear.x + vel_msg.angular.z*self.steering_track))
#             # self.pos[1] = math.atan(vel_msg.angular.z*self.wheel_base/(2*vel_msg.linear.x - vel_msg.angular.z*self.steering_track))
#             # self.pos[2] = -self.pos[0]
#             # self.pos[3] = -self.pos[1] 
            

            
#             #V = math.hypot(vel_msg.linear.x, vel_msg.linear.y)
#             V = vel_msg.linear.y
#             frontSteerAngle = math.atan(vel_msg.angular.z* self.wheel_base / V)

#             if frontSteerAngle > math.radians(60):
#                 frontSteerAngle = math.radians(60)
#             elif frontSteerAngle < math.radians(-60):
#                 frontSteerAngle = math.radians(-60)

#             rearSteerAngle = -frontSteerAngle

#             # Instantaneous Center of Rotation (ICR)
#             R = (self.wheel_base) / (2 * math.tan(frontSteerAngle)) if frontSteerAngle != 0 else float('inf')
#             Ri = R - self.wheel_base/2
#             Ro = R + self.wheel_base/2

#             # Individual wheel steering angle
#             self.pos[0]  = math.atan((self.wheel_base) / (2 * Ri))  # front wheel 1
#             self.pos[1]  = math.atan((self.wheel_base) / (2 * Ro))  # front wheel 2
#             self.pos[2]  = -self.pos[0]   # front wheel 3
#             self.pos[3]  = -self.pos[1] # front wheel 4

#             # Calculate wheel velocities
#             if R == float('inf'):
#                 self.vel[0] = V / math.cos(self.pos[0] )
#                 self.vel[1]  = V / math.cos(self.pos[1] )
#             else:
#                 self.vel[0]  = V * Ri / (R * math.cos(self.pos[0]))
#                 self.vel[1] = V * Ro / (R * math.cos(self.pos[1]))

#             self.vel[2] = self.vel[0] 
#             self.vel[3] = self.vel[1]

#         # in-phase
#         elif(mode_selection == 2):

#             V = math.hypot(vel_msg.linear.x, vel_msg.linear.y)
#             sign = np.sign(vel_msg.linear.x)
            
#             if(vel_msg.linear.x != 0):
#                 ang = vel_msg.linear.y / vel_msg.linear.x
#             else:
#                 ang = 0
            
#             self.pos[0] = math.atan(ang)
#             self.pos[1] = math.atan(ang)
#             self.pos[2] = self.pos[0]
#             self.pos[3] = self.pos[1]
            
#             self.vel[:] = sign*V
            
#         # pivot turn
#         elif(mode_selection == 3):

#             self.pos[0] = -math.atan(self.wheel_base/self.steering_track)
#             self.pos[1] = math.atan(self.wheel_base/self.steering_track)
#             self.pos[2] = math.atan(self.wheel_base/self.steering_track)
#             self.pos[3] = -math.atan(self.wheel_base/self.steering_track)
            
#             self.vel[0] = -vel_msg.angular.z
#             self.vel[1] = vel_msg.angular.z
#             self.vel[2] = self.vel[0]
#             self.vel[3] = self.vel[1]
#             #print('aqui')

#         #elif(mode_selection == 4):#no he hecho colcon y cambiar a mode_selection 3
#         else:

#             self.pos[:] = 0
#             self.vel[:] = 0

#         pos_array = Float64MultiArray(data=self.pos) 
#         vel_array = Float64MultiArray(data=self.vel) 
#         self.pub_pos.publish(pos_array)
#         self.pub_vel.publish(vel_array)
#         self.pos[:] = 0
#         self.vel[:] = 0

# class Joy_subscriber(Node):

#     def __init__(self):
#         super().__init__('joy_subscriber')
#         self.subscription = self.create_subscription(
#             Joy,
#             'joy',
#             self.listener_callback,
#             10)
#         self.subscription

#     def listener_callback(self, data):
#         global vel_msg, mode_selection

#         if(data.buttons[0] == 1):   # in-phase # A button of Xbox 360 controller
#             mode_selection = 2
#         elif(data.buttons[4] == 1): # opposite phase # LB button of Xbox 360 controller
#             mode_selection = 1
#         elif(data.buttons[5] == 1): # pivot turn # RB button of Xbox 360 controller
#             mode_selection = 3
#             #print("aqui1")
#         else:
#             mode_selection = 4

#         if(data.axes[0]==0):
#             data.axes[0] = 0.01
#         if(data.axes[1]==0):
#             data.axes[1] = 0.01

#         vel_msg.linear.x = data.axes[0]*7.5
#         vel_msg.linear.y = data.axes[1]*7.5
#         vel_msg.angular.z = data.axes[2]*10

# if __name__ == '__main__':
#     rclpy.init(args=None)
    
#     commander = Commander()
#     joy_subscriber = Joy_subscriber()

#     executor = rclpy.executors.MultiThreadedExecutor()
#     executor.add_node(commander)
#     executor.add_node(joy_subscriber)

#     executor_thread = threading.Thread(target=executor.spin, daemon=True)
#     executor_thread.start()
#     rate = commander.create_rate(2)
#     try:
#         while rclpy.ok():
#             rate.sleep()
#     except KeyboardInterrupt:
#         pass
    
#     rclpy.shutdown()
#     executor_thread.join()
