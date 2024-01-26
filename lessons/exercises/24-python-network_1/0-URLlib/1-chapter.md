1. **Introduction to urllib.request**:
   - `urllib.request` is a Python module that helps you fetch URLs (Uniform Resource Locators). Think of URLs as addresses for resources on the internet, like web pages, images, or files.
   - It provides a simple way to access these resources using the `urlopen` function.

2. **Capabilities of urllib.request**:
   - `urllib.request` can handle various protocols for fetching URLs, such as HTTP, FTP, and more.
   - It also offers features for handling common scenarios like basic authentication (logging in), cookies (storing information about your browsing session), proxies (intermediaries between you and the server), and more.
   - These features are implemented through objects called handlers and openers.

3. **URL Schemes and Protocols**:
   - A URL scheme is the part of a URL that identifies the protocol being used. For example, "ftp" in "ftp://python.org/".
   - `urllib.request` supports fetching URLs for various URL schemes (protocols) using their associated network protocols (e.g., FTP, HTTP).
   - This tutorial focuses on the most common protocol, HTTP, which is used for accessing web pages and resources on the World Wide Web.

4. **Using urlopen for Basic Cases**:
   - For simple cases, using the `urlopen` function is straightforward. It allows you to fetch URLs easily.
   - However, when you encounter errors or more complex situations, such as accessing secure websites or handling redirects, you'll need some understanding of the HTTP protocol.

5. **Understanding HTTP**:
   - HTTP (HyperText Transfer Protocol) is the protocol used for transferring hypertext (like web pages) over the internet.
   - It defines how messages are formatted and transmitted, and how web servers and browsers should respond to various commands.
   - The most comprehensive reference for HTTP is RFC 2616, but it's a technical document and can be difficult to read.

6. **Purpose of the HOWTO**:
   - This HOWTO aims to explain how to use `urllib` effectively, providing enough detail about HTTP to help you navigate through common scenarios.
   - It's meant to be a supplement to the official documentation for `urllib.request`, providing additional insights and explanations.

In summary, `urllib.request` is a powerful tool for fetching resources from the internet, and understanding how it works with different protocols and HTTP can help you effectively use it in your Python programs to interact with web servers and retrieve data.