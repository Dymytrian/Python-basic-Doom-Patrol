# 1. double_result
# This decorator function should return the result of another function multiplied by two
#def double_result(func):
    # return function result multiplied by two
    #pass

def double_result(func):
    def inner(*args):


        result = 2 * func(*args)
        print(result)
        #print(args)
    return inner

@double_result
def add(a, b,):
    return a + b
add(5, 5)




# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

#def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    #pass

def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 != 0:
                return func(*args)
            else:
                return ("Please use only odd numbers!")

    return inner

@only_odd_parameters
def add(a, b):
    return a + b
print(add(5, 5))
print(add(4, 5))


@only_odd_parameters
def multiply(a, b, c, d, e):
     return a * b * c * d * e
print(multiply(5, 5, 8, 7, 5))
print(multiply(10, 20, 41, 50, 60))




# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    def wraper(*args):
        result = func(*args)

        print(f"you called {func.__name__}{args}")
        print("it returned",result)
    return wraper


@logged
def func(*args):
    return 3 + len(args)

func(4, 4, 4)




# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def type_decorator(func):
        def inner_func(num):
            if type(num) == correct_type:
                return func(num)
            else:
                return f"Wrong Type: {type(num)}"

        return inner_func

    return type_decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
