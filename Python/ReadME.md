
## Setting up a Python  environment
* You can use pythonanywhere.com to get a free Linux server to update & run these scripts

## Syntax cheatsheet 
* https://devhints.io/python
* https://roadmap.sh/python


## General Programming in Python
* https://github.com/gregmalcolm/python_koans
* https://hackr.io/tutorials/learn-python : 19 hour course, unnecessary

## Algorithmic coding with Python
* Inbuilt collections: https://docs.python.org/3/library/stdtypes.html
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
* https://fastapi.tiangolo.com/advanced/websockets/#create-a-websocket

## Concurrency in Python
[SuperFastPython](https://superfastpython.com/python-concurrency-choose-api/) is an amazing intro. I have my notes on [Google docs](https://docs.google.com/document/d/1PC2y8loXZl0buptQjEV-nrxhVpVLAhQNANQZpXbWJI8/edit?tab=t.m3o8i6jwtzt5).

Start with a list of problems you want to solve. Then determine the correct programming paradigm, then pick the library.
Python has no inbuilt equivalent to the actor model (goroutines + channels).  
Python released a new binary with CPython 3.13 that can disable the GIL. The default version includes the GIL, so assume it's still there.  
Python has libraries to support multiple paradigms:
1.Threading module (is primitive, but interviews focus on this)
2. ThreadLocal, RLock, Semaphore, Condition, Event, Timer Thread, Thread Barrier, Queue for blocking reads,
Multiprocessing (true parallelism),
3. Thread pools / Executor frameworks (concurrent.futures.ThreadPoolExecutor, ProcessPoolExecutor)
4. asyncio (high I/O concurrency using co-routines. Don't use with requests bc that's synchronous calls), 
5. data-parallel libraries (Joblib, NumPy, PyTorch),
6. structured concurrency (asyncio.TaskGroup (Python 3.11+))
7. Shared-memory threading (threading, subject to the GIL)

Resources:
* https://superfastpython.com/learning-paths/ OR https://superfastpython.com/tutorial-archive.html 
* https://algomaster.io/learn/concurrency-interview
* https://codesignal.com/learn/courses/concurrency-async-io
* https://superfastpython.com/python-concurrency-choose-api/ has a lot of rave reviews on Reddit
* https://www.xanthium.in/creating-threads-sharing-synchronizing-data-using-queue-lock-semaphore-python#src
* https://pymotw.com/3/concurrent.futures/index.html

### Best practices for concurrency
from https://superfastpython.com/threading-in-python/ 
* Use context managers — Prefer with lock: / with semaphore: so synchronization primitives are released even if an exception occurs.
* You can also use finally if you are reading/writing from queues
* Use timeouts when waiting — Put timeouts on blocking operations such as lock.acquire(), thread.join(), and condition.wait() so threads cannot wait forever.
* Use a mutex to protect critical sections — Protect shared mutable state with threading.Lock to prevent race conditions.
* Acquire locks in a consistent order — If code needs multiple locks, always acquire them in the same order to reduce the risk of deadlocks.

## Requests Library
Sending a request to reboot a server:
```
def reboot_server(port):
    try:
        response = requests.post(
            f"{BASE_URL}/reboot",
            json={"port": port},
            timeout=TIMEOUT_SECONDS,
        )

        response.raise_for_status()
        data = response.json()

        result = data.get("result")
        reason = data.get("reason", "")

        print(f"{serial}: {result} - {reason}")

    except requests.Timeout:
        print(f"{serial}: failed - request timed out")

    except requests.ConnectionError:
        print(f"{serial}: failed - could not connect to server")

    except requests.HTTPError as e:
        print(f"{serial}: failed - HTTP {e.response.status_code}")

    except requests.JSONDecodeError:
        print(f"{serial}: failed - invalid JSON response")
```

Sending a request with OAuth token in the header

```
import requests

# 1. Get OAuth token
token_response = requests.post(
    "https://auth.example.com/oauth/token",
    data={
        "grant_type": "client_credentials",
        "client_id": "my-client-id",
        "client_secret": "my-client-secret",
    },
)

token = token_response.json()["access_token"]

# 2. Call the API using the token
r = requests.post(
    "http://localhost:3000",
    json={"message": "whats your name"},
    headers={"Authorization": f"Bearer {token}"},
)

name = r.json()["reply"]
print(f"hi {name.lower()}")
```

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
Implement serialization:
class Result:
    def __init__(self, job_id: int, result_code: int):
        self.job_id = job_id
        self.result_code = result_code

    def __str__(self):
        return f"code = {self.result_code}"




