# SPDX-FileCopyrightText: 2022 Shuichiro Fujisawa
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node
#import launch.actions
#import launch.substitutions
#import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription([
        test_talker(
            package='mypkg',
            executable='test_talker',
            )
        tra_listener(
            package='mypkg',
            executable='tra_listener',
            output='screen',
            )
        ])

    #return launch.LaunchDescription([talker, listener])
