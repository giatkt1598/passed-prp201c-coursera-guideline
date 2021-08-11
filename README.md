# How to pass prp201c FPTU
## Table of contents
[Review course 1: Programming for Everybody (Getting Started with Python)](#course1)

[Final Quiz](#final-quiz)

<a name="course1"></a>
## Review course 1: Programming for Everybody (Getting Started with Python)
- Variable & Expression
- Condition statement (If else)
- Function
- Loop and Iteration

## Review course 2: Python Data Structures
### Manipulate strings

    Compare strings

    lower(), 

    upper(), 

    rstrip([chars]), 

    lstrip([chars]),

    strip([chars),

    replace(old, new [,count]), 

    capitalize(), 

    center(width[, fillchar])

    endswith(suffix[, start[, end]]),

    find(sub[, start[, end]])

    len(param)

### Files

Open file:  open(filename, mode)

mode:

`"r"` - Read - Default value. Opens a file for reading, error if the file does not exist

`"a"` - Append - Opens a file for appending, creates the file if it does not exist

`"w"` - Write - Opens a file for writing, creates the file if it does not exist

`"x"` - Create - Creates the specified file, returns an error if the file exists

```python
fhand = open('mbox', 'r')
```
Read file
```python
s = fhand.read()
```
Close file, **remember close file when done if you add data to file**
```python
fhand.close()
```
For go to new line, append `"\n"`
```python
f.write("Now the file has more content!\n")
```
Example:
```python
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
```
<a name="final-quiz"></a>
### List
List is a kind of collection
```python
mylist = [1, [5, "cherry"], 'banana', "\n", 2.4, True]
print(len(mylist) # Output: 6
print(mylist[1]) # Output: [5, 'cherry']

fruits = ["apple", "banana", "cherry"]
print(",".join(fruits)) # Output: apple,banana,cherry
fruits.sort(reverse=True)
print(fruits) # Output: ['cherry', 'banana', 'apple']
```
### Dictionaries
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

*As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.*
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
thisdict["year"] = 2018
thisdict["color"] = "red"
thisdict.pop("model")
for x in thisdict:
  print(x)
mydict = thisdict.copy() # copy dictionary
```
Nested Dictionary
```bash
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
}
```
## Tuples
Tuples are like the lists but tuples are *immutable*.
Tuples are used to store multiple items in a single variable.
```python
thistuple = ("apple", "banana", "cherry")
```
How to change tuple? You can convert the tuple into a list, change the list, and convert the list back into a tuple.
```python
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
```

## Final Quiz: https://quizlet.com/521678301/prp201c-flash-cards/
