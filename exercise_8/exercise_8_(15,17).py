#exercise_8_(15,17)
#date: 08/04/2020

#exercise_8_15
#import_module
#printing_models

import printing_function
user_profile = printing_function.print_name('mir', 'md', profession = 'engineer', age = '30')
print(user_profile)

from printing_function import print_name
user_profile = print_name('swarna', 'sarker', profession = 'student', age = '29')
print(user_profile)

from printing_function import print_name as printing_name
user_profile = printing_name('swarna', 'sarker', profession = 'student', age = '29')
print(user_profile)

import printing_function as pf
user_profile = pf.print_name('swarna', 'sarker', profession = 'student', age = '29')
print(user_profile)

from printing_function import *
print_name_again()