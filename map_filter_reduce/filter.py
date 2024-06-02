def fil(x):
    return x>4
lst=[2,3,5,7,8]
newfilfee= list(filter(fil,lst))
print(newfilfee)
# this functon works like a water filter.
# if you at some conditon and use filter.
# then you gate your expacted value

# map, filter, reduce are higher order function