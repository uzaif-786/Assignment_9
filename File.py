File  = open("data.csv","w")

File.writelines('''RollNo,Name,Marks\n,
12,Rohit,56\n,
145,Rohit,56\n,
13,wrt,6\n
15,dosf,32\n''')

File = open("data.csv","r")
i= -1
for i in File:
    i+= 1
    if i == 4:
        my_line = line
        break

spl = File.readline()
line = spl[3]

lyn =  line.split(",")\

# print(lyn)

Roll = lyn[0]
Name = lyn[1]
Marks = lyn[2]

print(f"ROll No: {Roll}")
print(f"Name: {Name}")
print(f"Marks: {Marks}")

File.close()