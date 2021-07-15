mylist = ['prat', 'liva', 'amit', 'liza', 'ashu']

# for i in mylist:
#     # print(i)                     # i is a str type variable
#     if i.startswith('l'):          # i.startswith() chceks first letter of every element in list. if condition true then prints.
#         print('good morning '+ i)
#         # print(i)   

# # print(mylist[:]) #prints elements in list
# # print(i)      #prints last element. i[0] prints 1st letter of last element.

# for j in mylist:
  
#     if j.endswith('a'):
#         print('hello ', j)             

# for k in mylist:
#     # print(k)                   #simply prints all elemets in list


#how to greet names whose 2nd letter is 'i'?

for l in mylist:
    if l[1].startswith('i'):
        print('hey ', l)