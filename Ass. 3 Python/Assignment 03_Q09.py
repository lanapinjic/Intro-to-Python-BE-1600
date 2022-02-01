list_1 = []
def remove_dups(list_2):
    print("orginial list: ", list_2)
    for i in list_2:
        if i not in list_1:
            list_1.append(i)
    return list_1

remove_dups(['be', 'be','is', 'not', 'or', 'question', 'that', 'the', 'to', 'to'])
print("list after removing duplicates: ", list_1)
