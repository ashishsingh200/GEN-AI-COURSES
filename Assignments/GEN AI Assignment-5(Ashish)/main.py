# from Task 1
# calling functions inside packages 
import Math_utils as m
from Math_utils import square

#Testing all those functions
print(m.add(9,10)) # functions for adding two numbers

print(m.subtract(50,20)) #functions for subtracting two numbers

print(square(20)) #function for finding square of a number


# from task 2
#created a module string_utils.py
# importing functions inside string_utils package
import String_utils as word

#testing all the functions inside package string_utils.py
text='ashish kumar singh'
print(word.capitalize_words(text))

print(word.reverse_string(text))

print(word.word_count(text))


# task 4 after completing task 3 
#importing packages  shop_package
import shop_package.discount as disc

from shop_package.billing import calculate_total

#importing all functions as instructed
from shop_package.discount import flat_discount
from shop_package.billing import apply_tax


# performing operations as instructed
print(disc.apply_discount(1000,10))

print(calculate_total([100,200,300]))
