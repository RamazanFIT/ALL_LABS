import os   

path = str()

path = str(input("Input path: "))

print("directories: ", [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])


list_objects = os.listdir(path)

print("files: ", [x for x in list_objects if os.path.isdir(not os.path.join(path, x))])

print("files and directories: ", [x for x in list_objects])