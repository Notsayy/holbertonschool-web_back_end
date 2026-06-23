#!/usr/bin/env python3
"""Basic Redis cache module."""
import redis
import uuid
from functools import wraps
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """Count how many times a Cache method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call counter and execute the method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a Cache method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Record input arguments and output in Redis lists."""
        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a particular function."""
    redis_client = method.__self__._redis
    method_name = method.__qualname__

    count = redis_client.get(method_name)
    count_int = int(count.decode("utf-8")) if count else 0

    print("{} was called {} times:".format(method_name, count_int))

    inputs = redis_client.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = redis_client.lrange("{}:outputs".format(method_name), 0, -1)

    for input_data, output_data in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            method_name,
            input_data.decode("utf-8"),
            output_data.decode("utf-8")
        ))


class Cache:
    """Store and retrieve data from a Redis database."""

    def __init__(self) -> None:
        """Initialize the Redis client and clear the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally convert it."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a Redis value and decode it as a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a Redis value and convert it to an integer."""
        return self.get(key, fn=int)