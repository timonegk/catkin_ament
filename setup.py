from setuptools import setup
from setuptools import find_packages

setup(
    name='catkin_ament',
    version='0.1.0',
    python_requires='>=3.5',
    packages=find_packages(exclude=['tests*', 'docs']),
    install_requires=['catkin-tools'],
    author='Timon Engelke',
    author_email='catkin@timonengelke.de',
    maintainer='Timon Engelke',
    maintainer_email='catkin@timonengelke.de',
    keywords=['catkin'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description="Ament support for catkin_tools",
    long_description="Provides support for the ament build system used in ROS2 for catkin_tools.",
    license='Apache 2.0',
    entry_points={
        'catkin_tools.jobs': [
            'ament_cmake = catkin_tools.jobs.cmake:description',
            'ament_python = catkin_ament.ament_python:description',
        ],
    },
)
