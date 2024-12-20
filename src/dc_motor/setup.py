from setuptools import setup
from glob import glob  # Importa la función glob

package_name = 'dc_motor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),  # Agrega esta línea
    ],
    install_requires=['setuptools'],
                      #'rclpy',
                      #'std_msgs',],
                      #'std_srvs'],
    zip_safe=True,
    maintainer='siba',
    maintainer_email='joagovi@hotmail.com',
    description='TODO: Package description',  # Actualiza la descripción
    license='TODO: License declaration',  # Actualiza la licencia
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dc_motor_node_v1 = dc_motor.dc_motor_node_v1:main'  # Ajusta la ruta al archivo
        ],
    },
)