import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


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
