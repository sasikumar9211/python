def named(**kwargs):
    print(kwargs)


def print_nicley(**kwargs):
    named(**kwargs)

    for name,age in kwargs.items():
        print(f"{age} :{name}")



print_nicley(name="Bob", age=25)