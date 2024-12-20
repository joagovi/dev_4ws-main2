import serial.tools.list_ports
from sys import platform


def get_stm_ports():
    """Devuelve una lista de nombres de puertos seriales que contienen 'STM' en la descripción."""
    stm_ports = []
    ports = list(serial.tools.list_ports.comports())
    for port_no, description, address in ports:
        if 'STM' in description:
            stm_ports.append(port_no)
    return stm_ports

stm_ports = get_stm_ports()
print(stm_ports[1])