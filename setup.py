from __future__ import absolute_import
import os
import distutils.command.sdist
from setuptools import setup
import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

VERSION_INFO = {}
CWD = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(CWD, "dxlirflowclient", "_version.py")) as f:
    exec(f.read(), VERSION_INFO)

setup(
    # Package name:
    name="dxlirflowclient",

    # Version number:
    version=VERSION_INFO["__version__"],

    # Package requirements
    install_requires=[
        "requests>=2.20.0",
        "irflow_client",
        "dxlbootstrap>=0.2.0",
        "dxlclient>=4.1.0.184"
    ],

    # Python version requirements
    python_requires=">=2.7.9,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",

    # Package author details:
    author="JP Bourget, Syncurity",

    # License
    license="Apache 2.0",

    # Keywords
    keywords=['security', 'syncurity', 'ir-flow', 'orchestration', 'opendxl', 'soar'],

    # Packages
    packages=[
        "dxlirflowclient",
        "dxlirflowclient._config",
        "dxlirflowclient._config.sample"],

    package_data={
        "dxlirflowclient._config.sample" : ['*']},

    # Details
    url="https://github.com/Syncurity/opendxl-irflow-client",

    description="opendxl_irflow_client",

    long_description=open('README').read(),

    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)
