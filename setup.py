"""Setup module."""

from setuptools import setup, find_packages
from os import path


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    # Name of Project
    # $ pip install RCJRVision
    # where it will live on PyPI: https://pypi.org/project/RCJRVision/
    name='RCJRVision',
    version='1.5',
    description='A fast and simple image processing method to detect H S U victims in rescue maze',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mhmmdshirazi/RCJRVision',
    author='Mohammad Mahdi Shirazi',
    author_email='mhmmdshirazi@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=['RCJRVision'],
    python_requires='>=3.5, <4',
    install_requires=get_requires(),
)
