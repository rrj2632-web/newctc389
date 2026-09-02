#Rogelio Jeronimo
#CTC-389-151

#August 23, 2026

#This is Lab 6

print ()
students = ["Amy", "Diego", "Karla", "Rosemarie", "Yasmin"]

for i in students:
    print (i)

options = ["Add student to list", "Modify student name", "Remove student"]

print ()
print ("A", options [0])
print ("M", options [1])
print ("R", options [2])

print ()
chose = input ("Please enter the letter corresponding to what you want to accomplish: ")

if chose == "A":
    print ()
    new_name = input (print ("Please enter the name of the student you want to add to the list: "))
    students.append (new_name)
    for i in students:
        print (i)

elif chose == "M":
    print ()
    print ("0", students [0])
    print ("1", students [1])
    print ("2", students [2])
    print ("3", students [3])
    print ("4", students [4])
    print ()
    number = int (input (print ("Please enter the number next to the name of the student you want to Modify: ")))
    print ()
    ne_name = input ("Please enter the name of the new student: ")
    students [number] = ne_name

    print ()
    for i in students:
        print (i)

else:
    print ()
    print ("0", students [0])
    print ("1", students [1])
    print ("2", students [2])
    print ("3", students [3])
    print ("4", students [4])
    print ()
    num = int (input (print (" Please enter the number next to the name of the student you want to remove: ")))
    print ()
    students.pop (num)

    print ()
    for i in students:
        print (i)


