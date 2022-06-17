friends = [
{"name": "Rolf","age":20},
{"name": "Sam","age":22},
{"name": "Samantha","age":30},

]

print(friends[0])
print(friends[0]["name"])
print(friends[0]["age"])


student_attendance = {"Rolf":89,"Bob":98,"Anne":100}

for student,attendance in student_attendance.items():
    print(f"{student} :{attendance}")