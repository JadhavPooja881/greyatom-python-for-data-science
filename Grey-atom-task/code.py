# --------------
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
courses = {'Math':65,'English':70,'History':80,'French':70,'Science':60}
values = courses.values()
total = sum(values)
print(total)
percentage = (total*100)/500
print(percentage)
mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter warden':75}
max_marks_scored = max(courses,key = courses.get)
print(max_marks_scored)
topper = max(mathematics,key = mathematics.get)
print(topper)
first_name = topper.split()[0]
last_name = topper.split()[1]
certificate_name = last_name.upper() +" " +first_name.upper()
print(certificate_name) 









