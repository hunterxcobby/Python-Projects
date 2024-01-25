The OPTIONS request method allows a client to query the server about which request methods are supported for a particular resource. It's useful for understanding what actions are permitted by the server. The syntax for an OPTIONS request message is straightforward:

```
OPTIONS request-URI|* HTTP-version
(other optional headers)
(blank line)
```

Here's an example of an OPTIONS request:

```
OPTIONS http://www.amazon.com/ HTTP/1.1
Host: www.amazon.com
Connection: Close
(blank line)
```

And the corresponding response from the server:

```
HTTP/1.1 200 OK
Date: Fri, 27 Feb 2004 09:42:46 GMT
Content-Length: 0
Connection: close
Server: Stronghold/2.4.2 Apache/1.3.6 C2NetEU/2412 (Unix)
Allow: GET, HEAD, POST, OPTIONS, TRACE
Connection: close
Via: 1.1 xproxy (NetCache NetApp/5.3.1R4D5)
(blank line)
```

In this response, the server indicates which request methods are allowed for the specified resource. In this case, it allows GET, HEAD, POST, OPTIONS, and TRACE methods. Additionally, the response includes other headers like Date, Content-Length, and Server information.