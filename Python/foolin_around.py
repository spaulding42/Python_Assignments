# def multiply(num_list, num):
#     i = 0
#     for x in num_list:
#         x *= num
#         num_list[i] = x
#         i += 1
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)
# # output:
# # >>>[2,4,10,16]

def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16] 5
# >>>[2,4,10,16]

