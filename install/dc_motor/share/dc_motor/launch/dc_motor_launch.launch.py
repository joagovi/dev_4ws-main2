from launch import LaunchDescription
from launch_ros.actions import Node
import serial.tools.list_ports

def get_stm_ports():
    """Devuelve una lista de nombres de puertos seriales que contienen 'STM' en la descripción."""
    stm_ports = []
    ports = list(serial.tools.list_ports.comports())
    for port_no, description, address in ports:
        if 'STM' in description:
            stm_ports.append(port_no)
    return stm_ports

def generate_launch_description():
    stm_ports = get_stm_ports()
    nodes = []
    topic_name = ['position_1', 'position_2', 'position_3', 'position_4']

    for i, port in enumerate(stm_ports):
        node = Node(
            package='dc_motor',  # Reemplaza con el nombre de tu paquete
            executable='dc_motor_node_v1',  # Reemplaza si el nombre de tu ejecutable es diferente
            name=f'dc_motor_node_{i+1}',
            output='screen',
            arguments=[port],
            parameters=[{'topic_name': topic_name[i]}],
        )
        nodes.append(node)

    return LaunchDescription(nodes)