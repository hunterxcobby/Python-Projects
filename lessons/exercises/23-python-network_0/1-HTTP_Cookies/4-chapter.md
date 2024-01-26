To restrict access to cookies and enhance their security, you can use the `Secure` and `HttpOnly` attributes:

1. **Secure Attribute:**
   - A cookie with the `Secure` attribute is only sent to the server with an encrypted request over the HTTPS protocol.
   - It ensures that the cookie is transmitted securely and is not sent over unsecured HTTP connections.
   - This attribute helps prevent man-in-the-middle attacks by ensuring that the cookie is only transmitted over encrypted connections.
   - However, it's important to note that the `Secure` attribute does not prevent access to sensitive information in cookies by someone with access to the client's hard disk or by JavaScript if the `HttpOnly` attribute isn't set.

2. **HttpOnly Attribute:**
   - A cookie with the `HttpOnly` attribute is inaccessible to JavaScript via the `Document.cookie` API.
   - It ensures that the cookie is only sent to the server and cannot be accessed or modified by client-side scripts.
   - This attribute is particularly useful for cookies that store sensitive information or authentication tokens, as it helps mitigate cross-site scripting (XSS) attacks.
   - Cookies that are used for server-side sessions and don't need to be accessed by JavaScript should have the `HttpOnly` attribute set.

Example of setting a cookie with both `Secure` and `HttpOnly` attributes in Python with Flask:

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def set_cookie():
    response = make_response("Setting cookie")
    response.set_cookie('id', 'a3fWa', expires=datetime.datetime(2021, 10, 21, 7, 28, 0), secure=True, httponly=True)
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, the `secure=True` and `httponly=True` parameters in `set_cookie()` method set the `Secure` and `HttpOnly` attributes for the cookie, respectively.