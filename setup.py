# OpenAssistant 0.01
# 2016 General Public License V3
# By Andrew Vavrek, Clayton G. Hobbs, Jezra

# setup.py - Initialization

from setuptools import setup

with open("README.rst") as file:
    long_description = file.read()

setup(
    name = "OpenAssistant",
    version = "0.01",
    author = "Andrew Vavrek, Clayton G. Hobbs, Jezra, Jonathan Kulp",
    author_email = "info@openassistant.org",
    description = ("Open Source AI Systems"),
    license = "GPLv3+",
    keywords = "ai personal assistant voice control command",
    url = "https://github.com/vavrek/openassistant",
    packages = ['OpenAssistant'],
    long_description = long_description,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later "
            "(GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Topic :: Open Source AI"
    ],
    install_requires=["requests"],
    data_files = [
        ("./img", ["icon_inactive.png", "icon.png",
            "./etc/commands.json"])
    ],
    entry_points = {
        "console_scripts": [
            "assist=bin.core:run"
        ]
    }
)
