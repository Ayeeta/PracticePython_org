#Linear Search
def ElementSearch(ordered_list, search_elem):
    if search_elem in ordered_list:
        return True
    return False


o_list = [1,2,3,4,6,8,9]
print(ElementSearch(o_list, 4))
print(ElementSearch(o_list, 5))


#Using Binary Search
def find(ordered_list2, search_elem):    
    result = len(ordered_list2)//2   
    if search_elem in ordered_list2[0:result]:
        return True
    elif search_elem in ordered_list2[result:]:
        return True
    return False

print("=====================")
print('Using Binary Search')
print(find(o_list, 4))
print(find(o_list, 5))


