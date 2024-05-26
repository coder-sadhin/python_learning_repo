lst=[1,3,5,6,7,8]
def cube(x):
    return x*x*x

newL=list(map(cube,lst))
print(newL)