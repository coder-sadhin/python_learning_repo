with open("seek_talk/sample2.txt",'w') as f:
    f.write('Hello world, I am md akkas ali')
    f.truncate(5)
# we use truncate for talk how many word are store in my file

with open("seek_talk/sample2.txt") as f:
    print(f.read())