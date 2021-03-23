def tags(tag):
    def decorator(func):
        def wrapper(*args):
            body = func(*args)
            return f"<{tag}>{body}</{tag}>"
        return wrapper
    return decorator
