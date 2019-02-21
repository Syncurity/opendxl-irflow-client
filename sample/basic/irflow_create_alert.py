from __future__ import absolute_import
from __future__ import print_function
import json
import os
import sys

from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient
from dxlclient.message import Message, Event, Request
from dxlbootstrap.util import MessageUtils
from dxlirflowclient.client import IRFlowApiClient

# Import common logging and configuration
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Create the client
with DxlClient(config) as client:

    # Connect to the fabric
    client.connect()

    logger.info("Connected to DXL fabric.")

    # Build IR-Flow Client
    irfc = IRFlowApiClient(client)

    # Set request that will trigger request callback 'irflow_service_create_alert'
    request_topic = "/syncurity/service/irflow_api/create_alert"
    req = Request(request_topic)

    # Create dictionary payload with host to lookup and response format
    # eventType is Incoming Data Field Group in IR-Flow
    # See the payload of the alert object in IR-Flow to determine key: value pairs available
    # TODO parametrize kv pairs for creating alert or allow a dictionary to be passed in

    req_dict = {
        "sourceHostName": "irflow-test.syncurity.net",
        "sourceAddress": "10.0.10.20"
    }

    description = "DXL Payload"
    incoming_field_group_name = 'DXLAlerts'
    suppress_missing_field_warning = True

    # Fire Away
    res = irfc.create_alert(req_dict, description, incoming_field_group_name, suppress_missing_field_warning)
    if res.message_type is not Message.MESSAGE_TYPE_ERROR:
        create_alert_response = json.loads(res.payload)

        print("Response for irflow_service_create_alert: \n"
              "Created IR-Flow Alert ID: '{0}' \n"
              .format(create_alert_response['alert_num']))

        # Print output. You could also return this json to an app
        for key, value in create_alert_response.items():
            print(key + ': ' + str(value))
    else:
        print("Error invoking service with topic '{0}': {1} ({2})".format(
            request_topic, res.error_message, res.error_code))
