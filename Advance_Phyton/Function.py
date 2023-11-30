# write a function fetch the all list element?

# def fetch_list(li):
#     for i in li:
#         print(i)
#
# list = [20,67,[54,89],'String']
# fetch_list(list)



# write a fucntion find the biggest number among two?

# def find_biggest_of_two_numbers (num1,num2):
#     if num1>num2:
#         print(num1,'is the biggest number')
#     elif num2>num1:
#         print(num2, 'is the biggest number')
#     else:
#         print(num1,num2, 'are same')
#
# print(find_biggest_of_two_numbers(51,89))

###############################################
# def palindrome (str):
#     revirse_str = str[::-1]
#     if str == revirse_str:
#         print(str,'is a palindrome')
#     else:
#         print(str,'not a palindrome')
#
# palindrome('level')

###############################################
new_list=[]
def remove_duplicate(*args):
    for i in args:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

remove_duplicate(1,1,1,2,2,2,89,89,78,54,12)