with open("log.txt",'r') as file :
    data=file.read()
    
with open("log.txt",'a') as file :
   print('\n')
   file.write("\n i am append new data to file \n")
    
print(data)

