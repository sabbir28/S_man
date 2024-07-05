# HTTP Request CLI Tool Integration Guide

This guide explains how to import and use the HTTP Request CLI tool in your own projects. The tool, created by MD. SABBIR HOSHEN, allows you to send HTTP GET and POST requests with various data types, supporting custom headers and URL parameters.

## Installation

Ensure you have the required dependencies installed in your Python environment:

```bash
pip install requests colorama
```

## Integration

### Importing the Code

Save the provided code in a Python file, e.g., `sman.py`.

### Functions

You can use the functions provided in the script to send HTTP requests from your own code. Below are examples of how to import and use these functions.

#### `send_get_request`

```python
from sman import send_get_request

url = "http://example.com/api"
headers = {"Authorization": "Bearer token"}
params = {"param1": "value1"}

response = send_get_request(url, headers=headers, params=params)
print(response.decode())
```

#### `send_post_request`

```python
from sman import send_post_request

url = "http://example.com/api"
data = '{"key": "value"}'
headers = {"Authorization": "Bearer token"}
params = {"param1": "value1"}
content_type = "application/json"

response = send_post_request(url, data, headers=headers, params=params, content_type=content_type)
print(response.decode())
```

### Checking and Installing Modules

You can use the provided `check_module_installed` and `install_module` functions to ensure required modules are installed.

```python
from sman import check_module_installed, install_module

required_modules = ['argparse', 'requests', 'json', 'colorama']
missing_modules = [module for module in required_modules if not check_module_installed(module)]

if missing_modules:
    print(f"Missing modules: {', '.join(missing_modules)}")
    for module in missing_modules:
        install_module(module)
```

### Command-Line Interface

The script can also be used as a standalone command-line tool. Below is an example of how to execute it from the command line.

#### Running the Script

Save the code in `sman.py` and run it from the command line:

```bash
python sman.py -u "http://example.com/api" -r get --show-response
```

#### Example Command-Line Usage

1. **GET Request**

   ```bash
   python sman.py -u "http://example.com/api" -r get --show-response
   ```

2. **POST Request with Data**

   ```bash
   python sman.py -u "http://example.com/api" -r post -d '{"key": "value"}' --show-response
   ```

3. **POST Request with Custom Headers and URL Parameters**

   ```bash
   python sman.py -u "http://example.com/api" -r post -d '{"key": "value"}' -H '{"Authorization": "Bearer token"}' -p '{"param1": "value1"}' --show-response
   ```

4. **Save Response to File**

   ```bash
   python sman.py -u "http://example.com/api" -r get -s response.txt
   ```

### Conclusion

By following this guide, you can easily integrate and use the HTTP Request CLI tool in your own projects. The provided functions offer flexibility for sending various types of HTTP requests with custom headers and parameters.