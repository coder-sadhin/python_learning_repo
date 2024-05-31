import os

files = os.listdir("all_exersize/ex_7/clutteredFolder")
i = 1
for file in files:
  if file.endswith(".jpg"):
    print(file)
    os.rename(f"all_exersize/ex_7/clutteredFolder/{file}", f"all_exersize/ex_7/clutteredFolder/{i}.jpg")
    i = i + 1