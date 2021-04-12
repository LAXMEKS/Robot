#!/usr/bin/env python3


from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os


def generate_launch_description():
    stage = LaunchConfiguration('stage', default='4')

    saved_model_file_name = 'stage4_'
    saved_model = os.path.join(
        get_package_share_directory('turtlebot3_dqn'),
        'save_model',
        saved_model_file_name)

    return LaunchDescription([
        Node(
            package='turtlebot3_dqn',
            node_executable='turtlebot3_dqn',
            node_name='turtlebot3_dqn',
            output='screen',
            arguments=[saved_model]),

        Node(
            package='turtlebot3_dqn',
            node_executable='turtlebot3_moving_obstacle',
            node_name='turtlebot3_moving_obstacle2',
            output='screen'),

        Node(
            package='turtlebot3_dqn',
            node_executable='turtlebot3_graph',
            node_name='action_graph',
            output='screen'),

        Node(
            package='turtlebot3_dqn',
            node_executable='turtlebot3_graph',
            node_name='result_graph',
            output='screen'),
    ])
