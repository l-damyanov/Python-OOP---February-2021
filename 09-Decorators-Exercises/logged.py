def logged(func):
    def wrapper(*args):
        result = func(*args)
        return f"you called {func.__name__}{args}\n" \
               f"it returned {result}"
    return wrapper
