def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for i in reversed(range(len(L))):
        if f(L[i]) == False:
            L.pop(i)
    return len(L)

run_satisfiesF(L, satisfiesF)