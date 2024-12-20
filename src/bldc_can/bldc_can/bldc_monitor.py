#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Int32
import can  # Librería para comunicación CAN
import serial.tools.list_ports
from sys import platform
from std_msgs.msg import Header
from mis_mensajes.msg import MotorDatos

# Constantes para los IDs de los motores y comandos
CAN_PACKET_STATUS = 9
MOTOR_ID_1 = 0x0042
MOTOR_ID_2 = 0x0057
MOTOR_ID_3 = 0x0072
MOTOR_ID_4 = 0x0001

motor_ids = {
    'motor_1': MOTOR_ID_1,
    'motor_2': MOTOR_ID_2,
    'motor_3': MOTOR_ID_3,
    'motor_4': MOTOR_ID_4,
}

def check_motor_id(motor_id):
    return motor_id in motor_ids.values()

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

class CANHandler(Node):
    def __init__(self):
        super().__init__('can_handler')

        self.get_logger().info('Se inició lectura de 4 motores')
        #self.motor_pub = self.create_publisher(MotorDatos, 'motor1_datos', 10)

        self.publishers_ = {}

        for motor in motor_ids:
            self.publishers_[motor] = self.create_publisher(MotorDatos, f'{motor}_status', 10)

        # Configurar conexión al bus CAN
        try:
            self.bus = can.interface.Bus(bustype='slcan', channel=serial_ports_CAN(), bitrate=500000)
            self.get_logger().info("Connected to CAN bus.")
        except Exception as e:
            self.get_logger().error(f"Failed to connect to CAN bus: {e}")
            self.bus = None

        # Configurar temporizador para leer mensajes
        if self.bus:
            self.timer = self.create_timer(0.01, self.receive_publicar_datos)  # 10 Hz

    def receive_publicar_datos(self):
        """Recibe mensajes del bus CAN y los procesa."""
        try:
            message = self.bus.recv(timeout=0.1)  # Tiempo de espera de 100 ms
            timestamp1 = self.get_clock().now().to_msg()
            if message is not None:
                can_log_msg = f"ID: {message.arbitration_id.to_bytes(4, byteorder='big', signed=True).hex()}, Data: {message.data.hex()}"
                can_msg = f"{message.arbitration_id.to_bytes(4, byteorder='big', signed=True).hex()},{message.data.hex()}"
                self.get_logger().info(f"Received message: {can_log_msg}")
                self.process_can_message(can_msg,timestamp1)
        except can.CanError as e:
            self.get_logger().error(f"CAN Error: {e}")

    def process_can_message(self, can_msg,timestamp1):
        """Procesa el mensaje recibido del bus CAN."""
        msg_list = can_msg.split(",")
        if len(msg_list) != 2:
            self.get_logger().error("Invalid CAN message format.")
            return

        try:
            can_id = bytes.fromhex(msg_list[0])
            can_data = bytes.fromhex(msg_list[1])
        except ValueError as e:
            self.get_logger().error(f"Error parsing CAN message: {e}")
            return

        command_id = int.from_bytes(can_id[2:3], "big", signed=True)
        motor_id = int.from_bytes(can_id[3:4], "big", signed=True)

        if check_motor_id(motor_id):
            motor = list(motor_ids.keys())[list(motor_ids.values()).index(motor_id)]
            if command_id == CAN_PACKET_STATUS:
                rpm = int.from_bytes(can_data[0:4], "big", signed=True)
                current = int.from_bytes(can_data[4:6], "big", signed=True) / 10.0
                duty = int.from_bytes(can_data[6:8], "big", signed=True) / 1000.0

                motor_datos = MotorDatos()
                motor_datos.header = Header()
                motor_datos.header.stamp = timestamp1
                motor_datos.rpm = rpm
                motor_datos.current = current

                self.publishers_[motor].publish(motor_datos)


            #else:
                #self.get_logger().warning("Command Id not identified")
        else:
            self.get_logger().warning("Motor not identified")

def main(args=None):
    rclpy.init(args=args)
    can_handler = CANHandler()
    rclpy.spin(can_handler)
    can_handler.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
