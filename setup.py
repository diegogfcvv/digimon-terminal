from setuptools import setup, find_packages
import os

# List all data files recursively
def find_data_files(package_dir, data_dir):
    data_files = []
    for root, dirs, files in os.walk(os.path.join(package_dir, data_dir)):
        for file in files:
            data_files.append(os.path.relpath(os.path.join(root, file), package_dir))
    return data_files

setup(
    name='digimon-terminal',
    version='1.1',
    packages=find_packages(),
package_data={
        'digimon': ['data/digimon_data/*/*'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'digimon=digimon.cli:main',
        ],
    },
    python_requires='>=3.6',
)