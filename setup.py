import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


config = {}
config["name"]             = "file_helper"
config["version"]          = "0.1.3"
config["author"]           = "Qevo"
config["author_email"]     = "qevo@qevonics.net"
config["description"]      = ("File search, identification, analysis, and manipulation tools.")
config["license"]          = "MIT"
config["keywords"]         = "file_system file_management files file"
config["url"]              = "https://github.com/qevo/py_file_helper"
config["packages"]         = ["file_helper"]
config["install_requires"] = ["data_helper"]
config["dependency_links"] = ["https://github.com/qevo/py_data_helper/tarball/master#egg=data-helper"]
config["long_description"] = read("README.md")
config["classifiers"]      = [
    "Development Status :: 3 - Alpha",
    "Topic :: Utilities",
    "License :: OSI Approved :: MIT License",
]

if __name__ == '__main__':
    setup(**config)
