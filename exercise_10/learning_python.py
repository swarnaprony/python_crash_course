#exercise_10_1
#learning_python
#will print the summary of learning python from txt file
#date: 18/06/2020

with open('summary_python_learning.txt') as new_file_object:
    new_summary = new_file_object.read()
    print(3*new_summary)
print("first attempt")



file_name_1 = 'summary_python_learning.txt'

with open(file_name_1) as file_object_1:
    lines_1 = file_object_1.readlines()

for line in lines_1:
    print(line)
print("looping over the file object")




file_name = 'summary_python_learning.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

summary = ''
for line in lines:
    summary += line

print(summary)
print("storing the lines into list")


#exercise_10_2
#replacing_python_by_Java


new_file_name = 'summary_python_learning.txt'

with open(new_file_name) as new_summary_object:
    new_lines = new_summary_object.readlines()

new_summary_java = ''
for line in new_lines:
    if 'Python' in line:
        new_line = line.replace('Python', 'Java')
    else:
        new_line = line

    new_summary_java += new_line.strip()
print(new_summary_java)