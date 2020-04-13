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
