import time

def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Operation took {end_time - start_time}s")
        return result
    return wrapper