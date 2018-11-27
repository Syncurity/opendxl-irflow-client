Basic Search Sample
===================

This sample executes a `Syncurity IR-Flow API` request to create a new alert.

Prerequisites
*************
* The samples configuration step has been completed (see :doc:`sampleconfig`)
* An IR-Flow Service is available on the DXL fabric

Running
*******

To run this sample execute the ``sample/basic/basic_search_example.py`` script as follows:

    .. parsed-literal::

        /opendxl-irflow-client/ |version|/>python sample/basic/irflow_create_alert.py

The output should appear similar to the following:

    .. code-block:: python

        Response for irflow_service_create_alert:
        Created IR-Flow Alert ID: '110405'

        alert_num: 110405
        fact_group_id: 931810
        message: Alert Created
        score: 45.00
        success: True

Details
*******

The majority of the sample code is shown below:

    .. code-block:: python

        with DxlClient(config) as client:

            # Connect to the fabric
            client.connect()

            logger.info("Connected to DXL fabric.")

            # Send request that will trigger request callback 'irflow_service_create_alert'
            request_topic = "/syncurity/service/irflow_api/create_alert"
            req = Request(request_topic)

            # Create dictionary payload with host to lookup and response format
            # eventType is Incoming Data Field Group in IR-Flow
            req_dict = {
                        "sourceHostName": "irflow-test.syncurity.net",
                        "sourceAddress": "10.0.10.20",
                        "eventType": "openDXL fabric alert",
                        "description": "DXL Payload"
                        }

            # Convert dictionary to JSON and set as DXL request payload
            MessageUtils.dict_to_json_payload(req, req_dict)

            # Fire Away
            res = client.sync_request(req, timeout=30)
            if res.message_type is not Message.MESSAGE_TYPE_ERROR:
                create_alert_response = json.loads(res.payload)
                print("Response for irflow_service_create_alert: \n"
                      "Created IR-Flow Alert ID: '{0}'"
                      .format(create_alert_response['alert_num']))
            else:
                print("Error invoking service with topic '{0}': {1} ({2})".format(
                    request_topic, res.error_message, res.error_code))


Once a connection is established to the DXL fabric, a :class:`dxlmarclient.client.MarClient` instance is created
which will be used to perform searches.

Next, a search to collect the IP addresses for monitored systems is performed by invoking
the :func:`dxlmarclient.client.MarClient.search` method of the :class:`dxlmarclient.client.MarClient` instance.

Once the search has completed, the first 10 results are retrieved by invoking the
:func:`dxlmarclient.client.ResultsContext.get_results` method of the :class:`dxlmarclient.client.ResultsContext`
object that was returned from invoking the search method. The results are iterated and printed to the screen.