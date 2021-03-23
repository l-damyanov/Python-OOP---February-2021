def type_check(type_el):
    def decorator(func):
        def wrapper(*args):
            func_type = func(*args)
            for el in args:
                if type(el) != type_el:
                    return "Bad Type"
            return func_type
        return wrapper
    return decorator
