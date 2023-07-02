from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name='Cliente',
    version='0.0.2',
    description='Módulo que representa a classe Cliente do sistema bancário',
    long_description=page_description,
    packages=find_packages(),
    install_requires=[
        'datetime',
    ],
)
