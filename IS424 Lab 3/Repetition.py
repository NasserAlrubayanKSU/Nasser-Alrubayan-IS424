def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator


x = int(input("Enter a number of repetitions: "))

@repeat(x)
def hello():
    print('Hello')

hello()