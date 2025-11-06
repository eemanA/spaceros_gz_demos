from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
 
def generate_launch_description():
    # Path to your Nav2 params file
    nav2_params_path = os.path.join(
        os.getenv('HOME'),
        'spaceros_gz_demos',
        'nav2_bringup',
        'config',
        'nav2_params.yaml'
    )
 
    # Correct path to system Nav2 bringup file
    bringup_launch_path = os.path.join(
        '/opt/ros/humble/share/nav2_bringup/launch/bringup_launch.py'
    )
 
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(bringup_launch_path),
            launch_arguments={
    'use_sim_time': 'true',
    'params_file': nav2_params_path,
    'map': os.path.join(
        os.getenv('HOME'),
        'spaceros_gz_demos',
        'nav2_bringup',
        'maps',
        'map.yaml'
    )
}.items(),
        ),
    ])
