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
# new_list=[]
# def remove_duplicate(*args):
#     for i in args:
#         if i not in new_list:
#             new_list.append(i)
#     print(new_list)
#
# remove_duplicate(1,1,1,2,2,2,89,89,78,54,12)
##############################################
# find_biggest_of_two_numbers = lambda num1,num2: num1 if num1>num2 else num2
# print(find_biggest_of_two_numbers(51,89))
#######################################

# palandrome = lambda str: 'palindrome' if str == str[::-1] else 'not a palindrome'
# print(palandrome('madam'))
#######################################
# def add(a,b):
#     result = a+b # 30
#     def squre(sqr):
#         squre_result = result*result
#         return squre_result
#     return result,squre(result)
#
# print(add(10,20))
# # print(add('qwer',90))
######################################3
#WAP multiple two number and check the number even or odd help nested function?
# def multiplication_of_two_numbers(num1,num2):
#     result = num1*num2
#     def even_or_odd(num3):
#         if num3%2 == 0:
#             return num3,'is even'
#         else:
#             return num3,'is odd'
#     return result,even_or_odd(result)
#
# print(multiplication_of_two_numbers(10,20))
#######################################
# li = [12,'ui',90,'67',34,'qwerty','23',45,49,11,'yuo',42]
# def remove_string(li):
#     list_of_numbers=[]
#     for i in li:
#         # print(type(i))
#         if type(i) == str:
#             continue
#         else:
#             list_of_numbers.append(i)
#     def sort_num(list):
#         # print(list)
#         sorted_list = sorted(list)
#         return sorted_list
#     return sort_num(list_of_numbers)
# print(remove_string(li),)
###########################################
#
# li = [12,'ui',90,'67',34,'qwerty','23',45,49,11,'yuo',42]
#
#
# def str_remove(list):
#     for i in list[:]:
#         # print(i, type(i))
#         if type(i) == str:
#             list.remove(i)
# str_remove(li)
# print(li)

###################################################
# def decore(even_or_odd):
#     def palindrome(num):
#         if str(num) == str(num)[::-1]:
#             return 'palindrome', even_or_odd(num)
#         else:
#             return 'not a palindrome', even_or_odd(num)
#     return palindrome
# @decore
# def even_or_odd(num):
#     if num%2==0:
#         return 'Even'
#     else:
#         return 'Odd'
#
# print(even_or_odd(121))
########################################################################
# without string slicing
def decore(even_or_odd):
    def palindrome(num):
        original_num = num
        reversed_num = 0

        while num > 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num = num // 10

        if original_num == reversed_num:
            return 'palindrome', even_or_odd(original_num)
        else:
            return 'not a palindrome', even_or_odd(original_num)

    return palindrome

@decore
def even_or_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(even_or_odd(54346))

#################################################################
# def decore2(cal):
#     def div(num1,num2):
#         div_result= num1%num2
#         return div_result, cal(num1,num2)
#     return div
# def decore1(cal):
#     def sub(num1,num2):
#         sub_result= num1-num2
#         return sub_result, cal(num1,num2)
#     return sub
# def decore(cal):
#     def mul(num1, num2):
#         mul_result= num1*num2
#         return mul_result, cal(num1,num2)
#     return mul
# @decore2
# @decore1
# @decore
# def cal(num1,num2):
#     add_result=num1+num2
#     return add_result
#
# print(cal(15,18))
