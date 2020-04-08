def silence(file):
    def inner(func):
        def function(*args):
            try:
                func(*args)
            except Exception as exc:
                with open(file, 'w') as f:
                    f.write(str(exc))
        return function
    return inner
