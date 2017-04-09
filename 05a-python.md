	# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples both store a series of values which are indexed by numbers with the first entry starting at 0 and so on, the difference comes in the fact that 
lists are mutable (i.e. it's values(elements) are changeable) whereas a tuple's values are immutable(unchangeable)
Tuples work as dictionary keys and not lists because the hash function is used to search different key values and if a mutable container of values i.e. a list is used as a dictionary key and hypothetically the contents of that file are changed then this would change the 
hash value of the key which would produce errors upon lookup. Whereas an immutable list (tuples) produces a unique hash value from it's contents and will stay that way for referral and lookup.


---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets by definition are an unordered collection of unique and immutable objects i.e. hashable objects, therefore sets cannot contain lists. Mathematically elements in a set "belong" in that set, therefore there can't be duplicates of the same elements and this applies to python sets too.
Lists are containers of ordered values which are mutable. Since they are just containers and are ordered, duplicate values can be entered.

list: a = [12, 34, 56, 78]
set: b = set([1, 2, 3, 4, 5])
or can create an empty set: c = set() then use add function to add values, e.g. c.add("mouse") c.add("duck")

In terms of performance i.e. time taken to iterate through objects in the 2 different types of containers
The timeit function can be used to check time taken to iterate.
Results show that lists are faster when iterating over general values(including duplicates). However if dealing with unique values and the goal is to check for a value's existence, sets are faster.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda allows us to define anonymous functions without naming them per se, this enables it to be used to define functions as parameters within a function.

mylist = ['Happy', 'sad', 'angry', 'Attraction']
sorted(mylist, 	key = lambda word: word.lower())

first argument in sorted function points towards created list. 'key' keyword specifies a function that defines how to sort the given items in the list.
lambda enables the in-line definition of a sorting function, in this case being the lower casing of the words which removes the priority of words beginning with an upper case letter.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are equivalents to lambda in the sense that a list can be created by applying a specified formula within a specified range. Instead of performing a newly defined function on a list, list comprehensions essentially create lists using a specified formula using "for" and "if".

List comprehension:
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]

Creates a list using the specified conditions/function within a specified range

Map:
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda c: (float(9)/5)*c+32, Celsius)

Applies a specified function to all elements of an iterable and returns the result.

Filter:
Fahrenheit = [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
Fahrenheitunder100 = list(filter(lambda c: c<100, Fahrenheit))

Filters an interable based on the condition provided as the first argument and returns only the values which satisfied the condition resulting in a True boolean value.

Set comprehension:
Fahrenheitunder100 = { for x in Fahrenheit if x<100 }

Similar to list comprehension wherein a set is created from given conditions

Dictionary comprehension:

d = { Celsius:Fahrenheit for Celsius in Celsius }

Creates a dictionary using the specified keys and values within an iterable.
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





