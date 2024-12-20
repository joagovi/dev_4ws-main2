#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import serial
from modbus_tk import modbus_rtu
import modbus_tk
import time
from std_msgs.msg import Header
from mis_mensajes.msg import AngulosInclinacion

class ThreeImuNodes(Node):

    def __init__(self):
        super().__init__('three_imu_nodes')
        self.get_logger().info('Se inició el ThreeImuNodes.')
        self.timer = self.create_timer(0.1, self.publicar_datos)
        self.imu_pub1 = self.create_publisher(AngulosInclinacion, 'imu1_angulos', 10)
        self.imu_pub2 = self.create_publisher(AngulosInclinacion, 'imu2_angulos', 10)
        self.imu_pub3 = self.create_publisher(AngulosInclinacion, 'imu3_angulos', 10)

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

            msg1 = AngulosInclinacion()
            msg2 = AngulosInclinacion()
            msg3 = AngulosInclinacion()
            
            while rclpy.ok():
                try:
                    # Intentamos leer los registros del sensor
                    reg50 = self.master.execute(0x50, modbus_tk.defines.READ_HOLDING_REGISTERS, 52, 12)
                    
                    # Timestamp para la IMU 1
                    timestamp1 = self.get_clock().now().to_msg()

                    reg51 = self.master.execute(0x51, modbus_tk.defines.READ_HOLDING_REGISTERS, 52, 12)

                    # Timestamp para la IMU 2
                    timestamp2 = self.get_clock().now().to_msg()

                    reg52 = self.master.execute(0x52, modbus_tk.defines.READ_HOLDING_REGISTERS, 52, 12)

                    # Timestamp para la IMU 3
                    timestamp3 = self.get_clock().now().to_msg()

                except Exception as e:
                    self.get_logger().error(f'No se puede leer los registros: {e}')  # Mostrar el error específico
                    time.sleep(0.1) 

                else:  # Si se logra leer los registros, se publican los datos
                    # Conversión de registros a valores
                    v50 = [reg50[i] - 65536 if reg50[i] > 32767 else reg50[i] for i in range(12)]
                    v51 = [reg51[i] - 65536 if reg51[i] > 32767 else reg51[i] for i in range(12)]
                    v52 = [reg52[i] - 65536 if reg52[i] > 32767 else reg52[i] for i in range(12)]
                    
                    #  Ángulos de inclinación en grados (roll, pitch, yaw)
                    angulos_grados50 = [v50[i] / 32768.0 * 180 for i in range(9, 12)]
                    angulos_grados51 = [v51[i] / 32768.0 * 180 for i in range(9, 12)]
                    angulos_grados52 = [v52[i] / 32768.0 * 180 for i in range(9, 12)]

                    # Crear los mensajes personalizados
                    msg1 = AngulosInclinacion()
                    msg1.header = Header()
                    msg1.header.stamp = timestamp1
                    msg1.roll = angulos_grados50[0]
                    msg1.pitch = angulos_grados50[1]
                    msg1.yaw = angulos_grados50[2]

                    msg2 = AngulosInclinacion()
                    msg2.header = Header()
                    msg2.header.stamp = timestamp2
                    msg2.roll = angulos_grados51[0]
                    msg2.pitch = angulos_grados51[1]
                    msg2.yaw = angulos_grados51[2]

                    msg3 = AngulosInclinacion()
                    msg3.header = Header()
                    msg3.header.stamp = timestamp3
                    msg3.roll = angulos_grados52[0]
                    msg3.pitch = angulos_grados52[1]
                    msg3.yaw = angulos_grados52[2]

                    self.imu_pub1.publish(msg1)
                    self.imu_pub2.publish(msg2)
                    self.imu_pub3.publish(msg3)

def main(args=None):
    rclpy.init(args=args)
    node = ThreeImuNodes()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()