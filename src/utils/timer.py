import time


def measure_execution_time(function, *args, **kwargs):

    start = time.perf_counter()

    function(*args, **kwargs)

    end = time.perf_counter()

    return end - start