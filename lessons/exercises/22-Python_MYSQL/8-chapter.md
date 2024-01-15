**Handling Exceptions & Errors:**

In accordance with the Python DB-API, errors in MySQL are indicated by raising exceptions. The top-level exception for the MySQL package is 'MySQLdb.Error'.

Every DB-API statement has the potential to raise an exception. Therefore, it's advisable to enclose database queries within a try/except block. This applies to connections, cursor requests, and statement executions.

```python
try:
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
except MySQLdb.Error as e:
    try:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)

# Print results in comma delimited format
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"
```

In this example, the try/except block captures potential MySQL errors during the execution of the SELECT query. If an error occurs, it prints the error details. After handling the exception, you can proceed with further processing or take appropriate actions based on your application's requirements.