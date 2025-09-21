from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ('share/' + package_name + '/launch', glob('launch/*.py')),
        # ('share/' + package_name + '/config', glob('config/*.yaml')),
        # ('share/' + package_name + '/worlds', glob('worlds/*.world')),
        # ('share/' + package_name + '/worlds', glob('description')),
         # Install launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Install config files
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        # Install worlds
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        # Install description files
        (os.path.join('share', package_name, 'description'), glob('description/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mostafa',
    maintainer_email='mostafa.m.abdulraheem@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
