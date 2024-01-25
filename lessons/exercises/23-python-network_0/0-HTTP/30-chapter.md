URL (Uniform Resource Locator) serves as a unique identifier for web resources and consists of four main parts:

1. **Protocol**: Specifies the communication protocol used, such as HTTP, FTP, or telnet.
2. **Hostname**: Identifies the server's DNS domain name (e.g., www.example.com) or IP address.
3. **Port**: Denotes the TCP port number that the server listens for client requests. If not specified, it defaults to port 80 for HTTP.
4. **Path-and-file-name**: Indicates the location and name of the requested resource under the server's document base directory.

For example, in the URL http://www.example.com/docs/index.html:
- Protocol: HTTP
- Hostname: www.example.com
- Port: Default (80 for HTTP)
- Path-and-file-name: /docs/index.html

Special characters in URLs, like spaces or tildes (~), are encoded as %xx, where xx represents the ASCII hex code. For instance, '~' is encoded as %7e, and a space can be encoded as %20 or '+'.

URI (Uniform Resource Identifier) is a broader concept than URL and can identify fragments within a resource. The URI syntax for HTTP protocol includes request parameters and a name anchor:
- Request parameters, in name=value pairs, are appended to the URL with '?' as a separator and separated by '&'.
- The #nameAnchor identifies a specific fragment within an HTML document, usually defined using the anchor tag <a name="anchorName">...</a>.

Additionally, URI can be used for URL rewriting for session management, such as appending ";sessionID=xxxxxx" to maintain session state across requests.