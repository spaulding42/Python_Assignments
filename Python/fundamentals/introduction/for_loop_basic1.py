"""
-----Done----1) print all ints from 0 to 150
-----Done----2) print all multiples of 5 from 5 to 1000
-----Done----3) print integers 1 to 100. if divisible by 5 print "coding" instead. if diisible by 10 print "Coding Dojo".
-----Done----4) add odd integers from 0 to 500,000
-----Done----5) print positive numbers starting at 2018, counting down by fours
-----Done----6) set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
    For example, if lowNum = 2, highNum = 9, and mult = 3, the loop should print 3,6,9
"""

# challange 1: print all ints from 0 to 150
print('print all ints from 0 to 150')
for x in range(151):
    print(x)

#challenge 2: print all multiples of 5 from 5 to 1000
print('print all multiples of 5 from 5 to 1000')
for x in range(5,1005,5):
    print(x)

#Challenge 3: print integers 1 to 100. if divisible by 5 print "coding" instead. if diisible by 10 print "Coding Dojo".
print('print integers 1 to 100. if divisible by 5 print "coding" instead. if diisible by 10 print "Coding Dojo"')
for x in range(1,101):
    if (x % 10 == 0):
        print("Coding Dojo")
    elif(x%5==0):
        print("Coding")
    else:
        print(x)

#Challenge 4: add odd integers from 0 to 500,000
print('add odd integers from 0 to 500,000')
sum = 0
for x in range(500000):
    if (x%2==1):
        sum = sum + x
print(sum)

#Challenge 5: print positive numbers starting at 2018, counting down by fours
print('print positive numbers starting at 2018, counting down by fours')
for x in range(2018, 0, -4):
    print(x)

#Challenge 6: set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
print('set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.')
lowNum = 2
highNum = 23
mult = 4
for x in range(lowNum, highNum+1):
    if (x%mult == 0):
        print(x)
