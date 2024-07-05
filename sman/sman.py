import argparse
import requests
import json
import colorama
import importlib
import os
import sys
import subprocess

colorama.init()

# Define the banner text
banner = r"""
  ___|   \  |    \     \  | 
\___ \  |\/ |   _ \     \ | 
      | |   |  ___ \  |\  | 
_____/ _|  _|_/    _\_| \_| 
    _____| 
Made By SABBIR
"""

# Apply colors to the banner
colored_banner = colorama.Fore.CYAN + banner + colorama.Style.RESET_ALL

print(colored_banner)


def send_get_request(url, headers=None, params=None):
    """
    Send a GET request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        headers (dict, optional): Custom headers to include in the request. Defaults to None.
        params (dict, optional): URL parameters to include in the request. Defaults to None.

    Returns:
        bytes: The response content.

    """
    response = requests.get(url, headers=headers, params=params)
    return response.content


def send_post_request(url, data, headers=None, params=None, content_type='application/json'):
    """
    Send a POST request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        data (str): The data to include in the request.
        headers (dict, optional): Custom headers to include in the request. Defaults to None.
        params (dict, optional): URL parameters to include in the request. Defaults to None.
        content_type (str, optional): The content type of the request. Defaults to 'application/json'.

    Returns:
        bytes: The response content.

    """
    headers = headers or {'Content-Type': content_type}
    response = requests.post(url, data=data, headers=headers, params=params)
    return response.content


def check_module_installed(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

