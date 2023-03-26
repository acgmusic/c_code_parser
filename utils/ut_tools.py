import time
import inspect


class UtClassTestTool:
    """ add print info: start/end information and the time spent on this test cases
    """
    def __init__(self, print_time=False, add_case=True):
        self.print_time = print_time
        self.add_case = add_case

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"\n{'*' * 20} {func.__name__} start {'*' * 20}\n")
            if self.print_time:
                t_start = time.time()
                func(*args, **kwargs)
                t_end = time.time()
                cost_time = round(t_end - t_start, 3)
                print(f"\n{'*' * 20} {func.__name__} end, cost[{cost_time}s] {'*' * 20}\n")
            else:
                func(*args, **kwargs)
                print(f"\n{'*' * 20} {func.__name__} end {'*' * 20}\n")
        return wrapper
