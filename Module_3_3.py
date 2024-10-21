def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print('----------------------------------------------------------')

value_list = [1, 'Urban', False]
value_dict = {"a": 5, "b": "параметр b", "c": True}
print_params(*value_list)
print_params(**value_dict)
print('-------------------------------------------------------------')

value_list_2 = [555.555, 'строка в value_list_2']
print_params(*value_list_2, 42)
