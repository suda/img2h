import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "img2h",
    version = "0.0.1",
    author = "Wojtek Siudzinski",
    author_email = "admin@suda.pl",
    description = ("Utility which converts bitmaps to C/C++ byte arrays "
                    "used in microcontrollers like Arduino on Spark Core/Photon."),
    license = "BSD",
    keywords = "bitmap bytearray arduino spark core photon wiring",
    url = "https://github.com/suda/img2h",
    modules = ['img2h'],
    entry_points = {
        'console_scripts': ['img2h=img2h.command_line:convert'],
    },
    install_requires=[
        'pillow',
        'click'
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
