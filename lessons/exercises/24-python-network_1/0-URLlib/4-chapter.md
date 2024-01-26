Let's understand how to add headers to HTTP requests using `urllib.request`:

1. **Headers in HTTP Requests**:
   - HTTP headers are additional pieces of information sent along with an HTTP request.
   - One important header is the `User-Agent` header, which identifies the client making the request. Websites may behave differently based on this header.
   - By default, `urllib` identifies itself as `Python-urllib/x.y`, which some websites may not like. You can specify a custom `User-Agent` header to mimic a different browser.
   - Example:
     ```python
     import urllib.parse
     import urllib.request

     url = 'http://www.someserver.com/cgi-bin/register.cgi'
     user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
     values = {'name': 'Michael Foord',
               'location': 'Northampton',
               'language': 'Python'}
     headers = {'User-Agent': user_agent}

     data = urllib.parse.urlencode(values)
     data = data.encode('ascii')
     req = urllib.request.Request(url, data, headers)
     with urllib.request.urlopen(req) as response:
        the_page = response.read()
     ```

2. **Using Headers**:
   - In the example above, we create a dictionary called `headers` containing the `User-Agent` header with a custom value.
   - When creating a `Request` object, we pass this dictionary as the `headers` argument.
   - This tells the server that our request is coming from a browser identified as `Mozilla/5.0 (Windows NT 6.1; Win64; x64)`.

In summary, you can customize HTTP requests in `urllib.request` by adding headers. This allows you to mimic different browsers or provide additional information to the server when making requests.