from setuptools import setup

package_name = 'bldc_can'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joagovi',
    maintainer_email='joaquin.villarrealg@gmail.com',
    description='Un paquete ROS 2 para manejar mensajes CAN.',
    license='Licencia que prefieras',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'can_node = bldc_can.bldc_can_v1:main',  # Registra tu nodo aquí
            'can_monitor = bldc_can.bldc_monitor:main',
        ],
    },
)
