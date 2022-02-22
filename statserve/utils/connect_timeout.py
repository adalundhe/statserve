import time
import logging
import functools


def connect_with_retry(wait_buffer=5,timeout_threshold=30): 
    def retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            elapsed = 0
            result = None
            while elapsed < timeout_threshold:
                try:
                    result = func(*args, **kwargs)
                    break
                except Exception as execution_exception:
                    result = None
                    logging.error('Error: Connection attempt failed. Retrying in {wait_buffer}'.format(wait_buffer=wait_buffer))
                    logging.error(str(execution_exception))
                time.sleep(wait_buffer)
                current = time.time()
                elapsed = current - start

            return result
        return wrapper
    return retry