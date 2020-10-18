import requests
from requests import exceptions, Timeout, RequestException
import time

from rest_framework import status
from rest_framework.response import Response

MAX_RETRIES = 2  # Arbitrary number of times to attempt request


def get_json(url):
    attempt_count = 0

    while attempt_count < MAX_RETRIES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == status.HTTP_200_OK:
                return Response(response.json(), status=status.HTTP_200_OK)
            if status.is_client_error(response.status_code):
                return Response(response.reason, status=response.status_code)
        except Timeout as etout:
            attempt_count += 1
        except RequestException as erq:
            attempt_count += 1
        except ConnectionError as econ:
            attempt_count += 1
        else:
            attempt_count += 1

        time.sleep(2) # delay before retry

    return Response({"error": "Request failed"}, status=response.status_code)