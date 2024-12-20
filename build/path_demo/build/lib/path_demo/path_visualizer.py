import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import SpawnEntity, DeleteEntity
import math

class PathToGroundModel(Node):
    def __init__(self):
        super().__init__('path_to_ground_model')
        self.subscription = self.create_subscription(Path, 'path_reference', self.path_callback, 10)
        self.spawn_client = self.create_client(SpawnEntity, '/spawn_entity')
        self.delete_client = self.create_client(DeleteEntity, '/delete_entity')
        
        # Esperar hasta que los servicios /spawn_entity y /delete_entity estén disponibles
        while not self.spawn_client.wait_for_service(timeout_sec=1.0) or not self.delete_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando los servicios de Gazebo...')
        
        self.current_model_name = None

    def path_callback(self, msg):
        # Si hay un modelo anterior, eliminarlo antes de generar uno nuevo
        if self.current_model_name:
            self.delete_previous_model()

        # Generar un nombre único para el nuevo modelo
        self.current_model_name = f"path_model_{self.get_clock().now().to_msg().sec}"

        if len(msg.poses) < 2:
            self.get_logger().info("La ruta no tiene suficientes puntos para generar una línea continua.")
            return

        sdf_model = f"""<sdf version="1.6">
                         <model name='{self.current_model_name}'>
                           <static>true</static>
        """
        # Construir el SDF añadiendo visuales planos entre los puntos
        for i in range(len(msg.poses) - 1):
            start = msg.poses[i].pose.position
            end = msg.poses[i + 1].pose.position

            # Calcular la posición media entre los dos puntos
            mid_x = (start.x + end.x) / 2.0
            mid_y = (start.y + end.y) / 2.0
            mid_z = 0.01  # Asegurar que esté muy cerca del suelo

            # Calcular la longitud entre los dos puntos
            length = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)

            # Calcular el ángulo de orientación para que se alinee con la dirección de la trayectoria
            yaw = math.atan2(end.y - start.y, end.x - start.x)

            if length == 0:
                continue

            # Añadir un plano en el SDF para representar la ruta en el suelo
            sdf_model += f"""
                           <link name='link_{i}'>
                             <pose>{mid_x} {mid_y} {mid_z} 0 0 {yaw}</pose>
                             <visual name='visual_{i}'>
                               <geometry>
                                 <plane>
                                   <normal>0 0 1</normal> <!-- El plano está en el suelo -->
                                   <size>{length} 0.1</size> <!-- Un plano muy delgado -->
                                 </plane>
                               </geometry>
                               <material>
                                 <ambient>0 1 0 1</ambient> <!-- Color verde -->
                               </material>
                               <cast_shadows>false</cast_shadows> <!-- No proyecta sombras -->
                             </visual>
                           </link>
            """

        # Cerrar el modelo SDF
        sdf_model += """    </model>
                         </sdf>
        """

        # Preparar la solicitud de SpawnEntity para el modelo con la nueva ruta
        request = SpawnEntity.Request()
        request.name = self.current_model_name
        request.xml = sdf_model
        request.robot_namespace = 'route_model'
        request.initial_pose = Pose()  # Pose inicial en (0,0,0)
        request.reference_frame = 'world'

        # Llamada al servicio para spawnear el modelo en Gazebo
        self.spawn_client.call_async(request)

    def delete_previous_model(self):
        # Llamada al servicio para eliminar el modelo anterior
        delete_request = DeleteEntity.Request()
        delete_request.name = self.current_model_name
        self.delete_client.call_async(delete_request)

def main(args=None):
    rclpy.init(args=args)
    node = PathToGroundModel()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
