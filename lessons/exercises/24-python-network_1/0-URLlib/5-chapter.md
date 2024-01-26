When working with `urllib.request`, you may encounter exceptions, which are errors that occur during the execution of your code. Here's how to handle exceptions:

1. **URLError**:
   - `URLError` is raised when `urlopen` cannot handle a response. This can happen if there's no network connection or if the specified server doesn’t exist.
   - The exception object has a `reason` attribute, which is a tuple containing an error code and a text error message.
   - Example:
     ```python
     import urllib.request
     import urllib.error

     req = urllib.request.Request('http://www.pretend_server.org')
     try:
         urllib.request.urlopen(req)
     except urllib.error.URLError as e:
         print(e.reason)
     ```
   - In this example, if there's no connection to the server, it will print something like `(4, 'getaddrinfo failed')`.

2. **HTTPError**:
   - `HTTPError` is a subclass of `URLError` and is raised specifically for HTTP URLs.
   - This error occurs when the server returns an HTTP error response (e.g., 404 Not Found, 500 Internal Server Error).
   - You can handle `HTTPError` in a similar way as `URLError`, but with additional handling for HTTP-specific errors.

In summary, when using `urllib.request`, it's important to handle exceptions like `URLError` and `HTTPError` to gracefully handle unexpected situations, such as network issues or server errors.