
## Setting up a Python  environment
* You can use pythonanywhere.com to get a free Linux server to update & run these scripts

## General Programming in Python
* https://github.com/gregmalcolm/python_koans
* https://hackr.io/tutorials/learn-python : 19 hour course, unnecessary

## Algorithmic coding with Python
* https://medium.com/cheat-sheets/cheat-sheet-for-competitive-programming-with-python-3-0477b685d8cd
* https://www.geeksforgeeks.org/python/python-sorted-containers-an-introduction/
* https://www.pythoncheatsheet.org/cheatsheet/
* http://numpy.org/doc/stable/user/absolute_beginners.html
* [Graphlib](https://docs.python.org/3/library/graphlib.html) can do a topological sort for you
* SciPy.sparse can do Dijkstra’s
* [Collections](https://docs.python.org/3/library/collections.html)
* [Itertools](https://docs.python.org/3/library/itertools.html)
* Recursion with memoization: Use [functools.lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache) and set maxsize to whatever amount you think is appropriate. When the cache gets full, it will then discard cached values

## Learning API development with Python
* FastAPI
* Flask

## Snippets
### Default values in a dictionary
If you want to use a dictionary to count occurences of a word, you will first need to check if the word exists in the dictionary. 
So, you protect yourself by catching keys that have not been added to the dictionary, and pre-add them. You could also use get() to protect yourself, as:
```
animals_dict = {}
for animal in animals_list:
  animals_dict[animal] = animals_dict.get(animal,0) + 1
```
That works pretty well.

Defaultdict basically allows you to initialize unseen keys using a function, so we could rewrite the above as:

```
from collections import defaultdict
animals_dict = defaultdict(int) # or, equivalently, defaultdict(lambda :0)
for animal in animals_list:
  animals_dict[animal] += 1
```

### You can use Dictionaries to hold objects instead of defining classes

### Defining classes
```
from dataclasses import dataclass
from typing import NamedTuple

# Note that the type hints are used only by static analysis tools. Python will let you pass any object here
class Person(NamedTuple):  # immutable
  name: str
  age: int


@dataclass  #  automatically generates special methods like __init__, __repr__, __eq__ etc
class Person:
  name: str
  age: int

person = Person(name="Mike", age=45)
print(f"X type: {type(person.name)}")
```



