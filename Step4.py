def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated. First
    elif len(L) > 1:                                  #   and what are the values being added? 4 + 2 + 3
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated. First and Third
    elif len(L) > 0:                                  #   and what are the values being added? 4 + 2 and 7 + 4
        result = len(L[0])                            # For which call below is this statement evaluated. First, Second, and Third
    else:                                             # and what are the values being added? 4, 10, and 7
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()