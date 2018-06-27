# Range divisible by 7 but are not a multiple of 5
def div(min_value, max_value):
    my_list = []
    for i in range(min_value, max_value):
        if (i % 7 == 0) and (i % 5 != 0):
            my_list.append(i)
    return my_list

# Factorial
def fact(x):
    num = 1
    for i in range(1, x + 1):
        num = num * i
    return num

# Flatten List
def flatten(lst):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])


# Greatest Common Divisor
def gcd(my_list):
    while len(my_list) > 1:
        a = my_list[len(my_list) - 2]
        b = my_list[len(my_list) - 1]
        my_list = my_list[:len(my_list) - 2]

        while a:
            a, b = b % a, a

        my_list.append(b)

    return abs(b)