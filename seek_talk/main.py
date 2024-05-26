with open("seek_talk/sample.txt",'r') as f:
    print(f)

# usally we use seek() function for skip char or data form starting 
    f.seek(10)
    print(f.tell())
    data=f.read(5)
    print(data)

# if i want to know from which char my code staring reading then we use tell()
    print(f.tell())
