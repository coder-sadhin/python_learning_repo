# try:
#     l=[3,4,5,6]
#     i=int(input("Enter the index:  "))
#     print(l[i])
# except:
#     print("Some error occuted")
# finally:
#     print("this is inside finally")

def fun():
    try:
        l=[3,4,5,6]
        i=int(input("Enter the index:  "))
        print(l[i])
        return 1
    except:
        print("Some error occuted")
        return 0
    finally:
        print("this is insid e finally")
x= fun()
print(x)