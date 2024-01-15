To install the MySQLdb module in Python, you can use the following steps:

### Linux (Ubuntu example):
```bash
# Update package index
sudo apt-get update

# Install Python development files
sudo apt-get install python-dev

# Install MySQL client and development files
sudo apt-get install mysql-client libmysqlclient-dev

# Install MySQLdb using pip
pip install mysqlclient
```

### Windows:
- Download the MySQLdb installer from the [official Sourceforge project for MySQL Python](https://sourceforge.net/projects/mysql-python/).
- Run the installer, and it should guide you through the installation process.

### Mac OSX:
- Check if there are precompiled binaries on [PythonMac.org](https://pythonmac.org/packages/py25-fat/index.html) for your specific version.
- Alternatively, you can use Homebrew to install MySQL and then install the MySQLdb package using pip.

### Using pip directly (cross-platform):
```bash
pip install mysqlclient
```

After installing, you can test the installation by opening a Python interactive shell and importing MySQLdb:
```python
python
>>> import MySQLdb
```

If the import statement runs without errors, the MySQLdb module is successfully installed and ready for use.