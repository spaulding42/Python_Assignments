"""
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
"""

# Challenge 1 -----------------------------------------------------
print("Challenge 1----------")
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print(students[0])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30
print(z)

# Challenge 2---------------------------------------------
print("Challenge 2------------")
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(list):
    for i in range(len(list)):
        print("first_name - " + list[i]["first_name"] + ", last_name "+ list[i]["last_name"])
iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# # Challenge 3 --------------------------------------------------------
print("Challenge 3------------")
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

print("First Names: ")
iterateDictionary2("first_name", students)
print("Last Names: ")
iterateDictionary2("last_name", students)


# Challenge 4 --------------------------------------------------------
print("Challenge 4---------")
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dict):
    print(str(len(dict["locations"])) + " LOCATIONS")
    for i in range(len(dict["locations"])):
        print(dict["locations"][i])
    print("    ")
    print(str(len(dict["instructors"])) + " INSTRUCTORS")
    for i in range(len(dict["instructors"])):
        print(dict["instructors"][i])
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
