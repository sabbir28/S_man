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


def main():
    """
    Main function to handle command-line arguments and execute the request sending functionality.
    """
    # Check if the required modules are installed
    required_modules = ['argparse', 'requests', 'json', 'colorama']
    missing_modules = []
    for module in required_modules:
        if not check_module_installed(module):
            missing_modules.append(module)

    if missing_modules:
        print(f"The following modules are missing: {', '.join(missing_modules)}")
        install_modules = input("Do you want to install the missing modules? (y/n): ")
        if install_modules.lower() == 'y':
            for module in missing_modules:
                install_module(module)
            print("Modules installed successfully.")
        else:
            print("Cannot proceed without installing the missing modules.")
            return

    parser = argparse.ArgumentParser(description='Send requests with different data types to a server.')
    parser.add_argument('-u', '--url', required=True, help='Server URL')
    parser.add_argument('-r', '--request', choices=['get', 'post'], required=True,
                        help='HTTP request method (GET or POST)')
    parser.add_argument('-d', '--data', help='Data to send')
    parser.add_argument('-H', '--headers', help='Custom headers (in quotes)')
    parser.add_argument('-p', '--params', help='URL parameters (in quotes)')
    parser.add_argument('-t', '--content-type', help='Content type for the request')
    parser.add_argument('-s', '--save-file', help='File path to save the response')

    args = parser.parse_args()

    url = args.url
    method = args.request.lower()

    headers = None
    if args.headers:
        try:
            headers = json.loads(args.headers)
        except ValueError:
            print("Invalid JSON format for headers.")
            return

    params = None
    if args.params:
        try:
            params = json.loads(args.params)
        except ValueError:
            print("Invalid JSON format for parameters.")
            return

    content_type = args.content_type
    save_file = args.save_file

    if method == 'get':
        response = send_get_request(url, headers=headers, params=params)
    elif method == 'post':
        data = args.data
        if data is None:
            print("Data is required for POST request.")
            return

        response = send_post_request(url, data, headers=headers, params=params, content_type=content_type)
    else:
        print("Invalid HTTP request method.")
        return

    print("Response:")
    response_content = response.decode()
    print(response_content)

    if save_file:
        try:
            with open(save_file, 'w') as file:
                file.write(response_content)
            print(f"Response saved to {save_file} successfully.")
        except Exception as e:
            print(f"Error occurred while saving the file: {e}")


if __name__ == "__main__":
    main()
