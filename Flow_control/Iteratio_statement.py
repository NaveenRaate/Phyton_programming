# li = [10,20,30.89,90.89,True,'String',[678,90],(68,90),{56,90}]
# nonCollection=[]
# for var in li:
#     print(var,type(var))
#     if type(var)==str or type(var) == list or type(var)==tuple or type(var)==set:
#        nonCollection.append(var)
# print(nonCollection)
#####################################
# li=[10,20,589,457,698]
# add=0
# for i in li:
#     add=add+i
# print(add)
##############################################
# 1
#li = [10,20,,78.89,67.56,'78',[90,90,89],(68,90)]
#add those itmes , those data type only int and float


# li = [10,20,78.89,67.56,'78',[90,90,89],(68,90)]
# a=0
# for i in li:
#     if type(i)== int or type(i) == float :
#        a+=i
# print(a)
######################################################
# 2
#di = {'Math':82,'Science':89,'History':78}
# li = [10,20]

#output = li [10,20,82,89,78] sum all the items in the list
# di = {'Math':82,'Science':89,'History':78}
# li = [10,20]
# a=0
# for k,v in di.items():
#     li.append(v)
# print(li)
# for i in li:
#     a+=i
# print(a)
#################################################################3
# star=int(input('Enter number of star you want to print:'))
#
# for i in range(star):
#     for j in range(star-i):
#         print('*',end='')
#     print()
#####################################################################
#1
#Find all subject name of the canidtate
# di = {'Name':'Ajay','Salary':78000,'Subject':['Python','Java','SQL']}
#
# for i, j in di.items():
#     if i == 'Subject':
#         print(j)
############################################################################
# 2
#
# candidate_li = [
# {'Name':'Ajay','Salary':78000,'Subject':['Python','Java','SQL']},
# {'Name':'Atul','Salary':67000,'Subject':['C','Perl']},
# {'Name':'Rahul','Salary':56000,'Subject':['Python','dotnet']},
# {'Name':'Sagar','Salary':23000,'Subject':['Perl','Java','SQL']},
# {'Name':'Sudharshan','Salary':34000,'Subject':['Kibana','Grafana','SAP']},
# {'Name':'Santosh','Salary':26000,'Subject':['Python','PlSql','SQL']}
#
# ]

# find out the candidate who have more than 30,000 salary
# li=[]
# for i in candidate_li:
#     for j, k in i.items():
#         if j == 'Salary' and k <= 30000:
#             print(k)
#             li.append(i['Name'])
# print(li)
###################################################################
# # find the candidate details , who have Python on his subject.
# for i in candidate_li:
#     for j, k in i.items():
#         if j == 'Subject' and 'Python' in k:
#             print(i)
################################################################

#1 Remove all the duplicates word in a string without use any inbuilt function?
# string = 'i love india, going india, going to be , i'
#
# words = string.split() # ['i', 'love', 'india,', 'going', 'india,', 'going', 'to', 'be', ',', 'i']
# unique_words = [] # after compare , only add original elements
# seen_words = set()
#
# for i in words:
#     unique_words.append(i)
#     seen_words.add(i)
#
# result_string = ' '.join(seen_words)
# print(result_string)


#2 Reverse the string all charcter without using inbuilt fucntion?

# string = 'i have string'
# op = 'gnirts evah i'
# print(string[::-1]) # using built in method
#
# reversed_string = ''
#
# for char in string:
#     reversed_string = char+reversed_string
# print(reversed_string)

################################################################
#3 Reverse string words without using inbuilt function?
# string = 'i have string'
# op = 'string have i'
# words = string.split()
# reversed_words = ''
# # print(words)
# for i in words:
#     reversed_words = i + reversed_words
#     reversed_words = ' '+ reversed_words
# print(reversed_words)
###############################################
# 4 Reverse string words of char without using inbuilt function?
# string = 'i have string'
# # op = 'gnirts evah i'
# reversed_words = ''
# for i in string:
#     reversed_words = i+reversed_words
# print(reversed_words)

