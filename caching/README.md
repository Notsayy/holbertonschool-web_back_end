# Caching

This project explores different caching algorithms and their implementations in Python. Each caching system inherits from a base class and implements specific eviction policies when the cache reaches its maximum capacity.

## Project Context

This project is part of the Holberton School curriculum, focusing on backend development and data structure optimization. The goal is to understand and implement various cache replacement policies used in computer systems and applications.

## Learning Objectives

- Understand what a caching system is
- Implement different cache replacement policies (FIFO, LIFO, LRU, MRU, LFU)
- Understand the purpose and limitations of caching systems
- Know when to use each caching algorithm based on use cases

## Requirements

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the `pycodestyle` style (version 2.5)
- All files must be executable
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation
- Documentation must be real sentences explaining the purpose of the module, class, or method

## Base Class

All caching classes inherit from `BaseCaching`:

```python
class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Author

[Notsayy](https://github.com/Notsayy)
