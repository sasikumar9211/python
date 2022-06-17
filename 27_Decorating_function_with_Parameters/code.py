import functools
user = {"username":"jose","access_level":"admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if user["access_level"] =="admin":
            return func(*args,**kwargs)
        else:
            return f" No admin permission"
    
    return secure_function


@make_secure
def get_admin_password(panel):
    if panel =="billing":
        return 1234
    elif panel == "admin":
        return 4567
    else:
        return 9883

print(get_admin_password("guest"))


