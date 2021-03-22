import functools


def multiply(times):

    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result * times
        return wrapper
    return decorator
