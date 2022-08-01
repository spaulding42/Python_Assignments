"""
------ DONE-------1) Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
                        Example: countdown(5) should return [5,4,3,2,1,0]
-------Done-------2)  Create a function that will receive a list with two numbers. Print the first value and return the second.
                        Example: print_and_return([1,2]) should print 1 and return 2
-------Done ------3) Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
                        Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
-------Done-------4) Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
                        Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
                            Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
                            Example: values_greater_than_second([3]) should return False
-------Done-------5) Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, 
                        and whose values are all the given value.
                            Example: length_and_value(4,7) should return [7,7,7,7]
                            Example: length_and_value(6,2) should return [2,2,2,2,2,2]
"""


# Challenge 1: -------------------------------------
def countdown(num):
    new_list = []
    for x in range(num, 0, -1):
        new_list.append(x)
    return new_list

print("Challenge 1:")
print(countdown(5))


# Challenge 2: ---------------------------------------
def print1_return2(prin,ret):
    print(f'printed ' + str(prin))
    return ret

print("Challenge 2:")
returned = print1_return2(1,2)
print(f'returned {returned}')


#Challenge 3:---------------------------------------------
def first_plus_length(list):
    sum = list[0] + len(list)
    print(sum)
    return sum

print("Challenge 3:")
full_list = [5,4,3,2,1,0,3]
first_plus_length(full_list)

#Challenge 4: ----------------------------------------------
def values_greater_than_second(list):
    if len(list)<2:
        return False
    new_list = []
    greater_than_second_sum = 0
    for index in range(len(list)):
        if list[index] > list[2]:
            new_list.append(list[index])
            greater_than_second_sum += 1
    print(greater_than_second_sum, " numbers are greater than ", list[2])
    return new_list

print("Challenge 4:")
list = [4,5,2,2,1,2,3]
print(list)
newList = values_greater_than_second(list)
print(newList)

#Challenge 5: -----------------------------------------------------
#         Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    new_list = []
    for length in range(size):
        new_list.append(value)
    return new_list

print("Challenge 5:")
print(length_and_value(6,2))