data = '''\nhey.......how are you?'''
#a means append
with open(file="myfile.txt",mode="a") as file:
    file.write(data)