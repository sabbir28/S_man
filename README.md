# Sman

A Python command-line tool for sending HTTP requests with different data types to a server.

## Usage

```
python sman.py -u <url> -r <request> [-d <data>] [-H <headers>] [-p <parameters>] [-t <content-type>]
```

### Arguments

- `-u, --url`: The URL of the server to send the request to. (Required)
- `-r, --request`: The HTTP request method to use (GET or POST). (Required)
- `-d, --data`: The data to include in the request. (Optional)
- `-H, --headers`: Custom headers to include in the request, specified in JSON format. (Optional)
- `-p, --params`: URL parameters to include in the request, specified in JSON format. (Optional)
- `-t, --content-type`: The content type of the request. Defaults to 'application/json'. (Optional)

## Supported Data Types

- JSON (JavaScript Object Notation): A lightweight data interchange format that is easy to read and write for humans and machines.
- XML (eXtensible Markup Language): A format for representing structured data using tags and attributes.
- Form Data: Data sent using HTML forms with encoding types of `application/x-www-form-urlencoded` or `multipart/form-data`.
- Plain Text: Simple plain text data for basic data transmission.
- Binary Data: Binary files such as images, audio, or video files.
- GraphQL: A query language for APIs that allows structured requests and retrieval of specific data.
- Protobuf (Protocol Buffers): A binary serialization format for structured data with a specific schema.

## Examples

### Send a POST request with JSON data

```
python sman.py -u https://example.com/api -r post -d '{"name": "John", "age": 30}'
```

### Send a GET request with custom headers and URL parameters

```
python sman.py -u https://example.com/api -r get -H '{"Authorization": "Bearer token"}' -p '{"page": 1, "limit": 10}'
```

### Send a POST request with form data

```
python sman.py -u https://example.com/submit -r post -d 'username=johndoe&password=secret' -t application/x-www-form-urlencoded
```

## Dependencies

The following dependencies are required to run the script:

- Python 3.x
- requests
- argparse
- json
- colorama

To install the dependencies, you can use pip:

```
pip install requests argparse colorama
```

## License

This project is licensed under the MIT License. See the https://alor28.web.app file for details.

---

The script provides a convenient way to send requests to a server using various data types. It can be useful for testing APIs, interacting with web services, or performing data exchange with a server.
