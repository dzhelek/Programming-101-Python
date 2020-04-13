from contextlib import contextmanager


@contextmanager
def silence_exception(exception, msg=None):
    try:
        yield
    except exception as exc:
        if msg is not None and msg != str(exc):
            raise
