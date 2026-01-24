# File Handling - how to handle(read,write,append) a file
#rwa
data = '''HELLO
welcome to python
lets learn file handling'''
file = open(file="myfile.txt",mode="w")
file.write(data)
file.close()