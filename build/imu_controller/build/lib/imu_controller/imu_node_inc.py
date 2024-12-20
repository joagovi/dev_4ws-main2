#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import serial
from modbus_tk import modbus_rtu
import modbus_tk
import math
import time
from std_msgs.msg import Header
from mis_mensajes.msg import AngulosInclinacion  # Importa el mensaje personalizado

class ImuNode(Node):

    def __init__(self):
        super().__init__('imu_node')
        self.get_logger().info('Se inició el ImuNode.')
        self.timer = self.create_timer(0.1, self.publicar_datos)
        self.imu_pub = self.create_publisher(AngulosInclinacion, 'angulos_inclinacion', 10)  # Publicador para el mensaje personalizado

    def publicar_datos(self):
        try:
            self.wt_imu = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=0.5)
            if self.wt_imu.isOpen():
                self.get_logger().info('Puerto abierto.')
            else:
                self.wt_imu.open()
                self.get_logger().info('Puerto abierto.')

        except Exception as e:
            self.get_logger().info('Error al abrir el puerto. No está disponible el puerto /dev/ttyUSB0.')
            print(e)
            exit()
            
        else:
            self.master = modbus_rtu.RtuMaster(self.wt_imu)
            self.master.set_timeout(1)
            self.master.set_verbose(True)

            msg = AngulosInclinacion()  # Crea un mensaje de tipo AngulosInclinacion
            
            while rclpy.ok():
                try: 
                    reg = self.master.execute(0x52, modbus_tk.defines.READ_HOLDING_REGISTERS, 52, 12)

                except Exception as e:
                    self.get_logger().info('No se puede leer los registros.')
                    print(e)
                    time.sleep(0.1) 

                else:
                    # Conversión de registros a valores
                    v = [0]*12
                    for i in range(12):
                        if (reg[i]>32767):
                            v[i]=reg[i]-65536
                        else:
                            v[i]=reg[i]
                    
                    #  Ángulos de inclinación en grados (roll, pitch, yaw)
                    angulos_grados = [v[i] / 32768.0 * 180 for i in range(9, 12)]

                    # Crear el mensaje personalizado
                    msg = AngulosInclinacion()
                    msg.header = Header()
                    msg.header.stamp = self.get_clock().now().to_msg()
                    msg.roll = angulos_grados[0]
                    msg.pitch = angulos_grados[1]
                    msg.yaw = angulos_grados[2]

                    self.imu_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ImuNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()