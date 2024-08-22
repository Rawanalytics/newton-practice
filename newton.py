def function(x):
    return x**2


def fist(x):
    delta = 0.0001
    first = 0
    first = (function(x + delta) - function(x)) / delta
    return first


def second(x):
    delta = 0.0001
    second = 0
    second = (fist(x + delta) - fist(x)) / delta
    return second


def Newton(start, function):
    x = start
    delta = 0.0001
    x_t = start + 10

    while abs(x_t - x) > delta:
        copy = x_t

        first_derivative = fist(x)
        second_derivative = second(x)
        x_t = x - first_derivative / second_derivative

        x = copy

        print(x_t)
