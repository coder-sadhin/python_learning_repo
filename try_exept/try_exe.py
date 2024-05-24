n=input("Enter a number:  ")
print(f"Multiplication of {n}")

# if i give input intiger
# for i in range(1,11):
#     print(f"{int(n)} * {i} = {int(n)*i}")

# if issu some eroor
try:
    for i in range(1,11):
        print(f"{int(n)} * {i} = {int(n)*i}")
except Exception as e:
    print("sorry, I have some error")



# inside of this method have any Exception
