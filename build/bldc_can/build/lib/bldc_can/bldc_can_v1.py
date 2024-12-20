#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray, String
import can
import serial.tools.list_ports
from sys import platform

CAN_PACKET_SET_DUTY = 0
CAN_PACKET_SET_CURRENT = 1
CAN_PACKET_SET_CURRENT_BRAKE = 2
CAN_PACKET_SET_RPM = 3
CAN_PACKET_SET_POS = 4
CAN_PACKET_SET_CURRENT_REL = 10
CAN_PACKET_SET_CURRENT_BRAKE_REL = 11
CAN_PACKET_SET_CURRENT_HANDBRAKE = 12
CAN_PACKET_SET_CURRENT_HANDBRAKE_REL = 13

CAN_PACKET_STATUS = 9
CAN_PACKET_STATUS_2 = 14
CAN_PACKET_STATUS_3 = 15
CAN_PACKET_STATUS_4 = 16
CAN_PACKET_STATUS_5 = 27
CAN_PACKET_STATUS_6 = 28

MOTOR_ID_1 = 0x0342
MOTOR_ID_2 = 0x0357
MOTOR_ID_3 = 0x0372 
MOTOR_ID_4 = 0x0301

# Identifica SO, se conecta al puerto indicado
if platform == 'linux' or platform == 'linux2':
    def serial_ports_CAN():
        ports = list(serial.tools.list_ports.comports())  
        for port_no, description, address in ports:
            if 'ACM' in description:
                return port_no
            if 'CAN' in description:
                return port_no
            if 'Serial' in description:
                return port_no
    print(serial_ports_CAN())

class CANNode(Node):
    def __init__(self):
        super().__init__('can_node')

        self.vesc_id_1 = MOTOR_ID_1
        self.vesc_id_2 = MOTOR_ID_2
        self.vesc_id_3 = MOTOR_ID_3 
        self.vesc_id_4 = MOTOR_ID_4

        # Initialize CAN bus
        self.bus = can.interface.Bus(bustype='slcan', channel=serial_ports_CAN(), bitrate=500000)

        # Subscription to listen to RPM messages
        self.subscription_ = self.create_subscription(
            Int32MultiArray,
            'bldc_motors/rpm',
            self.set_rpm_callback,
            10)

    def set_rpm_callback(self, msg):
        """Callback function to process received messages."""
        rpm1 = msg.data[0].to_bytes(4, byteorder="big", signed=True)
        rpm2 = msg.data[1].to_bytes(4, byteorder="big", signed=True)
        rpm3 = msg.data[2].to_bytes(4, byteorder="big", signed=True)
        rpm4 = msg.data[3].to_bytes(4, byteorder="big", signed=True)

        self.bus.send(can.Message(
           arbitration_id=self.vesc_id_1, data=rpm1, is_extended_id=True
        ))
        self.bus.send(can.Message(
           arbitration_id=self.vesc_id_2, data=rpm2, is_extended_id=True
        ))
        self.bus.send(can.Message(
            arbitration_id=self.vesc_id_3, data=rpm3, is_extended_id=True
        ))
        self.bus.send(can.Message(
           arbitration_id=self.vesc_id_4, data=rpm4, is_extended_id=True
        ))

def main(args=None):
    rclpy.init(args=args)
    can_node = CANNode()
    try:
        rclpy.spin(can_node)
    except KeyboardInterrupt:
        pass
    finally:
        can_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
