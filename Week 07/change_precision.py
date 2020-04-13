from contextlib import contextmanager
from decimal import getcontext


@contextmanager
def change_precision(precision):
    try:
        default_precision = getcontext().prec
        getcontext().prec = precision
        yield
    except Exception:
        raise
    finally:
        getcontext().prec = default_precision

class change_precision:
    def __init__(self, precision):
        self.precision = precision

    def __enter__(self):
        self.default_precision = getcontext().prec
        getcontext().prec = self.precision

        return self

    def __exit__(self, *exc_args):
        getcontext().prec = self.default_precision
