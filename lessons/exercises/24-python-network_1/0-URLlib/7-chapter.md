Here's a breakdown of two approaches to handle `HTTPError` and `URLError` in Python when using the `urllib.request` module:

### Approach 1:
```python
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

req = Request(someurl)
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    # Everything is fine
```

### Approach 2:
```python
from urllib.request import Request, urlopen
from urllib.error import URLError

req = Request(someurl)
try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    # Everything is fine
```

### Explanation:
- Both approaches handle potential errors when making requests using `urlopen`.
- Approach 1 uses separate `except` blocks for `HTTPError` and `URLError`, providing specific error messages for each type of error.
- Approach 2 checks if the error object (`e`) has either a `reason` attribute (for `URLError`) or a `code` attribute (for `HTTPError`). It then prints the appropriate error message based on the available attribute.
- The `else` block in each approach is executed if no exceptions occur during the execution of the `try` block, indicating that the request was successful.

These approaches help you gracefully handle errors that may occur during URL requests, providing better control and understanding of the issues encountered during the communication with the server.