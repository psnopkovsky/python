def my_func_v1(x, y):
    if (type(x) == int or type(x) == float) and x >= 0:
        if type(y) == int and y < 0:
            result = x ** y
            return result
        else:
            print('Переменная "y" не соотвествует условиям: должна быть целым отрицательным числом!')
    else:
        print('Переменная "x" не соотвествует условиям: должна быть положительным действительным числом!')

def my_func_v2(x, y):
    if (type(x) == int or type(x) == float) and x >= 0:
        if type(y) == int and y < 0:
            result = x
            for i in range(abs(y)-1):
                result *= x
            return (1 / result)
        else:
            print('Переменная "y" не соотвествует условиям: должна быть целым отрицательным числом!')
    else:
        print('Переменная "x" не соотвествует условиям: должна быть положительным действительным числом!')

print(my_func_v1(4, -5))
print(my_func_v2(4, -5))