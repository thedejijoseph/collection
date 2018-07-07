# yield is used for/with generators

def gear(n):
    teeth = [n**x for x in range(n)]
    yield teeth

# the function above becomes a generator
# returning the desired result (i dunno)
# prebuilt or generated on the fly

# it came to me when i did some stuffs with
# itertools.permutations
