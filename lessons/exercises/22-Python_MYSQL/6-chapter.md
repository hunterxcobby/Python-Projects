**Executing MySQL Queries in Python:**

Executing queries in MySQL Python is straightforward. Using your cursor object, you call the 'execute' function. This function requires the query as its first parameter. If the query involves substitutions, you provide a second parameter, a tuple containing the values for substitution.

**Example 1: Create Table**
```python
cur.execute("CREATE TABLE song (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL)")
```
This example demonstrates the execution of a basic query without any parameters, creating a table named 'song.'

**Example 2: Execute Insert / Single Substitution Query**
```python
songs = ('Purple Haze', 'All Along the Watch Tower', 'Foxy Lady')
for song in songs:
    cur.execute("INSERT INTO song (title) VALUES (%s)", (song,))
    print "Auto Increment ID:", cur.lastrowid
```
Here, a query is executed with parameters, inserting songs into the 'song' table, and retrieving the auto-incremented ID.

**Example 3: Multiple Substitution Query**
```python
cur.execute("SELECT * FROM song WHERE id = %s or id = %s", (1, 2))
```
When there are multiple parameters to substitute, use a tuple to enclose all parameters for substitution. The parameters are substituted from left to right.

**Example 4: Execute Select**
```python
numrows = cur.execute("SELECT * FROM song")
print "Selected %s rows" % numrows
print "Selected %s rows" % cur.rowcount
```
Executing select queries is simple. You can obtain the number of rows returned either by saving the return value from the execute statement or by using the 'rowcount' attribute from the cursor object, following the Python DB-API 2.0 convention. The latter is preferred for database portability.