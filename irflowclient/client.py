from __future__ import absolute_import
from dxlclient.message import Request
from dxlbootstrap.util import MessageUtils
from dxlbootstrap.client import Client


class IRFlowApiClient(Client):
    """
    The ""IR-Flow Client"" client wrapper class.
    """

    # The valid output formats
    OUT_FORMATS = ["json", "dict"]

    def __init__(self, dxl_client):
        """
        Constructor parameters:

        :param dxl_client: The DXL client to use for communication with the fabric
        """
        super(IRFlowApiClient, self).__init__(dxl_client)

    def create_alert(self, fact_data, out_format="dict"):
        """
        Creates an alert in IR-Flow

        :param fact_data: IR-Flow Fact Fields (dict)
        :param out_format: The output format
        :return: The alert creation json
        """
        # Validate specified output format
        if out_format not in IRFlowApiClient.OUT_FORMATS:
            raise Exception("Unknown format: {0}".format(out_format))

        # Create the DXL request message
        request = Request("/syncurity/service/irflow_api/create_alert")

        # Build Request payload
        payload = {fact_data}
        payload['format'] = ("json" if out_format is "dict" else out_format)
        payload['eventType'] = "openDXL fabric alert"

        # Set the payload on the request message (Python dictionary to JSON payload)
        MessageUtils.dict_to_json_payload(
            request,
            payload
        )

        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)

        if out_format is "dict":
            return MessageUtils.json_payload_to_dict(response)
        else:
            return MessageUtils.decode_payload(response)

    def my_example_method(self):
        """
        TODO: Example only, should be removed
    
        This is an example method that demonstrates how DXL service invocations can be wrapped
        by the client. In this particular case we are making a service request to the broker
        the client is currently connected to in order to retrieve its health information.
        The results of the query are returned as a Python dictionary. The DXL-specific details
        (topics, message objects, JSON payload format, etc.) are hidden from the users of this
        method.
    
        :return: The result of the broker health query
        """
        # Create the DXL request message
        request = Request("/mcafee/service/dxl/broker/health")
    
        # Set the payload on the request message (Python dictionary to JSON payload)
        MessageUtils.dict_to_json_payload(request, {})
    
        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)
    
        # Convert the JSON payload in the DXL response message to a Python dictionary
        # and return it.
        return MessageUtils.json_payload_to_dict(response)
