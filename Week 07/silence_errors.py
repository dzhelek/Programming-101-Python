from contextlib import contextmanager


@contextmanager
def silence_exception(exception, msg=None):
    try:
        yield
    except exception as exc:
        if msg is not None and msg != str(exc):
            raise


class silence_exception:
    def __init__(self, exception, msg=None):
        self.exception = exception
        self.msg = msg
        self.raising = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.exception == exc_type:
            if self.msg is not None and self.msg != str(exc_value):
                return False
            else:
                return True
        else:
            return False
