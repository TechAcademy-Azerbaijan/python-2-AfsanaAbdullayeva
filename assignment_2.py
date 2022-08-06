from os.path import exists
from datetime import datetime
if not exists('sample.txt'):
    with open('sample.txt', 'w') as f:
        f.write('Function name\t|\tWorked time\t|\tArguments as list\t|\tArguments as dictionary\t|\tFunction results\t|\n') 
def logger(func):
    def wrapper(*args,**kwargs):
        try:
            result = func(*args, **kwargs)
        except ZeroDivisionError as error:
            result = error
        except TypeError as error:
            result = error
        except NameError as error:
            result = error
        except Exception as error:
            result = error
        with open('sample.txt','a') as f:
            if args and kwargs:
                f.write(f'{func.__name__}\t\t\|\t{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}|\t\t\t\t{args}\t\t\t\t|\t\t\t\t{kwargs}\t\t\t\t|\t{result}\t|\n')
            elif args:
                f.write(f'{func.__name__}\t\t\|\t{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}|\t\t\t\t{args}\t|\t\t\t\t{str()}\t\t\t\t|\t{result}\t\t\t\t|\n')
            elif kwargs:
                f.write(f'{func.__name__}\t\t\|\t{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}|\t\t\t\t{str()}\t\t\t\t|\t{kwargs}\t\t\t\t|\t{result}\t\t\t\t|\n')
    return wrapper
@logger
def sum(a,b):
    return a+b
@logger
def divide(a,b):
    return a/b
sum(1,2)
divide(a='j',b=2)
divide(a=2, b=1.5)
divide(10,0)