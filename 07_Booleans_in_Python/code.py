friends = ["Rolf","Bob"]
abroad = ["Rolf","Bob"]

local_friends =friends

print(friends == abroad)

print(friends is abroad)

print(friends is local_friends)

str = "Sasikumar B"
str2 ="SASIKUMAR"

print(str.casefold() == str2.casefold())