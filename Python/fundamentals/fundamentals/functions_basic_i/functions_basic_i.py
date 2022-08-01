# #1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#------------ outputs the number 5

# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# ----------------crashes because number_of_days_in_a_week_silicon_or_triangle_sides() function is not defined

# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#--------- returns 5 and never gets to return 10

# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# -------------returns 5 and never gets to the print command... its even greyed out in vs code... it must know it will never get to that point

# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# ---------------output will be "5, None" since the function is not returning any value its default return is "None"

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
# ----------------output: 3, 5, then crashes because nothing is being returned and you can't add none to none


# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# -----------------"25" converts the int to a string then sticks the two strings together returning a string "25"


# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# --------------- prints 100, 10   will never return 7 because if b < 10 it will return 5 and if that isn't true it will always return 10

# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#-------- 7, 14, 21

# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#-------------------- prints 8. will never get to second return statement even if the result of b+c is 10


# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#------------ prints 500, 500, 300, 500  the b in the for loop is a different int than the b that was initially defined


# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# ------------- prints: 500, 500, 300, 500 return b was never stored in anything so it accomplished nothing

# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#------------ prints: 500, 500, 300, 300 the outer b received the value of the inner b from the return function

# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#---------- prints: 1, 3, 2


# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#------------ prints: 1, 3, 5, 10