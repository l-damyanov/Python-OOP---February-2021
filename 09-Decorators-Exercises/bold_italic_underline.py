def make_bold(func):
    def wrapper(*args):
        word = func(*args)
        return f"<b>{word}</b>"
    return wrapper

def make_italic(func):
    def wrapper(*args):
        word = func(*args)
        return f"<i>{word}</i>"
    return wrapper

def make_underline(func):
    def wrapper(*args):
        word = func(*args)
        return f"<u>{word}</u>"
    return wrapper
