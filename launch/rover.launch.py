import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, TimerAction

# this is the function launch  system will look for
def generate_launch_description():
    package_description = "rover_description"

    print("Fetching URDF ==>")
    #robot_desc_path = os.path.join(get_package_share_directory(package_description), "rover_desc", urdf_file)
    urdf_file = os.path.join(get_package_share_directory(package_description), 'rover_desc', 'rover.xacro')    #xacro_file = "urdfbot.xacro"
    urdf_content = Command(['xacro ', urdf_file])

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{
            'use_sim_time': True, 
            'robot_description': urdf_content,
        }],
        output="screen"
    )
    
    #joint state publisher: Publishes fake or gui-driven msgs for testing (joint_state_publisher_gui joint_state_publisher_gui)
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        parameters=[],        
        output="screen"
    )


    # create and return launch description object
    return LaunchDescription(
        [            
            robot_state_publisher_node,
            joint_state_publisher_gui_node,
        ]
    )
