from botocore.exceptions import ClientError
from datetime import datetime
from enum import Enum
from urllib.parse import urlparse

import boto3
import json
import logging
import os
import random
import re
# import requests
import string
from api_sdk_python.API import MicroserviceAPI


class Click(Enum):
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    LONG = "LONG"


# environment
users_params_table_name = os.environ.get("USERS_PARAMS_TABLE_NAME")
microservice_endpoint = os.environ.get("MICROSERVICE_ENDPOINT")
minimum_password_length = 12

# resources
dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
config_table = dynamodb.Table(users_params_table_name)
current_ts = datetime.now().isoformat().split(".")[0].replace(":", "-")

# logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

microservice_api = MicroserviceAPI(
    api_endpoint=microservice_endpoint,
    api_version="Prod",
    region="eu-west-1"
)


def camelcase_to_snake(s):
    """Convert camelcase to snakecase notation"""

    d = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', d).lower()


def snake_to_camelcase(s):
    """Convert snakecase to camelcase notation"""

    return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), s)


def launch_stack(configuration_item):
    """Launch stack given a configuration item"""

    # define stack data
    stackdata = None

    # fingers crossed
    try:

        # generate a `minimum_password_length` random password if not defined in configuration item parameter
        configuration_item["app_password"] = "".join(
            random.choices(string.ascii_letters + string.digits, k=minimum_password_length)) \
            if "app_password" not in configuration_item.keys() \
            else configuration_item["app_password"]

        # map configuration item parameters to stack parameters
        parameters = list(map(lambda x: {
            "ParameterKey": f"{snake_to_camelcase(x)[0].upper()}{snake_to_camelcase(x)[1:]}",
            "ParameterValue": configuration_item[x]
        }, configuration_item.keys()))

        response = microservice_api.create_environment(parameters)
        # response = requests.post(
        #     f"{microservice_endpoint}/environments", data=json.dumps(parameters))
        stackdata = response.text

    # if any error occur
    except Exception as e:
        logging.error(str(e))

    return stackdata


def stack_exists(name, required_status=["CREATE_COMPLETE", "UPDATE_COMPLETE"]):
    try:

        # response = requests.get(f"{microservice_endpoint}/environments",
        #                         {'stack_name': name, 'stack_statuses': required_status})
        response = microservice_api.list_environments(
            params={'stack_name': name, 'stack_statuses': required_status})

        if response.text != None:
            return True

        return False

    except ClientError:

        return False


def take_care_of(event, configuration_item):

    # if click event is single
    if Click(event["clickType"]) is Click.SINGLE:

        logging.info(f"Single click from {event['clickType']}")

        if stack_exists(f"VisualCodeServer-{event['serialNumber']}"):
            logging.info("Nothing to do")
            # do nothing
            return {"message": "A stack with this name already exists"}

        stack_creation = launch_stack(configuration_item)
        return stack_creation

    # if click event is double
    elif Click(event["clickType"]) is Click.DOUBLE:

        logging.info(f"Double click from {event['clickType']}")

        if stack_exists(f"VisualCodeServer-{event['serialNumber']}") == False:
            logging.info("Nothing to do")
            # do nothing
            return {"message": "A stack with this name doesn't exists"}

        # stack_deletion = requests.delete(
        #     f"{microservice_endpoint}/environments", data=json.dumps({
        #         "StackName": f"VisualCodeServer-{event['serialNumber']}"
        #     }))

        stack_deletion = microservice_api.delete_environment({
            "StackName": f"VisualCodeServer-{event['serialNumber']}"
        })

        return stack_deletion.text

    # if click event is long
    elif Click(event["clickType"]) is Click.LONG:

        logging.info(f"Long click from {event['clickType']}")

        # do nothing
        return {"message": "No action mapped to LONG press"}


def handler(event, context):

    logging.info(event)

    # fingers crossed
    try:

        # retrieve configuration item for given user and handle related event
        response = config_table.get_item(
            Key={"user_id": event["serialNumber"]})

        message = take_care_of(event, configuration_item=response["Item"])

        return {
            "statusCode": 200,
            "body": json.dumps(message),
        }

    # if any error occurs
    except ClientError as e:

        logging.error(e.response["Error"]["Message"])
