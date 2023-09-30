
## Table of Contents

1. [Explanation Of The Codes](#explanation-of-the-codes)
2. [How to Generate Usernames](#how-to-generate-usernames)
    - [Step 1: Define a Function](#step-1-define-a-function)
    - [Step 2: Set Up a Collection](#step-2-set-up-a-collection)
    - [Step 3: Generate Basic Usernames](#step-3-generate-basic-usernames)
    - [Step 4: Add Unique Usernames to the Collection](#step-4-add-unique-usernames-to-the-collection)
    - [Step 5: Consider Variations](#step-5-consider-variations)
    - [Step 6: Control the Number of Usernames](#step-6-control-the-number-of-usernames)
    - [Step 7: Return the Collection](#step-7-return-the-collection)
    - [Step 8: Get User Input](#step-8-get-user-input)
    - [Step 9: Call the Function](#step-9-call-the-function)
    - [Step 10: Display Usernames](#step-10-display-usernames)
    - [Step 11: Handle Missing Information](#step-11-handle-missing-information)
    - [Step 12: Test Your Code](#step-12-test-your-code)
    - [Sample Code](#sample-code)

## Explanation of The Codes

```python
#!/usr/bin/python3
```
- This is known as a **shebang line**. It indicates that this script should be executed using the `python3` interpreter located at `/usr/bin/python3`. This is used in Unix-like systems to specify which interpreter should be used to execute the script.

```python
def generate_usernames(first_name, surname):
```
- This line defines a function named `generate_usernames` which takes two parameters: `first_name` and `surname`.

```python
    usernames = set()
```
- This initializes an empty set called `usernames`. A set is a collection of unique elements, and it's used here to store unique username suggestions.

```python
    usernames.add(f"@{first_name[:3].lower()}_{surname[:3].lower()}")
```
- This adds the first username suggestion to the set. It combines the first three characters of `first_name` and `surname` with an underscore in between, converts them to lowercase, and prepends `@`.

```python
    usernames.add(f"@{first_name.lower()}_{surname.lower()}")
```
- This adds a second username suggestion to the set. It uses the full `first_name` and `surname`, converted to lowercase, separated by an underscore, and prepends `@`.

```python
    usernames.add(f"@{first_name[0].lower()}_{surname.lower()}")
```
- This adds a third username suggestion. It uses the first character of `first_name`, converts it to lowercase, and combines it with the full `surname`, also in lowercase, separated by an underscore, and prepends `@`.

```python
    usernames.add(f"@{first_name.lower()}_{surname[:3].lower()}")
```
- This adds a fourth username suggestion. It uses the full `first_name` in lowercase, combines it with the first three characters of `surname` in lowercase, separated by an underscore, and prepends `@`.

```python
    for i in range(1, len(first_name)):
        for j in range(1, len(surname)):
```
- These lines set up nested loops. The outer loop iterates over indices `i` from 1 to the length of `first_name`, and the inner loop iterates over indices `j` from 1 to the length of `surname`.

```python
            usernames.add(f"@{first_name[:i].lower()}_{surname[:j].lower()}")
```
- Inside the loops, this line generates additional username suggestions using slices of `first_name` and `surname`, converting them to lowercase, and combining them with an underscore in between, all prepended with `@`.

```python
            if len(usernames) >= 15:
                return usernames
```
- If the number of generated usernames reaches or exceeds 15, the function returns the set of usernames. This is done to ensure we don't generate too many usernames.

```python
    return usernames
```
- After the loops, if 15 usernames have not yet been generated, the function returns the set of usernames.

```python
first_name = input("First Name: ")
surname = input("Surname: ")
```
- These lines prompt the user for their first name and surname, and assign the input to the variables `first_name` and `surname`.

```python
if first_name and surname:
```
- This line checks if both `first_name` and `surname` are non-empty (i.e., if the user provided both names).

```python
    usernames = generate_usernames(first_name, surname)
```
- If both names are provided, this line calls the `generate_usernames` function with the provided names, and assigns the resulting set of usernames to the variable `usernames`.

```python
    print(f"Your username suggestions are:")
    for username in usernames:
        print(username)
```
- This block of code prints a message indicating that username suggestions are about to be displayed, and then iterates over each username in the `usernames` set, printing them one by one.

```python
else:
    print("Please provide both your first name and surname.")
```
- If either `first_name` or `surname` is empty (i.e., if the user did not provide both names), this line prints a message asking the user to provide both names.

I hope this breakdown helps you understand the code I used in the project. Contact me if you have any further questions!

---

## How to Generate Usernames

### Step 1: Define a Function
- Start by defining a function named `generate_usernames`.

### Step 2: Set Up a Collection
- Create a collection to store the generated usernames. You can use a set, which ensures uniqueness.

### Step 3: Generate Basic Usernames
- Begin by generating basic usernames based on the provided first name and surname. For example, you can create usernames using combinations of the first three characters of each name.

### Step 4: Add Unique Usernames to the Collection
- Add each generated username to the collection. Be sure to format it with a prefix (like `@`) and separate the first name and surname with an underscore.

### Step 5: Consider Variations
- Think about other possible variations for usernames. For example, you might want to use the entire first name, only the first character, or a mix of both.

### Step 6: Control the Number of Usernames
- Decide on a limit for the number of usernames you want to generate. You can use a loop and an `if` statement to ensure you generate a reasonable number but it can be any number depending on personal preferences.

### Step 7: Return the Collection
- At the end of the function, return the collection of generated usernames.

### Step 8: Get User Input
- Ask the user for their first name and surname using the `input` function. Store the inputs in variables.

### Step 9: Call the Function
- Call the `generate_usernames` function with the provided first name and surname.

### Step 10: Display Usernames
- Print out the generated usernames for the user to see.

### Step 11: Handle Missing Information
- Add checks to make sure the user provides both their first name and surname. If not, prompt them to provide the missing information.

### Step 12: Test Your Code
- Run your code with different inputs to make sure it's working as expected.

### Sample Code:

You can use this code as a sample code to start writing your own 

```python
def generate_usernames(first_name, surname):
    usernames = set()
    # Generate usernames and add to the set
    # ...
    return usernames

# Get user input
first_name = input("First Name: ")
surname = input("Surname: ")

if first_name and surname:
    usernames = generate_usernames(first_name, surname)
    if len(usernames) > 0:
        print(f"Your username suggestions are:")
        for username in usernames:
            print(username)
    else:
        print("No usernames generated.")
else:
    print("Please provide both your first name and surname.")
```
