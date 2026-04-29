from typing import Callable, Any
from functools import wraps
import inspect


def cache(func: Callable) -> Callable:
    results = {}
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        key = tuple(sorted(bound.arguments.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result
        return result
    return wrapper
