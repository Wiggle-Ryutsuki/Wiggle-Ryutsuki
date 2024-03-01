# Maimoona Aziz

class Jar:
    """Initialize a cookie jar with the given capacity,
    If capacity is not a positive int, __init__ should raise ValueError."""

    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a positive integer")
        self._capacity = capacity
        self._cookies = 0


    """Return a str with n🍪, where n is the number
    of cookies in the cookie jar."""

    def __str__(self):
        return "🍪" * self._cookies


    """Add n cookies to the cookie jar.
    If exceeded cookie jars capacity, deposit should raise a ValueError."""

    def deposit(self, n):
        if (self._cookies + n) > self._capacity:
            raise ValueError("Exceeds capacity")
        self._cookies += n


    """Should remove n cookies from the cookie jar.
    If there arent that many cookies in the cookie jar,
    withdraw should instead raise a ValueError."""

    def withdraw(self, n):
        if (n) > self._cookies:
            raise ValueError("Not enough cookies")
        self._cookies -= n


    """Should return the cookie jars capacity."""
    @property
    def capacity(self):
        return self._capacity


    """Should return the number of cookies actually in the cookie jar,
    initially 0."""
    @property
    def size(self):
        return self._cookies
