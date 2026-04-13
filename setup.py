from setuptools import find_packages, setup

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/robot_description/launch', ['launch/display.launch.py']),
        ('share/robot_description/urdf', ['urdf/my_robot.urdf']),
        ('share/robot_description/rviz', ['rviz/my_rviz_config.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nemo',
    maintainer_email='nemo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "camera_tf = robot_description.camera_tf:main",
            "tf_listener = robot_description.tf_listener:main"
        ],
    },
)
