from os import getenv
from subprocess import check_output

from setuptools import find_packages, setup

setup(
    name="neureal-tarot-api",
    author="Cheyenne Nelson",
    author_email="cnelsonn@picarro.com",
    install_requires=[
        "jinja2>=3.1",
        "fastapi>=0.92",
        "uvicorn[standard]>=0.20",
    ],
    python_requires=">=3.7",
)
