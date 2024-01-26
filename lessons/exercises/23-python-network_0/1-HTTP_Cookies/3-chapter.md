The lifetime of a cookie can be defined using the attributes in the `Set-Cookie` header. There are two types of cookie lifetimes:

1. **Permanent Cookies:**
   - Permanent cookies have an expiration date specified by the `Expires` attribute or a period set by the `Max-Age` attribute.
   - The `Expires` attribute defines a specific date and time when the cookie will expire and be deleted by the browser.
   - For example, `Set-Cookie: id=a3fWa; Expires=Thu, 31 Oct 2021 07:28:00 GMT;` sets a permanent cookie with an expiration date of October 31, 2021, at 07:28:00 GMT.
   - Alternatively, the `Max-Age` attribute specifies the maximum age of the cookie in seconds. After this period, the cookie will expire and be deleted.
   - Permanent cookies persist even after the browser is closed and are stored on the user's device until they expire or are manually deleted.

2. **Session Cookies:**
   - Session cookies do not have an expiration date or a `Max-Age` attribute specified.
   - These cookies are deleted when the current browsing session ends.
   - The end of a session is determined by the browser, and it varies depending on the browser and its settings.
   - Some browsers may retain session cookies even after closing the browser if they support session restoring or session persistence.
   - Session cookies are commonly used for temporary data storage during a user's session on a website and are deleted when the user closes the browser.

Here's an example in Python of setting a cookie with an expiration date using Flask:

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def set_cookie():
    response = make_response("Setting cookie")
    response.set_cookie('id', 'a3fWa', expires=datetime.datetime(2021, 10, 31, 7, 28, 0))
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

In this example, the `expires` parameter in `set_cookie()` method sets the expiration date for the cookie.