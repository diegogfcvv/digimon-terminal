from setuptools import setup, find_packages

setup(
    name='digimon-terminal',
    version='1.0',
    packages=find_packages(),
    package_data={
        'digimon': ['data/*/*'],
    },
    entry_points={
        'console_scripts': [
            'digimon=digimon.cli:main',
        ],
    },
    python_requires='>=3.6',
)