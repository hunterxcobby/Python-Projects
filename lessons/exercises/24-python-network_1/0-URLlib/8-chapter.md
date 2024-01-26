Here's an explanation of the `info()` and `geturl()` methods in Python's `urllib.request` module:

### `geturl()`
- The `geturl()` method returns the actual URL of the page that was fetched.
- This is beneficial because `urlopen()` or the opener object used might have followed a redirect. 
- The URL of the page retrieved might differ from the originally requested URL.

### `info()`
- The `info()` method returns a dictionary-like object that describes the fetched page, particularly the headers sent by the server.
- It returns an `http.client.HTTPMessage` instance.
- Common headers include attributes like `Content-Length`, `Content-Type`, and others, which provide information about the content being sent by the server.
- For more details on HTTP headers and their meanings, you can refer to resources like the Quick Reference to HTTP Headers, which provides a useful listing of HTTP headers with brief explanations.

These methods allow you to gather additional information about the fetched page, such as its URL and the headers provided by the server, which can be valuable for understanding and processing the retrieved content.