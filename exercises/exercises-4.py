# def func(a,b, c=10, d=11):
#     print(a,b,c,d)

# func(1,2)
# func(1,2,3)
# func(1,2,3,4)

# def func(*args):
#     print(args)

# func(1)
# func(1,2)
# func(1,2,3)

# def func(a, b, **kwargs):
#     print(a,b, kwargs)
#     print(a,b, kwargs['c'], kwargs['d'])

# func(1,2, c=3,d=4)

def func(a, b, *args, name='John', **kwargs):
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('args = {}'.format(args)) #tuple
    print('name = {}'.format(name))
    print('kwargs = {}'.format(kwargs)) #dict

func(1,2,3,4,5, 'a', name='Anna', age='34', email='anna@email.com')





