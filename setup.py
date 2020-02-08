from setuptools import setup, find_packages
import ImageRobot

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name                    = "ImageRobot",
    version                 = ImageRobot.__version__,
    packages                = find_packages(),
    author                  = "Rouyan Thi",
    author_email            = "rouyanthi@gmail.com",
    description             = "A library used to do image recognition.",
    long_description        = open('README.md').read(),
    include_package_data    = True,
    classifiers             = [
                                "Programming Language :: Python",
                                "Development Status :: 1 - Planning",
                                "Natural Language :: English",
                                "Operating System :: OS Independent",
                                "Programming Language :: Python :: 3.7",
                            ],
    install_requires        = requirements,
)
