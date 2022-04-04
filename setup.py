import os
from setuptools import (
    setup,
    find_packages
)

current_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_directory, 'README.md'), "r") as readme:
    package_description = readme.read()

setup(
    name="statserve",
    version="0.1.5",
    author="Sean Corbett",
    author_email="sean.corbett@umconnect.edu",
    description="Statserve is a microservices implementation of the statstream library.",
    long_description=package_description,
    long_description_content_type="text/markdown",
    url="https://github.com/scorbettUM/statserve",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'idna<2.10',
        'grpcio',
        'grpcio-tools',
        'stringcase',
        'packaging',
        'py3cli-tools',
        'easy-logger-py',
        'statstream-py'
    ],
    entry_points = {
        'statserve': 'statserve=statserve',
        'console_scripts': [
            'statserve-server=statserve.run:run',
            'statserve-stop=statserve.run:stop'
        ],
    },
    python_requires='>=3.8'
)
