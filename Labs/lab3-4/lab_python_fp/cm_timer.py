import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(elapsed_time)

class cm_timer_2:
    @contextmanager
    def maneger(self):
        start_time = time.time()
        yield
        elapsed_time = time.time() - start_time
        print(elapsed_time)