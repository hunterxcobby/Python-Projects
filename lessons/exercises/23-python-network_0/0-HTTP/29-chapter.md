In web applications, users often interact with servers by submitting form data. This data can be sent to the server using either a GET or a POST request. Let's break down how this process works step by step:

1. **HTML Form Creation**: First, an HTML form is created within a web page using the `<form>` tag. This form contains various input fields where users can enter data.

2. **Form Fields**: Inside the form, different types of input fields are used to collect specific types of data:
   - Text Box (`<input type="text">`): Allows users to input text.
   - Password Box (`<input type="password">`): Similar to a text box but obscures the entered text.
   - Radio Button (`<input type="radio">`): Allows users to select one option from multiple choices.
   - Checkbox (`<input type="checkbox">`): Allows users to select multiple options.
   - Selection (`<select>` and `<option>`): Provides a dropdown menu for users to select an option.
   - Text Area (`<textarea>`): Allows users to input multiple lines of text.
   - Submit Button (`<input type="submit">`): Submits the form data to the server.
   - Reset Button (`<input type="reset">`): Clears the form fields.
   - Hidden Field (`<input type="hidden">`): Stores data that is not displayed to the user but is submitted with the form.

3. **Form Submission**: When the user fills in the form and clicks the submit button, the browser gathers the data from all the form fields.

4. **Query String Formation (GET)**: If the form method is set to `GET`, the browser constructs a query string by concatenating the names and values of all the form fields. Each name-value pair is separated by an ampersand (`&`). This query string is appended to the URL after a question mark (`?`). For example:
   ```
   GET /bin/login?user=Peter+Lee&pw=123456&action=login HTTP/1.1
   ```

5. **URL Encoding**: Special characters in the form data are replaced with their corresponding ASCII codes preceded by a percent sign (%). This process is called URL encoding. For example, a space becomes `%20` and a plus sign (+) can represent a space in some contexts.

6. **Request Submission**: The browser sends the form data as part of an HTTP request to the server. The server processes the request and responds accordingly.

7. **POST Method**: Alternatively, if the form method is set to `POST`, the form data is included in the body of the HTTP request instead of the URL. This method is often used for submitting sensitive information like passwords, as the data is not visible in the URL.

8. **Server Response**: The server processes the received data and sends back a response, which may include a confirmation message or an error message if the submission was unsuccessful.

Remember to handle sensitive information securely, especially when using the GET method, as the data is visible in the URL. For sensitive data like passwords, it's recommended to use the POST method for added security.