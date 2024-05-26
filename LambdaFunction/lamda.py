# try to duble a number using function
# def duble(x):
#     return x*x

# try to duble a number using lamda
# duble =lambda x:x*x
# print(duble(5))

def app(fx,value):
    return 6+fx(value)

print(app(lambda x:x*x*x,2))

# annonimus function called lamda function 