##################################################
#5 write Pllindrom number and string without use inbulit function?
#cac == cac
#121 == 121
#tac != cat
# a=input('Enter the value which you want to check whether its palindrome:')
# b=''
# for i in a:
#     b=i+b
# if b == a:
#     print(a,'is a Palindrome')
# else:
#     print(a, 'is not a palindrome')

#########################################################
#6 write the anagram of string without using inbuilt function?

#listen == silent
# a = input('Enter the 1st value:-')
# b = input('Enter the 2nd value:-')
# e = []
# g = []
# c = 0
# d = 0
# for h in a:
#     g.append(h)
# for k in b:
#     c += 1
#     e.append(k)
# # print(e)
# for i in g:
#     for j in e:
#         # print(j)
#         if i == j:
#             g[d] = ' '
#             d += 1
#             break
#         else:
#             continue
# #     print(g)
# # print(d,'d')
# # print(c)
# if c == d:
#     print('Two strings are Anagram')
# else:
#     print('Two strings are not Anagram')
#####################################################

#Comprehension question list
# 1.Find all of the words in a string that are less than 5 char
# 2.Count the number of space in a string]

# 1.Find all of the words in a string that are less than 5 char
# str = 'This a very large city in my village surronding'
#
# # var = [each_word for each_word in str.split() if len(each_word)<5]
#
# var = [element for element in str.split() if len(element)<5]
# print(var)

# 2.Count the number of space in a string]
# str = 'This a very large city in my village surronding'
#
# var =sum([1 for char in str if char== ' '])
# print(var)

########################################################
#-----------------------------List Qurstion -----------------------------------------

# 1. Find the duplicate of list and remove it without using any inbuilt function
# 2. Reverse a list  without using any inbuilt function
# 3. fetch the data in nested list and add them
# 4. Swap a list without using any inbuilt function accending to decending
# 5. [2,[4,5],[4,,5,6],9] add this nested list
# 6. In a list if string their remove it without using any inbuilt function.

'''Find the duplicate of list and remove it without using any inbuilt function'''

# li = [1,2,3,4,1,2,3,5,6,7,7,7,8,8]
# unique_list = []

# for i in li:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

#list comprehension
# var = [unique_list.append(i) for i in li if i not in unique_list]
# print(unique_list)


''' 2. Reverse a list  without using any inbuilt function'''

# li = [1,2,3,4,5]
#
# start_index = 0
# end_index = len(li)-1
#
# while start_index<end_index:
#     li[start_index],li[end_index] = li[end_index],li[start_index]
#     start_index = start_index+1
#     end_index = end_index-1
#
# print(li)

'''# 3. fetch the data in nested list and add them'''

# li = [
#     [1,2,3],
#     [3,4,5],
#     [9,8,7]
# ]
#
# for element in li:
#     for i in element:
#         print(i)





'''4. Swap a list without using any inbuilt function accending to decending'''

# li = [3,1,4,2,5] # 3>1, 3>4, 3>2
#
# for i in range(len(li)):#i = 0,1,2,3,
#     for j in range(i+1,len(li)):#j=1,2,3 , j = 2,3  j = 3
#         if li[i]>li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li)


'''# 5. [2,[4,5],[4,5,6],9] add this nested list'''

# li = [2,[4,5],[4,5,[6,8]],9]
#
# def recursive_sum(li):
#     sum = 0
#     for i in li:
#         if isinstance(i,list):
#             sum = sum + recursive_sum(i)
#         else:
#             sum = sum+i
#     return sum
# print(recursive_sum(li))
#

li = [12,13,1,4,'89','uo'] # don's use remove
#############################################################################33
# 6. In a list if string their remove it without using any inbuilt function.
# li = [12,13,1,4,'89','uo'] # don's use remove
# list_of_numbers = []
#
# for i in li:
#     # print(type(i))
#     if type(i) == str:
#         continue
#     else:
#         list_of_numbers.append(i)
#
# print(list_of_numbers)