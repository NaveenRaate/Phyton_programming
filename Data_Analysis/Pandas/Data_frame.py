# array = [10,10,20,30]
#
# li = [10,68,'5678',[567,89]]

import pandas as pd

name  = ['Deba','Naveen','Ganesh']
age = [25,26,27]

'''Basic List'''
data_frame = pd.DataFrame(list(zip(name,age)),columns=['Names','Ages'])

print(data_frame)

'''Nested List'''

# data_frame = pd.DataFrame({'Names':name,'Ages':age})
# print(data_frame)


'''Dictionary'''

# students_name = {
#     'Name':['Deba','Naveen','Ganesh'],
#     'Age':[25,26,27],
#     'State':['Odisha','Karnataka','Maharastra'],
#     'Country':'India'
# }

# data_frame = pd.DataFrame(students_name)
# print(data_frame)

'''dictionary of lits'''

# data_frame = pd.DataFrame.from_dict(students_name)
# print(data_frame)


'''Settings  Column Names'''

# students_name = {
#     'Name':['Deba','Naveen','Ganesh'],
#     'Age':[25,26,27],
#     'State':['Odisha','Karnataka','Maharastra'],
#     'Country':'India'
# }

# data_frame = pd.DataFrame.from_dict(students_name)
# data_frame.columns = ['Na','Ag','St','Cou']
# print(data_frame)

'''Setting Row Index'''

# data_frame = pd.DataFrame.from_dict(students_name)
# data_frame.index = ['STD-1','STD-2','STD-3']
# print(data_frame)


#Data Access and manipulation

#using .iloc[] for position baed indexing

students_name = {
    'Name':['Deba','Naveen','Ganesh','Rathod','Subha'],
    'Age':[25,26,27,34,45],
    'State':['Odisha','Karnataka','Maharastra','Karnataka','Maharastra'],
}

students_df = pd.DataFrame(students_name)

'''accessing the first row'''
# first_row = students_df.iloc[0]
# print(first_row)

'''accessing the first column all rows'''
# first_column = students_df.iloc[:,0]
# print(first_column)

'''acceessing a specific cell like (row2,column2)'''

specific_cell = students_df.iloc[0,2]
print(specific_cell)

