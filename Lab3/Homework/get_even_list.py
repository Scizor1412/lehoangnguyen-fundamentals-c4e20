def get_even_list(l):
    new_list = []
    for i in l:
        if i % 2 ==0:
            new_list.append(i)
    return new_list
result = get_even_list([1, 2, 4, 5, 7, 8, 44, 55, 7, 77, 5])
print (result)