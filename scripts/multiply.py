"""
This script provide a method to multiply the items of a list of integers
"""

def list_product(my_list):
    result = 1
    for n in my_list:
        if int(n):
            result = result * n
	else:
	    result = 'Error, cannot multiply with a non integer'
    return result
  
print(list_product([2,4]))
print(list_product([2,10,15]))

