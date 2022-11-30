"""
CoRoutine decorator
Allows for convenient usage without having to manually call next()

Example:

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
search.close()

Instead, you can decorate grep() with the method below, and not
need to manually call next() within the usage code.

Example:

@coroutine
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

search = grep('coroutine')
#next(search)
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
search.close()

"""

def coroutine(func):
    def start(*args, **kwargs):
        corout = func(*args, **kwargs)
        next(corout)
        return corout
    return start