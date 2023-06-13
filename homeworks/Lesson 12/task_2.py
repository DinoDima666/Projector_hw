def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__} {str(e)}")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
# > Found 1 error during execution of your function: KeyError no such key as foo

some_function_with_risky_operation({'key': 'bar'})
# > bar
