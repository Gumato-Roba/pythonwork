def hello():
    print("Hello Adalab")

def hello(name,age):
    year = 2022-age
    print(f"Hello {name} you were born in {year}")

def hello2(name):
    print(f"Hello {name}")
    return
    print(f"Welcome to Adalab")

def hello3(name):
    return f"Hello {name}"

def greet(name,age):
    year= 2022-age
    return f"Hello {name} you were born in {year}"

# default keyword
def my_country(name,country="Uganda"):
    return f"Hello {name} from {country}"

def Hello_multi(*names):
    for name in names:
        print(f"Hello {name}")

def sum(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum

def greet_multiple(**kwargs):
    keys = kwargs.keys()
    if "name" in keys:
        print("Hello { kwargs['name']}")
    elif "country" in keys:
        print("Hello from { kwargs['country']}")
    else:
        print("Hello anonymous")

def sum_and_greet(*args, **kwargs):
        print(args)
        print(kwargs)


 

