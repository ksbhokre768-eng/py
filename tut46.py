import os
# os.mkdir("data")  #to create directory

for i in range(46 ,100):
    os.mkdir(f".vscode/tut{i+1}.py")  #to create files
    # os.rename(f"__pycache__/tut.py{i+1}" ,f"__pycache__/tut{i+1}.py") #rename/
    # file_path= f"__pycache__/day{i}"
    # os.remove(file_path)

folders=os.listdir("__pycache__")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"__pycache__/{folder}"))
