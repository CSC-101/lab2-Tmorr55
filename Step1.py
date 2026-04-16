def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? smallest(3,2) and smallest(2,2)
    else:
        return m

first = smallest(3, 2)       # What is the value of first? first = 2
second = smallest(2, 2)      # What is the value of second? second = 2
                                    # Is this a reasonable result? Why or why not? yes because else -> n >= m and 2 >= 2
print()