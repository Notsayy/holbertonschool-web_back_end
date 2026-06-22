#!/usr/bin/env python3
"""Basic Redis cache module."""
import redis
import uuid
from typing import Union


class Cache:
    """Redis cache class."""

    def __init__(self) -> None:
        """Initialize Redis client and clear the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis using a random key and return this key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
