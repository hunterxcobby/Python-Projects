In Python's `urllib.request` module, when you fetch a URL, you're using an opener, which is an instance of `urllib.request.OpenerDirector`. The default opener is used when you call `urlopen()`, but you can create custom openers if you need to handle specific scenarios, like cookies or redirections.

Here's how you can work with openers and handlers:

1. **Custom Openers**: You can create custom openers by instantiating `OpenerDirector` and adding handlers to it using the `.add_handler()` method.
  
2. **Using `build_opener()`**: This is a convenience function for quickly creating opener objects with default or custom handlers. It's useful when you need to add multiple handlers or override default ones.

3. **Handlers**: Handlers do the heavy lifting in opening URLs. They know how to handle specific aspects like URL schemes (http, ftp) or situations like HTTP redirections or cookies.

4. **Installing Openers**: The `install_opener()` function sets an opener object as the global default opener. This means that subsequent calls to `urlopen()` will use the installed opener.

5. **Using Opener's `open()` Method**: Opener objects have an `open()` method that you can use to directly fetch URLs, similar to `urlopen()`. You don't necessarily need to call `install_opener()` unless you want to set a default opener for all subsequent URL fetches.

By understanding and utilizing openers and handlers effectively, you can customize how URLs are fetched and processed, allowing for greater control and flexibility in your network operations.