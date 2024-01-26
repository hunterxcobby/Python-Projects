When you make a request to a server using `urlopen` from the `urllib.request` module, the server may respond with an HTTP error code along with an error page. Here's how you can handle these errors and interpret the error codes:

1. **HTTP Error Codes**:
   - HTTP error codes are numeric codes returned by the server to indicate the status of the request.
   - Codes in the 100–299 range typically indicate success, while codes in the 400–599 range indicate errors.
   - For example, `404` means "Not Found," indicating that the requested resource does not exist on the server.

2. **Handling Errors**:
   - You can handle HTTP errors using `urllib.error.HTTPError`. When an HTTP error occurs, `urlopen` raises an `HTTPError` exception.
   - The `HTTPError` instance has attributes like `code`, which represents the HTTP error code returned by the server.
   - You can also access the error page returned by the server using the `read()` method of the `HTTPError` instance.

Example:
```python
import urllib.request
import urllib.error

req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)  # prints the HTTP error code, e.g., 404
    print(e.read())  # prints the error page returned by the server
```

In this example, if the requested URL `http://www.python.org/fish.html` returns a `404` error (Not Found), the code will print `404` along with the error page returned by the server. This helps you understand the reason for the error and handle it accordingly in your code.