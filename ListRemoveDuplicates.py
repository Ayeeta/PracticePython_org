def removeDupl(anylist):
    newlist = []
    for item in anylist:
        if item not in newlist:
            newlist.append(item)
    return newlist




print(removeDupl(['a','b','b','c','c',1,1]))
