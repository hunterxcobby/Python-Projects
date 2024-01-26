Let's break down the steps for fetching URLs using `urllib.request`:

1. **Simple URL Fetching**:
   - The basic way to fetch a URL is by using the `urlopen` function from the `urllib.request` module.
   - This function opens the URL specified as an argument and returns a response object that represents the data retrieved from the URL.
   - Example:
     ```python
     import urllib.request
     with urllib.request.urlopen('http://python.org/') as response:
        html = response.read()
     ```

2. **Storing a Resource Temporarily**:
   - If you want to fetch a resource and store it in a temporary location, you can use `shutil.copyfileobj()` and `tempfile.NamedTemporaryFile()` functions.
   - This is useful when you want to process the data later or store it for further use.
   - Example:
     ```python
     import shutil
     import tempfile
     import urllib.request

     with urllib.request.urlopen('http://python.org/') as response:
         with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
             shutil.copyfileobj(response, tmp_file)

     with open(tmp_file.name) as html:
         pass
     ```

3. **HTTP Requests and Responses**:
   - HTTP (HyperText Transfer Protocol) is based on requests and responses. Clients (like browsers) make requests to servers, and servers respond with data.
   - `urllib.request` mirrors this behavior with a `Request` object, which represents the HTTP request being made.
   - You create a `Request` object specifying the URL you want to fetch, and then use `urlopen` with this `Request` object to get a response object.
   - Example:
     ```python
     import urllib.request

     req = urllib.request.Request('http://python.org/')
     with urllib.request.urlopen(req) as response:
        the_page = response.read()
     ```

4. **Using Request Objects**:
   - Request objects allow you to pass additional data or metadata (headers) to the server along with the request.
   - This can be useful for sending data to the server or providing extra information about the request.
   - Example:
     ```python
     req = urllib.request.Request('http://python.org/')
     # You can pass data or metadata here
     ```

In summary, `urllib.request` provides a simple interface for fetching URLs, handling responses, and interacting with servers using HTTP. It's a versatile tool for making web requests and retrieving data from the internet.