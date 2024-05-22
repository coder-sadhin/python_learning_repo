a=int(input())
b=int(input())
want=input("What do you want to do? ,, \"+\", \"-\", \"*\", \"/\",\"//\", \"**\", \"%\" ")
match want:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case "//":
        print(a//b)
    case "**":
        print(a**b)
    case "%":
        print(a%b)
    case _:
        print("Input not correct")