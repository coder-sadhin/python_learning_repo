try:
    with open('IO/myfile.txt', 'r') as f:
        text = f.read()
        if not text:
            print("The file is empty.")
        else:
            print(text)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")


    # READING A FILE

# f = open('myfile.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()

# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside with")
