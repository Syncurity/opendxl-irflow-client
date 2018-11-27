Library Installation
====================

Prerequisites
*************

* OpenDXL Python Client library installed
   `<https://github.com/opendxl/opendxl-client-python>`_

* The OpenDXL Python Client prerequisites must be satisfied
   `<https://opendxl.github.io/opendxl-client-python/pydoc/installation.html>`_

* The Syncurity IR-Flow OpenDXL Service
   `<https://github.com/Syncurity/opendxl-irflow-service>`_

* Python 3.4 or higher in the Python 3.x series installed within a Windows or Linux environment.

Installation
************

Use ``pip`` to automatically install the library:

    .. parsed-literal::

        pip install opendxl-irflow-client\ |version|\-py2.py3-none-any.whl

Or with:

    .. parsed-literal::

        pip install opendxl-irflow-client\ |version|\.zip

As an alternative (without PIP), unpack the irflowclient-\ |version|\.zip (located in the lib folder) and run the setup
script:

    .. parsed-literal::

        python setup.py install
