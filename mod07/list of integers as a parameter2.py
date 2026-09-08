# Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list except
# that all uneven numbers have been removed. 
# For testing, write a main program where you create a list, call the function, 
# and then print out both the original as well as the cut-down list.

def function_name(numbers):
    second_list = []

    for i in numbers:
        if i % 2 == 0:
            second_list.append(i)
    return second_list

original_list=[0,2,4,6,7,9,32,65,89,94]
result = function_name(original_list)
print(original_list)
print(result)


    