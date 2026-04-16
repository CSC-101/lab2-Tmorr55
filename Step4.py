def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? "this", "is", "confusing", "code."
         # What are the values of first and second at this point? "words, Avoid" and "words, such."
         # What happened? When first was call, Avoid became the last word, then when second was called, such. replaced Avoid as the last word
print()   