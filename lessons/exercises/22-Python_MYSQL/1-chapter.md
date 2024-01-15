**Introduction to MySQL in Python:**

**MySQL Python Components:**
1. **_mysql:** Wrapper library.
2. **MySQLdb:** DB-API 2.0 module for MySQL in Python.

**Standards and PEP 249:**
- MySQLdb follows the standards outlined in Python PEP 249, promoting consistent database development in Python.
- Similar concept to JDBC in Java.

**Installation:**
- For Linux, check distribution for precompiled binaries or use an installer.
- Windows: Download installer from the Sourceforge project for MySQL Python.
- Mac OSX: Check PythonMac.org for binaries.
- Avoid source installation unless experienced. Windows source installation via Cygwin is not recommended.
- Prerequisites: Python 2.3.4 or greater with development files, MySQL 4.0 or greater libraries with development files, zlib with development files.

**Source Installation:**
```bash
tar zxf MySQL-python-x.x.x.tar.gz
cd MySQL-python-x.x.x
python setup.py build
sudo python setup.py install # or su first
```

**Testing Installation:**
```python
python
>>> import MySQLdb
```

**Usage in Scripts:**
- Import MySQLdb at the top of your script to use the MySQLdb module in your packages.

**Next Steps:**
The next section will cover establishing a connection to a MySQL database.