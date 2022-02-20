""" this is my first module & script """

def my_func1(x):
    return print(x**2)

def my_func2(y):
    return print(*y)

if __name__ == '__main__':  # output-generating statements are here
    print('hello') 
    my_func1(3)
    my_func2("clarusway")