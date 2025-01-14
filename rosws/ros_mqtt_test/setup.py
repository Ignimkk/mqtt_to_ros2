from setuptools import find_packages, setup

package_name = 'ros_mqtt_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mk',
    maintainer_email='kmingi98@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros_mqtt_test = ros_mqtt_test.subscribe_test:main',
            'mqtt_to_ros_servoj = ros_mqtt_test.mqtt_to_ros_servoj:main',

        ],
    },
)
