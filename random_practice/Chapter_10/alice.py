#Handling the file not found exception

title = " Alice in Wonderland"
print(title.split())

file_name = 'C:\\Users\\asifhossain\\Documents\\python_work\\random_practice\\Chapter_10\\paragraph.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {file_name} does not exsist.")

else:
    #count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_name} has about {num_words} words.")
