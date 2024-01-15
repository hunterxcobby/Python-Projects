**Obtaining Query Results:**

After executing a SELECT statement, you can obtain results using one of these methods:

**Method 1: Fetch All-at-Once**
```python
cur.execute("SELECT * FROM song")
rows = cur.fetchall()
for row in rows:
    for col in row:
        print "%s," % col
    print "\n"
```
This method fetches all results at once, allowing you to iterate over the rows and columns and print them. Adjust the processing logic based on your requirements.

**Method 2: Fetch One-at-a-Time**
```python
cur.execute("SELECT * FROM song WHERE id = 1")
print "Id: %s -- Title: %s" % cur.fetchone()
```
This method fetches one row at a time. In this example, it prints the ID and title of the first row.

There is no inherently better method; use the one that best suits your specific needs.

**Note:** If you're using the cursor class "CursorUseResultMixIn" or its subclasses, be cautious. These cursor classes store results on the server and provide them to your program as requested. Ensure you retrieve all results and close the cursor before executing additional queries. Refer to the reference section for more information on cursor classes.