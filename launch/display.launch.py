from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
import os


def generate_launch_description():

    pkg_path = FindPackageShare("robot_description").find("robot_description")
    urdf_file = os.path.join(pkg_path, "urdf", "my_robot.urdf")
    rviz_config = os.path.join(pkg_path, "rviz", "my_rviz_config.rviz")

    robot_description = Command(['cat ', urdf_file])

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),

        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui"
        ),

        Node(
            package="robot_description",
            executable="camera_tf",
            output="screen"
        ),


        Node(
            package='camera_tf_cpp',
            executable='camera_tf_node',
            name='camera_tf_broadcaster',
            output='screen'
        ),
     
        Node(
            package='camera_tf_cpp',
            executable='tf_listener_cpp',
            name='tf_listener',
            output='screen'
        ),

        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d", rviz_config],
            output="screen"
        ),

    ])