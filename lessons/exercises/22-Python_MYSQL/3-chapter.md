**Connecting to a MySQL Database:**

To use MySQL in Python scripts, the next step is to establish a connection to the desired database. All Python DB-API 2.0 modules implement a 'module_name.connect' function. For MySQL, this function is used to make the connection:

```python
db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
```

This statement connects to the MySQL database on `MY_HOST`, using the `MY_USER` as the username, `MY_PASS` as the password, and `MY_DB` as the database name. Note that the parameter for the password is 'passwd', not 'password'.

Executing this function passes the parameters to the underlying Python extension `_mysql`, allowing you to pass many MySQL-specific connection parameters through the normal connection method. For a complete list of supported connection parameters, refer to the reference section.