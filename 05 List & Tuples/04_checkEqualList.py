def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True

# Example usage:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(are_lists_equal(list1, list2))  

list3 = [1, 2, 3]
list4 = [3, 2, 1]
print(are_lists_equal(list3, list4))  
