users = [
    (0,"Bob","password"),
    (1,"ROlf","1234"),
    (2,"Jose","Rad123")
]

username_mapping = { user[1]:user for user in users}

username_input  = input("Enter your username:")
password_input  =  input("Enter your password:").lower()

_,user_name,password = username_mapping [username_input]

if password.lower() == password_input:
    print("your details are correct..")
else:
    print("your details are not correct..")