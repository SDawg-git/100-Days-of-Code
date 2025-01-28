# save this as app.py
import time
from functools import wraps
from flask import Flask

app = Flask(__name__)

#print(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

# if __name__ == "__main__":
#     app.run()

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#                                   #Step by step breakdown:
#inner = outer_function()           #this calls the outer function, and saves the REFERENCE to "nested_function" since that's the return
# inner()                           #now since this has the reference to the nested_function, if you call it with () you get the inner function
#outer_function()()                 #this does 2 in one, calls the first function then uses the reference to call the other


#python decorator function





def decorator_function(function):

    def wrapper_function():                                     #that's how a decorator works
        function()

    return wrapper_function





def delay_decorator(function):
    print("this comes first")
    #@wraps(function)                           #can use functools to keep the original function name when calling in passed function
    def wrapper_function():
        time.sleep(2)
        function()
        print(function.__name__)        #now since you've passed in the "say_hello" function, when you print out the name it'll say "hello_function"
    return wrapper_function

@delay_decorator                                       #don't have to pass the function into the wrapper, calling it above the function enough
def say_hello():                                       #also known as syntactic sugar?
    print("hello")                                     #can instead do decorated_function = delay_decorator(say_hello)
                                                       #decorated_function()
    print(say_hello.__name__)              #the reason this returns "wrapper_function" instead of "say_hello" is because you're
                                           #actually calling the "wrapper_function", not "say_hello".


def say_greeting():
    print("How are you?")

say_hello()
