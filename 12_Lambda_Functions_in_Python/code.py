sequence =[1,2,3,4]

double = [(lambda x :2*x)(x) for x in sequence]

print(double)

map_double = list(map(lambda x :2*x,sequence))

print(map_double)