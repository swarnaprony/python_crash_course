#exercise_10_8
#Cats_and_dogs

def cat_dog_names():
    """Printing the name of the dogs and cats reading from text files with error handling"""

    cats_name = "C:\\Users\\asifhossain\\Documents\\python_work\\exercise_10\\cats_name.txt"
    dogs_name = "C:\\Users\\asifhossain\\Documents\\python_work\\exercise_10\\dogs_name.txt"

    try:
        with open(cats_name, 'r') as cats_name_object:
            cats_name_list = cats_name_object.readlines()
            cats = ''
            for cat_name in(cats_name_list):
                print(f"name of the cat is : {cat_name.rstrip()}")
                cats += str(cat_name)

    except FileNotFoundError:
        pass

    else:
        words = cats.split()
        num_words = len(words)
        print(f"Length of the text is: {num_words}")

    try:
        with open(dogs_name, 'r') as dogs_name_object:
            dogs_name_list = dogs_name_object.readlines()
            for dog_name in(dogs_name_list):
                print(f"name of the dog is : {dog_name.rstrip()}")
    except FileNotFoundError:
        print("File is missing")

cat_dog_names()