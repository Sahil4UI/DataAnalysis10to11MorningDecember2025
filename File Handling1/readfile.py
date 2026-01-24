file = open(file="myfile.txt",mode="r")
# data = file.read()
# data = file.read(3)#read 3 character only
# data = file.readline()#read first line
data = file.readlines()#it will give us list
print(data[2])

file.close()