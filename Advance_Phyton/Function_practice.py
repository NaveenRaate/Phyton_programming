#1
#Find all subject name of the canidtate
# di = {'Name':'Ajay','Salary':78000,'Subject':['Python','Java','SQL']}
# def subject_names(dir):
#     for i, j in dir.items():
#         if i == 'Subject':
#             print(j)
# subject_names(di)
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

# find out the candidate who have less than 30,000 salary
# def salary_less_than_30k(clist):
#     li=[]
#     for i in clist:
#         for j, k in i.items():
#             if j == 'Salary' and k <= 30000:
#                 print(k)
#                 li.append(i['Name'])
#     print(li)
#
# salary_less_than_30k(candidate_li)
###################################################################
# # find the candidate details , who have Python on his subject.
# def details_python_subject(clsit):
#     for i in clsit:
#         for j, k in i.items():
#             if j == 'Subject' and 'Python' in k:
#                 print(i)
# details_python_subject(candidate_li)
################################################################

#1 Remove all the duplicates word in a string without use any inbuilt function?
# string = 'i love india, going india, going to be , i'
# def remove_duplicate_words(input_string):
#     words = input_string.split() # ['i', 'love', 'india,', 'going', 'india,', 'going', 'to', 'be', ',', 'i']
#     unique_words = [] # after compare , only add original elements
#     seen_words = set()
#
#     for i in words:
#         unique_words.append(i)
#         seen_words.add(i)
#
#     result_string = ' '.join(seen_words)
#     print(result_string)
# remove_duplicate_words(string)

#2 Reverse the string all charcter without using inbuilt fucntion?

# string = 'i have string'
# # op = 'gnirts evah i'
# # print(string[::-1]) # using built in method
# def reverse_str(input_str):
#     reversed_string = ''
#
#     for char in input_str:
#         reversed_string = char+reversed_string
#     print(reversed_string)
# reverse_str(string)

################################################################
#3 Reverse string words without using inbuilt function?
# string = 'i have string'
# # op = 'string have i'
# def reverse_str(input_str):
#     words = input_str.split()
#     reversed_words = ''
#     # print(words)
#     for i in words:
#         reversed_words = i + reversed_words
#         reversed_words = ' '+ reversed_words
#     print(reversed_words)
# reverse_str(string)
###############################################
# 4 Reverse string words of char without using inbuilt function?
# string = 'i have string'
# # op = 'gnirts evah i'
# def reverse_char(input_str):
#     reversed_words = ''
#     for i in input_str:
#         reversed_words = i+reversed_words
#     print(reversed_words)
# reverse_char(string)

##################################################
#5 write Pllindrom number and string without use inbulit function?
#cac == cac
#121 == 121
#tac != cat
# input_string=input('Enter the value which you want to check whether its palindrome:')
# def find_palindrome(input):
#     string=''
#     for i in input:
#         string=i+string
#     if string == input:
#         print(input,'is a Palindrome')
#     else:
#         print(input, 'is not a palindrome')
# find_palindrome(input_string)

#########################################################
#6 write the anagram of string without using inbuilt function?

#listen == silent
# input1 = input('Enter the 1st value:-')
# input2 = input('Enter the 2nd value:-')
# def find_anagram(a,b):
#     e = []
#     g = []
#     c = 0
#     d = 0
#     for h in a:
#         g.append(h)
#     for k in b:
#         c += 1
#         e.append(k)
#     # print(e)
#     for i in g:
#         for j in e:
#             # print(j)
#             if i == j:
#                 g[d] = ' '
#                 d += 1
#                 break
#             else:
#                 continue
#     #     print(g)
#     # print(d,'d')
#     # print(c)
#     if c == d:
#         print('Two strings are Anagram')
#     else:
#         print('Two strings are not Anagram')
# find_anagram(input1,input2)
#####################################################

#Comprehension question list
# 1.Find all of the words in a string that are less than 5 char
# 2.Count the number of space in a string]

# 1.Find all of the words in a string that are less than 5 char
# string = 'This a very large city in my village surronding'
#
# def less_than_5char(str):
#     var = [element for element in str.split() if len(element)<5]
#     print(var)
# less_than_5char(string)
# 2.Count the number of space in a string]
# string = 'This a very large city in my village surronding'
# def space_count(str):
#     var =sum([1 for char in str if char== ' '])
#     print(var)
# space_count(string)
########################################################
#-----------------------------List Qurstion -----------------------------------------

# 1. Find the duplicate of list and remove it without using any inbuilt function
# 2. Reverse a list  without using any inbuilt function
# 3. fetch the data in nested list and add them
# 4. Swap a list without using any inbuilt function accending to decending
# 5. [2,[4,5],[4,,5,6],9] add this nested list
# 6. In a list if string their remove it without using any inbuilt function.

'''Find the duplicate of list and remove it without using any inbuilt function'''

# input_list = [1,2,3,4,1,2,3,5,6,7,7,7,8,8]
#
# def unique_num(li):
#     unique_list = []
#     for i in li:
#         if i not in unique_list:
#             unique_list.append(i)
#     print(unique_list)
# unique_num(input_list)

# list comprehension
# input_list = [1,2,3,4,1,2,3,5,6,7,7,7,8,8]
# def unique_num(li):
#     unique_list = []
#     var = [unique_list.append(i) for i in li if i not in unique_list]
#     print(unique_list)
# unique_num(input_list)


''' 2. Reverse a list  without using any inbuilt function'''

# input_list = [1,2,3,4,5]
# def reverse_list(li):
#     start_index = 0
#     end_index = len(li)-1
#
#     while start_index<end_index:
#         li[start_index],li[end_index] = li[end_index],li[start_index]
#         start_index = start_index+1
#         end_index = end_index-1
#
#     print(li)
# reverse_list(input_list)
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

# input_list = [3,1,4,2,5] # 3>1, 3>4, 3>2
# def acc_order(li):
#     for i in range(len(li)):#i = 0,1,2,3,
#         for j in range(i+1,len(li)):#j=1,2,3 , j = 2,3  j = 3
#             if li[i]>li[j]:
#                 li[i],li[j] = li[j],li[i]
#     print(li)
# acc_order(input_list)

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


# li = [12,13,1,4,'89','uo'] # don's use remove
#############################################################################33
# 6. In a list if string their remove it without using any inbuilt function.
input_list = [12,13,1,4,'89','uo'] # don's use remove
def remove_str(li):
    list_of_numbers = []
    for i in li:
        # print(type(i))
        if type(i) == str:
            continue
        else:
            list_of_numbers.append(i)

    print(list_of_numbers)
remove_str(input_list)