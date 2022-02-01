original_list = input("Enter a string")
def double_list(original_list):
    second_list = []
    original_list = list(original_list.split())
    print('original list: ', original_list)
    for a in original_list:
        for i in range (2):
            second_list.append(a)
    print('double list: ',second_list) 

double_list(original_list)
