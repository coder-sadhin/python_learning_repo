from functools import reduce

lst=[1,3,5,7,8]

newL=reduce(lambda x,y:x+y,lst)

print(newL)


# another topic

# is and ==, is are same.
# no.......
# == are compare the value, and 'is' are compare to exact location