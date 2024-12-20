from setuptools import setup

package_name = 'path_demo'  # Reemplaza con el nombre real de tu paquete

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Agrega esta línea para incluir los archivos de lanzamiento
        ('share/' + package_name + '/launch', ['launch/visualize_random_path.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tu_nombre',  # Reemplaza con tu nombre
    maintainer_email='tu_correo@ejemplo.com',  # Reemplaza con tu correo electrónico
    description='Paquete de demostración de trayectoria',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kinematics_controller_node = path_demo.kinematics_controller_node:main',
            'path_publisher_node = path_demo.path_publisher_node:main',
            'robot_pose_listener = path_demo.robot_pose_listener:main',
            'path_visualizer = path_demo.path_visualizer:main'
        ],
    },
)