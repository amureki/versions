import json
import os
from typing import Optional
from urllib.error import URLError
import urllib.parse
import urllib.request
from time import sleep
from datetime import date

ACTUAL_VERSION_PREFIX = 3


def parse_python():
    url = "https://www.python.org/api/v2/downloads/release/"
    request = urllib.request.Request(
        url,
    )
    try:
        response = urllib.request.urlopen(request)
    except URLError as e:
        print(f"Error: {e}")
        return
    data = response.read().decode("utf-8")
    json_data = json.loads(data)
    # latest = [version for version in json_data if version['is_latest'] and version['version'] >= ACTUAL_VERSION_PREFIX]
    latest_versions = [version for version in json_data if version['is_latest']]
    the_latest = sorted(latest_versions, key=lambda k: k['version'], reverse=True)[0]
    breakpoint()
    raise ZeroDivisionError


if __name__ == "__main__":
    parse_python()
