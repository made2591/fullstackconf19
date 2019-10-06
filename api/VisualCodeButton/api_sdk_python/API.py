import boto3
import random
import string
import dateutil.parser as date_parser

import requests
from .aws_requests_auth.boto_utils import BotoAWSRequestsAuth
from .APIExceptions import APIException, BadRequestException, UnauthorizedException, ForbiddenException, NotFoundException, ConflictException, InternalServerErrorException


class API(object):

    def __init__(self, region, api_endpoint, api_version):
        self.api_endpoint = api_endpoint
        self.api_version = api_version
        self.region = region
        self.api_baseurl = f"{self.api_endpoint}/{self.api_version}"

    def __api_auth(self):
        return BotoAWSRequestsAuth(
            aws_host=self.api_endpoint,
            aws_region=self.region,
            aws_service='execute-api'
        )

    def __http_handle_response(self, response):
        if response.status_code == 200 or response.status_code == 201 or response.status_code == 202:
            return response.json()
        elif response.status_code == 400:
            raise BadRequestException()
        elif response.status_code == 401:
            raise UnauthorizedException()
        elif response.status_code == 403:
            raise ForbiddenException()
        elif response.status_code == 404:
            raise NotFoundException()
        elif response.status_code == 409:
            raise ConflictException()
        elif response.status_code == 500:
            raise InternalServerErrorException()
        else:
            raise APIException()

    def http_get(self, uri, params=None):
        return self.__http_handle_response(
            response=requests.get(
                f"{self.api_baseurl}/{uri}", auth=self.__api_auth(), params=params)
        )

    def http_post(self, uri, body=None):
        return self.__http_handle_response(
            response=requests.post(
                f"{self.api_baseurl}/{uri}", auth=self.__api_auth(), json=body)
        )

    def http_put(self, uri, body=None):
        return self.__http_handle_response(
            response=requests.put(
                f"{self.api_baseurl}/{uri}", auth=self.__api_auth(), json=body)
        )

    def http_delete(self, uri, body=None):
        return self.__http_handle_response(
            response=requests.delete(
                f"{self.api_baseurl}/{uri}", auth=self.__api_auth(), json=body)
        )


class MicroserviceAPI(API):

    def list_environments(self, params=None):
        return self.http_get(
            uri="environments",
            params=params
        )

    def create_environment(self, body):
        return self.http_post(
            uri="environments",
            body=body
        )

    def delete_environment(self, body):
        return self.http_delete(
            uri="environments",
            body=body
        )
