#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    world_file_name = '4ws_world.model'
    world = os.path.join(get_package_share_directory('gazebo_simulation'),
                         'worlds', world_file_name)
    launch_file_dir = os.path.join(get_package_share_directory('gazebo_simulation'), 'launch')

    sdf_file_name = 'rs_robot/rs_robot.sdf'
    sdf = os.path.join(
        get_package_share_directory('gazebo_simulation'),  # Nombre del paquete
        'models',  # Directorio donde está ubicado el SDF
        sdf_file_name  # Nombre del archivo SDF
    )

    urdf_file_name = 'rs_robot.urdf'
    urdf = os.path.join(get_package_share_directory('gazebo_simulation'), 'urdf', urdf_file_name)

    yaml_file_name = 'rs_robot/config/controllers.yaml'
    yaml = os.path.join(get_package_share_directory('gazebo_simulation'), 'models', yaml_file_name)


    #Obtén la ruta al directorio del paquete
    package_dir = get_package_share_directory('gazebo_simulation')

    # Construye las rutas a los archivos necesarios
    urdf_file = os.path.join(package_dir, 'urdf', 'rs_robot.urdf')
    controllers_config = os.path.join(package_dir, 'models', 'rs_robot', 'config', 'controllers.yaml')

    # Carga el contenido del archivo URDF
    with open(urdf_file, 'r') as file:
        robot_description_content = file.read()

    # Parámetros para los nodos
    robot_description = {'robot_description': robot_description_content}

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_four_ws_control = get_package_share_directory('four_ws_control')

    # controller_manager = Node(
    #     package="controller_manager",
    #     executable="ros2_control_node",
    #     parameters=[
    #         robot_description,
    #         {"use_sim_time": True},
    #         controllers_config
    #     ],
    #     output="screen",
    # )

    # gzserver = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource(
    #             os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
    #         ),
    #         launch_arguments={'world': world}.items(),
    #     )

    # gzclient = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource(
    #             os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
    #         ),
    #     )

    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    #     ]),
    #     launch_arguments={
    #         'use_sim_time': LaunchConfiguration('use_sim_time')
    #     }.items()
    # )

    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true'
    )
    

    # Configura el lanzamiento de Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={
            'use_sim_time': 'true'  # Establece directamente como 'true'
        }.items()
    )

    
    controller = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_four_ws_control, 'launch', 'four_ws_control.launch.py')
            ),
            launch_arguments={'use_sim_time': use_sim_time}.items(),
        )
        
    
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'rs_robot',
            '-file', sdf,
            '-x', '0',
            '-y', '0',
            '-z', '0.2',
            '--ros-args',
            '-p', 'use_sim_time:=true'
        ],
        output='screen'
    )

    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([launch_file_dir, '/robot_state_publisher.launch.py']),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )
    

    # Publicar una transformación estática entre `world` y `base_footprint`
    # static_transform_publisher = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',
    #     name='static_transform_publisher',
    #     output='screen',
    #     arguments=['0', '0', '0', '0', '0', '0', 'world', 'base_footprint']  # Ajusta según tu frame
    # )

    # controller_manager_node = Node(
    #     package='controller_manager',
    #     executable='ros2_control_node',
    #     parameters=[{
    #         'robot_description': robot_desc,  # Pasa la descripción del robot aquí
    #     }, os.path.join(get_package_share_directory('gazebo_simulation'), 'models', 'rs_robot', 'config', 'controllers.yaml')],
    #     output='screen'
    # )

    forward_position_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'forward_position_controller'],
        output='screen', additional_env={'use_sim_time': 'true'}
    )

    forward_velocity_controller = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'forward_velocity_controller'],
        output='screen', additional_env={'use_sim_time': 'true'}
    )

    joint_state_broadcaster = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'joint_state_broadcaster'],
        output='screen', additional_env={'use_sim_time': 'true'}
    )

    joy_node = Node(
        package="joy",
        executable="joy_node",
        parameters=[{'use_sim_time': use_sim_time}]  # Agrega esta línea
    )

    nodes = [
        # gzserver,
        # gzclient,
        use_sim_time_arg,
        gazebo,
        spawn_entity,
        robot_state_publisher,
        #static_transform_publisher,  # Añadido aquí
        joy_node,
        #controller_manager,
        controller,
        forward_position_controller,
        forward_velocity_controller,
        joint_state_broadcaster
    ]

    return LaunchDescription(nodes)
