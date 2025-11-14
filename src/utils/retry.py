import time

def retry_with_delay(func, retries=1, delay=1):
    """
    Retry wrapper: retry function calls with delay up to retries times.
    """
    def wrapper(*args, **kwargs):
        attempt = 0
        while attempt <= retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                attempt += 1
                if attempt > retries:
                    raise e
                time.sleep(delay)
    return wrapper
