from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration

from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    map_yaml_file = LaunchConfiguration('map', default='/home/joaquin/dev_4ws/src/path_demo/maps/empty_map.yaml')

    # ... (otros nodos de Nav2 que ya tengas)

    # Nodo que publica la ruta aleatoria
    path_publisher_node = Node(
        package='path_demo', 
        executable='path_publisher_node',
        name='path_publisher_node',
        output='screen'
    )

    robot_pose_listener_node = Node(
        package='path_demo', 
        executable='robot_pose_listener',
        name='robot_pose_listener',
        output='screen'
    )

    kinematics_controller_node = Node(
        package='path_demo',  
        executable='kinematics_controller_node',
        name='kinematics_controller_node',
        output='screen'
    )
    

    # Map server con el mapa vacío de Nav2
    # map_server_node = Node(
    #     package='nav2_map_server',
    #     executable='map_server',
    #     name='map_server',
    #     output='screen',
    #     parameters=[{'use_sim_time': use_sim_time}, 
    #                 {'yaml_filename': map_yaml_file}]
    # )

    # ... (otros nodos de Nav2 que necesites)

    # Lanzar Gazebo con el archivo .world. 
    # Cargando un mundo vacio
    # gazebo = ExecuteProcess(
    #     cmd=['gazebo', '--verbose', 
    #         '-s', 'libgazebo_ros_init.so', 
    #         '-s', 'libgazebo_ros_factory.so', 
    #         '/home/siba/dev_4ws-main2/src/path_demo/world/world_4ws.world'],
    #     output='screen'
    # )

    # world_path = os.path.join(get_package_share_directory('path_demo'), 'worlds', 'basic_world.world')

    # # Configuración de Gazebo con el archivo .world
    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(
    #         get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    #     launch_arguments={'world': world_path}.items()
    # )


        # Nodo convertidor de trayectorias (PathConverterNode)
    path_visualizer= Node(
        package='path_demo',  # Asegúrate de que este sea el nombre correcto de tu paquete
        executable='path_visualizer',  # Asegúrate de que este sea el nombre de tu script de Python
        name='path_visualizer',
        output='screen'
    )


    return LaunchDescription([
        # ... (otros nodos de Nav2)
        path_publisher_node,
        robot_pose_listener_node,
        kinematics_controller_node,
        #map_server_node,  # Asegúrate de que map_server se lance antes de Gazebo
        # ... (otros nodos de Nav2)
        path_visualizer,
        #gazebo,  # Gazebo se lanza al final

    ])