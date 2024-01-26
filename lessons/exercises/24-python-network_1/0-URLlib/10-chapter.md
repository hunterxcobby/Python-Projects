Basic authentication in Python's `urllib.request` module involves using the `HTTPBasicAuthHandler` to handle authentication requests from servers. Here's a step-by-step explanation of how to use basic authentication with urllib:

1. **Create a Password Manager**: You start by creating a password manager object (`HTTPPasswordMgrWithDefaultRealm`) to handle the mapping of URLs and realms to usernames and passwords.

2. **Add Username and Password**: Add the username and password to the password manager using the `add_password()` method. If you don't know the realm, you can pass `None` instead.

3. **Create HTTPBasicAuthHandler**: Instantiate an `HTTPBasicAuthHandler` object, passing the password manager created in the previous step.

4. **Create Opener**: Build an opener (`OpenerDirector` instance) using `build_opener()`, passing the `HTTPBasicAuthHandler`.

5. **Fetch URL with Opener**: Use the opener to fetch a URL by calling `opener.open(a_url)`.

6. **Install Opener**: Install the opener using `install_opener(opener)`. This sets the installed opener as the default opener for all subsequent URL fetches.

By following these steps, you can authenticate with servers using basic authentication in Python's `urllib.request` module.