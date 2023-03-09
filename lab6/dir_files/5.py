# list to a file


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = open("sometask.txt", "a")
f = open("sometask.txt", "w")


for i in some_list:
    f.write(str(i))
    f.write("\n")
