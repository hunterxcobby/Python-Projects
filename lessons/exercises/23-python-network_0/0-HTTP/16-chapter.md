### HTTP/1.0 GET Request Example:

In an HTTP/1.0 GET request, the client requests a specific resource from the server using the GET method. Here's an example of a GET request along with the response received from the server:

#### Request:
```
GET /index.html HTTP/1.0
```
(Enter twice to create a blank line)

#### Response:
```
HTTP/1.1 200 OK
Date: Sun, 18 Oct 2009 08:56:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Sat, 20 Nov 2004 07:16:26 GMT
ETag: "10000000565a5-2c-3e94b66c2e680"
Accept-Ranges: bytes
Content-Length: 44
Connection: close
Content-Type: text/html
X-Pad: avoid browser bug

<html><body><h1>It works!</h1></body></html>
```

#### Description:
- **Request Line:** Specifies the method (`GET`), request-URI (`/index.html`), and HTTP version (`HTTP/1.0`).
- **Response Status Line:** Indicates the HTTP version, status code (`200 OK`), and reason phrase.
- **Response Headers:** Provide metadata about the response, including date, server information, content details (type, length), and connection information.
- **Response Body:** Contains the requested document (`<html><body><h1>It works!</h1></body></html>` in this case).
- **Connection:** The server closes the TCP connection (`Connection: close`) after delivering the response in HTTP/1.0 by default.

#### Notes:
- **Case Sensitivity:** The request method name "GET" is case-sensitive and must be in uppercase.
- **Error Handling:** Incorrect request method names or URIs can result in various error messages (e.g., "501 Method Not Implemented," "404 Not Found," "400 Bad Request").
- **Connection Handling:** HTTP/1.0 closes the connection by default, while HTTP/1.1 uses keep-alive connections unless specified otherwise (`Connection: Keep-Alive`). This affects network efficiency and subsequent requests on the same connection.

Understanding these components helps in effectively communicating with HTTP servers and handling responses based on their status codes and headers.