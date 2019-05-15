from functools import wraps
def decorator_parameter_wrap(para = "default"):
    def function_decorator(func):
        @wraps(func)
        def decorator_wrapper(*args, **kwargs):
            print("You are now before the function needed to be decorated.")
            func(*args, **kwargs)
            print("You are now after the function needed to be decorated.")
            print("The passed in parameter is %s" % para)
        return decorator_wrapper
    return function_decorator

@decorator_parameter_wrap("decorator_wrapper")
def function_need_to_be_decorated():
    print("You are in the function that requires decoration.")

function_need_to_be_decorated()
print(function_need_to_be_decorated.__name__)

# The following code implements a decorator using class
class logit(object):
    _logfile = 'out.log'
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        print("Log is generated")
        # Now, send a notification
        self.notify()
        # return base func
        return self.func(*args, **kwargs)

    def notify(self):
        # logit only logs, no more
        pass

logit._logfile = 'out2.log' # if change log file
@logit
def myfunc1(x):
    return x

print(myfunc1(4))
# Output: myfunc1 was called
