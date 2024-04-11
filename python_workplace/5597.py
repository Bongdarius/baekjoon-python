students = [];
allStudents = [];

for i in range(28):
    students.append(int(input()));
students.sort();

for i in range(30):
    allStudents.append(i+1);

for i in students:
    allStudents.remove(i);

print(allStudents[0]);
print(allStudents[1]);