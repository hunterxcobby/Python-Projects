import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)
        tmp_file.seek(0)  # Reset file pointer to the beginning for reading later

    # Retrieve the path of the temporary file
        temp_file_path = tmp_file.name
        print("Temporary file path:", temp_file_path)
    # Now you can access the temporary file for further processing
    with open(tmp_file.name, 'r') as html_file:
        html = html_file.read()
        print("Successfully stored...")