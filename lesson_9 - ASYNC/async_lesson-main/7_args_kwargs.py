def foo(*args):
    print(args)
    print(len(args))

def foo_2(**kwargs):
    return kwargs


lst = ['Bob', 2, 3]
foo(*lst)
# print(foo_2(my_list = lst))


