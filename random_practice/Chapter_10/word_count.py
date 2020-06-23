#Working with multiple Files

def count_words(file_name):
    """Counts the approximate word in a file"""

    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
 #       print(f"Sorry the file {file_name} does not exsist.")
        pass

    else:
        #count the approximate number of words in the file.
            words = contents.split()
            num_words = len(words)
            print(f"The file {file_name} has about {num_words} words.")

file_name = 'C:\\Users\\asifhossain\\Documents\\python_work\\random_practice\\Chapter_10\\paragraph.txt'
count_words(file_name)

file_names = ['C:\\Users\\asifhossain\\Documents\\python_work\\random_practice\\Chapter_10\\paragraph.txt', 'sidharta.txt']
for file_name in file_names:
    count_words(file_name)
