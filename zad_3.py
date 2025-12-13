def liczby_parzyste(*args):
    return print(list(filter(lambda x: x % 2 == 0, args)))

liczby_parzyste(1, 4, 6, 15, 352, 222, 5221)