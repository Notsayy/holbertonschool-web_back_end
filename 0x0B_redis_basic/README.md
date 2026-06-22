# Redis basic

This project introduces basic Redis usage with Python. It focuses on connecting to a local Redis server, storing simple values, and building a small cache class with `redis-py`.

## Learning objectives

- Use Redis for basic operations.
- Use Redis as a simple cache.
- Practice Python class design, type annotations, and documentation.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- Redis server installed and running
- Code style checked with `pycodestyle 2.5`
- All modules, classes, and methods documented
- All functions and methods type-annotated

## Installation

```bash
sudo apt-get -y install redis-server
pip3 install redis
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
service redis-server start
```

## Project structure

- `exercise.py`: contains the `Cache` class and Redis-related methods.
- `main.py`: local test file used to check behavior.
- `README.md`: project description and setup instructions.

## Example

```python
#!/usr/bin/env python3
import redis

Cache = __import__('exercise').Cache

cache = Cache()
key = cache.store(b"hello")
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

Expected output:

```bash
<random-uuid>
b'hello'
```

## Author

[Notsayy](https://github.com/Notsayy)
