from csv import reader
from time import sleep


with open('iot_project/IoT_Project/Data/Processed/inside.csv', 'r') as entries:
    csv_reader = reader(entries)
    header = next(csv_reader)  
    if header != None:
        for row in csv_reader:
            print(row)
            sleep(2)
           
# with open('iot_project/IoT_Project/Data/Processed/out.csv', 'r') as entries:
#     csv_reader = reader(entries)
#     header = next(csv_reader)  
#     if header != None:
#         for row in csv_reader:
#             print(row)
