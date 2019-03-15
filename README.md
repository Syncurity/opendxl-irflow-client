# Syncurity IR-Flow DXL Python Client Library
[![OpenDXL Bootstrap](https://img.shields.io/badge/Built%20With-OpenDXL%20Bootstrap-blue.svg)](https://github.com/opendxl/opendxl-bootstrap-python)
# [![Latest PyPI Version](https://img.shields.io/pypi/v/dxltieclient.svg)](https://pypi.python.org/pypi/dxlirflowservice)

## Overview

The Syncurity IR-Flow DXL Python client library provides a high level wrapper for invoking Syncurity IR-Flow API calls via the Data Exchange Layer Fabric
IR-Flow via the DXL fabric.

The purpose of this service is to allow users to invoke IR-Flow remote commands via the DXL fabric.

A single IR-Flow service can connect to a single IR-Flow instance to provide access to the remote API endpoints exposed by IR-Flow.

DXL clients can invoke ePO remote commands by sending DXL request messages via the DXL fabric. The IR-Flow DXL service handles incoming request messages and forwards them to the appropriate ePO server via secure HTTP. Responses received from the IR-Flow server are packaged by the IR-Flow DXL service as DXL response messages and sent back to the invoking DXL client.

## Documentation

Documentation is supplied in the README links found after extracting the release.zip file on the releases page of this repo.

## Installation

* Download the Latest Release
* Extract the release .zip file
* View the README.html file located at the root of the extracted files.
* The README links to the documentation which includes installation instructions, API details, and samples.


## Bugs and Feedback

For bugs, questions and feedback please use github issues in this repo. 

## LICENSE

Copyright 2019

Apache 2.0
