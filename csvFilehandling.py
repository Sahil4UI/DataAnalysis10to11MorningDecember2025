#WRITING DATA IN EXCEL CSV
# data = [{"id":101,"name":"amit","marks":80},
#         {"id":102,"name":"lokesh","marks":70},
#         {"id":103,"name":"vinay","marks":60},
#         {"id":104,"name":"suresh","marks":40},
#         {"id":105,"name":"vinay","marks":30}]

# import csv

# with open("a.csv","w") as file:
#     writer = csv.DictWriter(file,fieldnames=["id","name","marks"])
#     writer.writeheader()
#     writer.writerows(data)

#READING DATA FROM EXCEL CSV FILE

import csv 
with open("a.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)