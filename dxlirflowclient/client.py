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

    def create_alert(self, payload, description, incoming_field_group_name, suppress_missing_field_warning):
        """
        Creates an alert in IR-Flow

        :param payload: IR-Flow Fact Fields (dict)
        :param description: The IR-Flow Alert Description
        :param incoming_field_group_name: The Data Source Name in IR-Flow
        :param suppress_missing_field_warning: Boolean to show missing fields from API
        :return: The alert creation json
        """
        # Validate specified output format
        # Commented out, will only support JSON return
        # if out_format not in IRFlowApiClient.OUT_FORMATS:
        #    raise Exception("Unknown format: {0}".format(out_format))

        # Create the DXL request message
        request = Request("/syncurity/service/irflow_api/create_alert")

        # Build Request payload
        fact_data = {'fields': payload, 'description': description,
                     'incoming_field_group_name': incoming_field_group_name,
                     'suppress_missing_field_warning': suppress_missing_field_warning}

        # Set the payload on the request message (Python dictionary to JSON payload)
        MessageUtils.dict_to_json_payload(
            request,
            fact_data
        )

        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)

        return response

    def close_alert(self, payload):
        """
        Closes an alert in IR-Flow

        :param payload: IR-Flow Close Alert Fields (dict) (alert_num(str), close_reason(str)

        :return: The alert close json
        """
        # Validate specified output format
        # Commented out, will only support JSON return
        # if out_format not in IRFlowApiClient.OUT_FORMATS:
        #    raise Exception("Unknown format: {0}".format(out_format))

        # Create the DXL request message
        request = Request("/open/threat/v1/orchestration/Syncurity/service/irflow_api/close_alert")

        # Build Request payload
        fact_data = {'alert_num': payload['alert_num'],
                     'close_reason': payload['close_reason']}

        # Set the payload on the request message (Python dictionary to JSON payload)
        MessageUtils.dict_to_json_payload(
            request,
            fact_data
        )

        # Perform a synchronous DXL request
        response = self._dxl_sync_request(request)

        return response

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

