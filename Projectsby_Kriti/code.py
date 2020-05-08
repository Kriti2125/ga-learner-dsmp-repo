# --------------
# Code starts here

class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']

class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
#Concatenation
new_class = class_1 + class_2
print("New class is : ", new_class)

#Appending new data
new_class.append("Peter Warden")
print("Updated new class is : ", new_class)
print(len(new_class))

#Removing data
new_class.remove("Carla Gentry")
print("Updated class list is : ", new_class)
len(new_class)
# Code ends here


# --------------
# Code starts here

courses = {'Math' : 65, 'English' : 70, 'History' : 80, 'French' : 70, 'Science' : 60}
print("The marks of Geoffrey Hinton in each subject : ", courses)

#Fetching only marks
marks = courses.values()
#print(marks)

#Getting the total
total = 0
for x in marks :
    total += x
print("The total marks of Geoffrey Hinton is :", total)  

#Calculate Percentage
percentage = total/ 500 * 100
print("Percentage of Geoffrey Hinton: ", percentage)

# Code ends here


# --------------
# Code starts here

mathematics = {'Geoffrey Hinton' : 78, 'Andrew Ng': 95, 'Sebastian Raschka' : 65, 'Yoshua Benjio' : 50, 'Hilary Mason' : 70, 'Corinna Cortes' : 66, 'Peter Warden' : 75 }

#marks_scored = mathematics.values()

#top_number = max(marks_scored)
topper = max(mathematics, key = mathematics.get)
print("The topper in mathematics is : ", topper)


# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here
first_name = topper.split()[0]
last_name = topper.split()[1]

full_name = last_name + ' ' + first_name
print("The toppper is ", full_name)

certificate_name = full_name.upper()
print("Cetificate name :", certificate_name)

# Code ends here


