# лаб1 решение биквадратного уравнения
# уравнение вида: a*(x*x) + b*x + c = 0
# вариант с доп заданием

print('\n\tШамаилов Максим, ИУ5-53 \n')

def discr_func(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError as VE:
        print(VE)
    except NameError: # as NE
        print("Ошибка ввода: допустимы только числа")
    else:
        d = b**2 - 4*a*c
        if d > 0:
            print("D = ", d)
            x1 = (-b - d**0.5)/2*a
            x2 = (-b + d**0.5)/2*a
            print(x1, x2, sep="; ")
            print("Решенное уравнение:")
            print(f'{a}x^2 + {b}x + {c} = 0\n')
        elif d == 0:
            print("D = ", d) 
            x = (-b)/(2*a)
            print(x)
            print("Решенное уравнение:")
            print(f'{a}x^2 + {b}x + {c} = 0\n')
        elif d < 0:
            print("D = ", d)
            print("нет решений ")
    finally:
        print("=====================\nЗавершение работы программы\n=====================")

print(discr_func(2, 68, 2))