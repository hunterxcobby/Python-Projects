The HEAD request method is similar to GET, but it retrieves only the response header without the actual document body. This is useful for checking header information like Last-Modified, Content-Type, and Content-Length before making a full GET request to retrieve the document. The syntax for a HEAD request is similar to that of a GET request, but without the response body.

Here's an example of a HEAD request:

```
HEAD /index.html HTTP/1.0
(blank line)
```

And the corresponding response:

```
HTTP/1.1 200 OK
Date: Sun, 18 Oct 2009 14:09:16 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Sat, 20 Nov 2004 07:16:26 GMT
ETag: "10000000565a5-2c-3e94b66c2e680"
Accept-Ranges: bytes
Content-Length: 44
Connection: close
Content-Type: text/html
X-Pad: avoid browser bug
```

Note that the response only includes the header information and does not contain the actual document body.