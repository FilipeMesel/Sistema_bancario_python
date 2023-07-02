from setuptools import setup, find_packages

setup(
    name='Cliente',
    version='0.0.1',
    description='Módulo que representa a classe Cliente do sistema bancário',
    packages=find_packages(),
    install_requires=[
        'datetime',
    ],
)
