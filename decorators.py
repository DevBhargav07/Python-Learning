"""
https://www.w3schools.com/python/python_decorators.asp
https://www.geeksforgeeks.org/python/decorators-in-python/
#now we will see about decorators
#decorators without arguments (2 levels)
#decorators with arguments (3 levels)

#now we will see 2 levels decorator
"""
def simple_decorator(func):
    def wrapper(name):
        print('calling the decorator function')
        say = func(name)
        print('after calling the decorator function')
        return say
    return wrapper

@simple_decorator
def say_hello_touser(name):
    print('decorator function called!')
    return "Hello {}".format(name)

print(say_hello_touser("Bhargav"))


print('\n\n\n\n')
#now we will see the 3 levels decorator

def a_repeat_decorator(times):
    def inner_decorator(func):
        def wrapper(name):
            for _ in range(times):
                print('wrapper inside print')
                result = func(name)
                print('after calling the wrapper')
            return result
        return wrapper
    return inner_decorator

@a_repeat_decorator(times=3)
def say_hello_touser(name):
    print('say hello function says hi too {}'.format(name))
    return "Hi {}".format(name)

print(say_hello_touser("Bhargav"))
