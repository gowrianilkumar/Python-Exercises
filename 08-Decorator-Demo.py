import time
from functools import wraps

def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"--> Running {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"--> {func.__name__} ran in {elapsed_time:.6f} seconds")
        return result
    return wrapper


@time_this
def sleeper_func(sleeptime):
    print(f'sleeping for {sleeptime}')
    time.sleep(sleeptime)
    return 'Woke up!'


sleeper_func(2)
