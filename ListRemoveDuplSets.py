def RemoveDup(anylist):
    anylist = set(anylist)
    return list(anylist)

print(RemoveDup(['a','a','b','b','c','c']))