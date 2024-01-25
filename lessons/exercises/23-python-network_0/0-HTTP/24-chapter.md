To issue a GET request through a proxy server:

1. **Establish Connection**: First, establish a TCP connection to the proxy server.

2. **Use Absolute Request-URI**: When sending the GET request, use an absolute request-URI that includes the full URL of the target server, including the hostname, port, and path.

Here's an example of a GET request issued through a proxy server using telnet:

```
GET http://www.amazon.com/index.html HTTP/1.1
Host: www.amazon.com
Connection: Close
(blank line)
```

In this example:
- The request line includes the absolute request-URI: `GET http://www.amazon.com/index.html HTTP/1.1`.
- The `Host` header specifies the hostname of the target server.
- The `Connection` header indicates that the connection should be closed after this request.

The response from the server includes a status code (`302 Found`) indicating a redirection, along with other headers and the response body.

It's important to note that the response is returned in "chunks," which means the response body is divided into separate parts for transmission.